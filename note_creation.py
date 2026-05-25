import os
from datetime import datetime


CREATE_NOTE_TOOL = {
    "type": "function",
    "function": {
        "name": "create_note",
        "description": (
            "Write a new markdown note. Use this when the user asks you to "
            "create, write, or compose a new note (for example, a summary "
            "that links to several existing notes). The note gets YAML "
            "frontmatter with tags and timestamps. Put [[wiki-links]] in the "
            "body to reference notes in the vault."
        ),
        "parameters": {
            "type": "object",
            "properties": {
                "path": {
                    "type": "string",
                    "description": "Target path ending in .md, e.g. projects/Attention_Summary.md."
                },
                "title": {
                    "type": "string",
                    "description": "Heading title. Defaults to the filename."
                },
                "content": {
                    "type": "string",
                    "description": "Markdown body. Use [[Note_Title]] to link to vault notes."
                },
                "tags": {
                    "type": "array",
                    "items": {"type": "string"},
                    "description": "Lowercase tags for the frontmatter."
                },
                "overwrite": {
                    "type": "boolean",
                    "description": "Replace an existing note at the same path. Default false.",
                    "default": False
                }
            },
            "required": ["path", "content"]
        }
    }
}


def _title_from_path(path):
    base = os.path.basename(path)
    if base.endswith(".md"):
        base = base[:-3]
    return base.replace("_", " ")


def _frontmatter(tags, now):
    iso = now.strftime("%Y-%m-%dT%H:%M:%S")
    tag_line = "[]" if not tags else "[" + ", ".join(str(t).lower() for t in tags) + "]"
    return f"---\ntags: {tag_line}\ncreated: {iso}\nmodified: {iso}\n---\n\n"


def create_note(write_root, path, content, title=None, tags=None, overwrite=False):
    if not path.endswith(".md"):
        return {"error": "path must end in .md"}
    if "/" not in path:
        return {"error": "path must include a folder, e.g. projects/Foo.md"}

    full_path = os.path.join(write_root, path)
    if os.path.exists(full_path) and not overwrite:
        return {"error": "Note already exists. Set overwrite=true to replace.", "path": path}

    os.makedirs(os.path.dirname(full_path), exist_ok=True)

    if not title:
        title = _title_from_path(path)

    now = datetime.now()
    body = f"# {title}\n\n{content.strip()}\n"
    with open(full_path, "w", encoding="utf-8") as f:
        f.write(_frontmatter(tags, now) + body)

    return {
        "ok": True,
        "path": path,
        "title": title,
        "tags": tags or [],
        "created": now.isoformat(),
    }


def wrap_executor_with_create(base_executor, write_root):
    def wrapped(tool_name, args):
        if tool_name == "create_note":
            return create_note(
                write_root=write_root,
                path=args["path"],
                content=args.get("content", ""),
                title=args.get("title"),
                tags=args.get("tags"),
                overwrite=bool(args.get("overwrite", False)),
            )
        return base_executor(tool_name, args)
    return wrapped


def with_create_tool(tools):
    return list(tools) + [CREATE_NOTE_TOOL]
