"""
Generic OpenAI-compatible tool calling runner.
Works with Groq, OpenAI, or any OpenAI-compatible API.
"""

import json
import time
from typing import Any, Callable
from openai import OpenAI




class LLMRunner:
    def __init__(self, base_url: str, api_key: str, model: str):
        self.client = OpenAI(base_url=base_url, api_key=api_key)
        self.model = model

    def run(
        self,
        query: str,
        tools: list[dict],
        tool_executor: Callable[[str, dict], Any],
        system_prompt: str = "",
        max_rounds: int = 10,
        verbose: bool = False,
    ) -> dict:
        """
        Run a single query through the tool-calling loop.

        Returns:
            dict with: response, tool_calls, trace, total_input_tokens,
            total_output_tokens, latency_seconds, rounds
        """
        messages = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": query},
        ]

        all_tool_calls = []
        trace = []  # round-by-round log
        total_input_tokens = 0
        total_output_tokens = 0
        rounds = 0

        start_time = time.time()

        while rounds < max_rounds:
            rounds += 1

            response = self.client.chat.completions.create(
                model=self.model,
                messages=messages,
                tools=tools if tools else None,
                tool_choice="auto" if tools else None,
            )

            choice = response.choices[0]
            message = choice.message

            if response.usage:
                total_input_tokens += response.usage.prompt_tokens
                total_output_tokens += response.usage.completion_tokens

            round_entry = {"round": rounds, "tool_calls": []}

            # No tool calls → final response
            if not message.tool_calls:
                round_entry["final_response"] = message.content or ""
                trace.append(round_entry)
                if verbose:
                    print(f"    [Round {rounds}] LLM final response: {(message.content or '')[:200]}")
                break

            # Append assistant message with tool calls
            messages.append(message)

            # Execute each tool call
            for tool_call in message.tool_calls:
                tool_name = tool_call.function.name
                try:
                    tool_args = json.loads(tool_call.function.arguments)
                except json.JSONDecodeError:
                    tool_args = {}

                all_tool_calls.append({
                    "tool": tool_name,
                    "arguments": tool_args,
                })

                if verbose:
                    print(f"    [Round {rounds}] LLM calls: {tool_name}({json.dumps(tool_args)})")

                try:
                    result = tool_executor(tool_name, tool_args)
                    result_str = json.dumps(result, default=str) if not isinstance(result, str) else result
                except Exception as e:
                    result_str = json.dumps({"error": str(e)})

                # Summarise result for trace (avoid huge blobs)
                try:
                    result_obj = json.loads(result_str)
                    if isinstance(result_obj, list):
                        result_summary = [r.get("path", r) for r in result_obj[:10]]
                        if len(result_obj) > 10:
                            result_summary.append(f"... ({len(result_obj)} total)")
                    else:
                        result_summary = result_obj
                except Exception:
                    result_summary = result_str[:300]

                round_entry["tool_calls"].append({
                    "tool": tool_name,
                    "arguments": tool_args,
                    "result_summary": result_summary,
                })

                if verbose:
                    print(f"    [Round {rounds}] Whoosh returned: {result_summary}")

                messages.append({
                    "role": "tool",
                    "tool_call_id": tool_call.id,
                    "content": result_str,
                })

            trace.append(round_entry)

        elapsed = time.time() - start_time

        return {
            "response": message.content or "",
            "tool_calls": all_tool_calls,
            "trace": trace,
            "total_input_tokens": total_input_tokens,
            "total_output_tokens": total_output_tokens,
            "latency_seconds": round(elapsed, 3),
            "rounds": rounds,
        }
