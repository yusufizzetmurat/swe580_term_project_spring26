import argparse
import json
import os
import re
import sys
import time
from datetime import datetime

from search_backend import build_index
from llm_runner import LLMRunner
from executors import create_executor_a, create_executor_b
from note_creation import with_create_tool, wrap_executor_with_create


SYNTH_PROMPT_TAIL = """

You also have a create_note tool. When the user asks you to create, write, or compose a new note, first search the vault for the notes you should link to, then call create_note with the body containing [[wiki-links]] to them. After creating, end your reply with RESULT_PATHS containing the new note's path.
"""


def load_config(cfg):
    with open(f"config_{cfg}_tools.json") as f:
        tools = json.load(f)
    with open(f"config_{cfg}_prompt.txt") as f:
        prompt = f.read()
    return with_create_tool(tools), prompt + SYNTH_PROMPT_TAIL


def verify(write_root, expected_path, must_link_to, expected_tags):
    full = os.path.join(write_root, expected_path)
    if not os.path.exists(full):
        return {
            "file_exists": False,
            "links_ok": False,
            "tags_ok": False,
            "missing_links": must_link_to,
            "missing_tags": expected_tags,
        }

    with open(full, encoding="utf-8") as f:
        text = f.read()

    def norm(s):
        return s.strip().replace("_", " ").lower()

    found_links = {norm(l) for l in re.findall(r"\[\[([^\]]+)\]\]", text)}
    missing_links = [l for l in must_link_to if norm(l) not in found_links]

    found_tags = set()
    fm = re.match(r"^---\s*\n(.*?)\n---\s*\n", text, re.DOTALL)
    if fm:
        tag_match = re.search(r"^tags:\s*\[([^\]]*)\]", fm.group(1), re.MULTILINE)
        if tag_match:
            for raw in tag_match.group(1).split(","):
                t = raw.strip().strip("'\"").lower()
                if t:
                    found_tags.add(t)
    missing_tags = [t for t in expected_tags if t.lower() not in found_tags]

    return {
        "file_exists": True,
        "found_links": sorted(found_links),
        "missing_links": missing_links,
        "links_ok": not missing_links,
        "found_tags": sorted(found_tags),
        "missing_tags": missing_tags,
        "tags_ok": not missing_tags,
    }


def cleanup_previous(write_root, queries):
    for q in queries:
        target = os.path.join(write_root, q["expected_path"])
        if os.path.exists(target):
            os.remove(target)


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--api-key", default=os.environ.get("LLM_API_KEY"))
    p.add_argument("--base-url", default="https://openrouter.ai/api/v1")
    p.add_argument("--model", default="google/gemini-2.5-flash")
    p.add_argument("--vault", default="vault",
                   help="Read-only vault used by the search tools.")
    p.add_argument("--write-root", default="results/synthesis/notes",
                   help="Where created notes are written. Kept separate from the vault.")
    p.add_argument("--queries", default="synthesis_queries.json")
    p.add_argument("--config", choices=["a", "b"], default="a")
    p.add_argument("--output-dir", default="results/synthesis")
    p.add_argument("--delay", type=float, default=1.5)
    p.add_argument("--verbose", action="store_true")
    args = p.parse_args()

    if not args.api_key:
        print("ERROR: provide --api-key or set LLM_API_KEY", file=sys.stderr)
        sys.exit(1)

    with open(args.queries) as f:
        queries = json.load(f)["queries"]

    os.makedirs(args.write_root, exist_ok=True)
    cleanup_previous(args.write_root, queries)

    ix = build_index(args.vault)
    base = (create_executor_a if args.config == "a" else create_executor_b)(ix)
    executor = wrap_executor_with_create(base, args.write_root)
    tools, prompt = load_config(args.config)

    runner = LLMRunner(base_url=args.base_url, api_key=args.api_key, model=args.model)
    print(f"Model: {args.model}  |  Config: {args.config}  |  {len(queries)} queries")
    print(f"Reading vault: {args.vault}   Writing notes to: {args.write_root}")

    results = []
    for i, q in enumerate(queries):
        print(f"\n[{i+1}/{len(queries)}] {q['id']}: {q['query'][:80]}...")
        try:
            r = runner.run(query=q["query"], tools=tools, tool_executor=executor,
                           system_prompt=prompt, verbose=args.verbose)
            v = verify(args.write_root, q["expected_path"],
                       q.get("must_link_to", []), q.get("expected_tags", []))
            ok = v["file_exists"] and v["links_ok"] and v["tags_ok"]
            print(f"  file={v['file_exists']} links={v['links_ok']} tags={v['tags_ok']} => {'PASS' if ok else 'FAIL'}")
            results.append({
                "query_id": q["id"],
                "query": q["query"],
                "expected_path": q["expected_path"],
                "success": ok,
                "verification": v,
                "tool_calls": [t["tool"] for t in r["tool_calls"]],
                "total_tokens": r["total_input_tokens"] + r["total_output_tokens"],
                "latency_seconds": r["latency_seconds"],
            })
        except Exception as e:
            print(f"  ERROR: {e}")
            results.append({"query_id": q["id"], "error": str(e), "success": False})

        if i < len(queries) - 1:
            time.sleep(args.delay)

    n = len(results)
    summary = {
        "model": args.model,
        "config": args.config,
        "vault": args.vault,
        "write_root": args.write_root,
        "num_queries": n,
        "success_count": sum(1 for r in results if r.get("success")),
        "success_rate": round(sum(1 for r in results if r.get("success")) / n, 3) if n else 0,
        "results": results,
    }

    os.makedirs(args.output_dir, exist_ok=True)
    stamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    out = os.path.join(args.output_dir, f"synthesis_{args.config}_{stamp}.json")
    with open(out, "w") as f:
        json.dump(summary, f, indent=2)
    print(f"\n{summary['success_count']}/{n} passed ({summary['success_rate']})")
    print(f"Saved to: {out}")


if __name__ == "__main__":
    main()
