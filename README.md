# SWE 580 Term Project — Tool Granularity in Personal Knowledge Retrieval

This repository contains my submission for the SWE 580 term project. The instructor provides the evaluation harness, the Whoosh search backend, the test queries, and the 100 note vault. My contribution is the four edited interface files (two system prompts and two tool description JSONs), and the bonus note creation tool.

Author: Yusuf İzzet Murat


## What is being compared

The project asks how tool granularity affects an LLM agent's ability to search a personal knowledge vault. Configuration A exposes four rich tools whose central piece is one `search_notes` call that takes content, tags, and a date range together. Configuration B exposes nine narrow tools, one per filter or graph direction. Both run on the same backend, the same 100 notes, and the same 25 test queries. The only thing that differs is the tool surface and the system prompt that explains it.


## Setup

```bash
python3 -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

The evaluator and runner use the OpenAI Python SDK against any OpenAI compatible endpoint. The main runs in this submission go through OpenRouter. Put your API key in a `.env` file as `LLM_API_KEY=...`.


## How to reproduce the runs

Baseline pass (uses the prompts and tool descriptions exactly as shipped, so this needs to be done before any edits, or by restoring them from git):

```bash
export $(cat .env | xargs)
python evaluator.py --config both --model google/gemini-2.5-flash
```

Improved pass (uses my rewritten prompts and tool descriptions in this repo state):

```bash
python evaluator.py --config both --model google/gemini-2.5-flash
```

Multi model bonus runs (same evaluation, different model, output into a subdir to keep things tidy):

```bash
python evaluator.py --config both --model anthropic/claude-sonnet-4.5      --output-dir results/claude-sonnet
python evaluator.py --config both --model deepseek/deepseek-chat-v3.1      --output-dir results/deepseek-v3
python evaluator.py --config both --model openai/gpt-4o-mini               --output-dir results/gpt-4o-mini
python evaluator.py --config both --model meta-llama/llama-3.1-8b-instruct --output-dir results/llama-8b
```

Note creation bonus, running the synthesis demo on Gemini:

```bash
python synthesis_demo.py --config a --model google/gemini-2.5-flash
python synthesis_demo.py --config b --model google/gemini-2.5-flash
```

Build the consolidated summary table from everything in `results/`:

```bash
python build_summary.py
```


## File index

Files I edited:

| File | What it is |
|---|---|
| `config_a_prompt.txt` | System prompt for Configuration A |
| `config_b_prompt.txt` | System prompt for Configuration B |
| `config_a_tools.json` | Tool descriptions for Configuration A's four tools |
| `config_b_tools.json` | Tool descriptions for Configuration B's nine tools |

Files I added for the bonus:

| File | What it is |
|---|---|
| `note_creation.py` | The `create_note` tool and an executor wrapper that plugs it into either configuration without touching the existing infrastructure |
| `synthesis_demo.py` | A small runner that exercises `create_note` on the synthesis queries and checks the created files |
| `synthesis_queries.json` | Three synthesis queries with expected paths, expected wiki links, and expected tags |
| `build_summary.py` | Walks `results/` and produces a single comparison table across baseline, improved Gemini, and all bonus model runs |

Files I did not change (these are the infrastructure):

`evaluator.py`, `executors.py`, `search_backend.py`, `llm_runner.py`, `test_queries.json`, the `vault/` directory.


## How the results directory is organized

```
results/
├── comparison_baseline.json            main run, default prompt
├── config_a_baseline.json
├── config_b_baseline.json
├── comparison_improved.json            main run, my prompts
├── config_a_improved.json
├── config_b_improved.json
├── final_summary.json                  consolidated table built by build_summary.py
├── claude-sonnet/                      bonus model run
├── deepseek-v3/                        bonus model run
├── gpt-4o-mini/                        bonus model run
├── llama-8b/                           bonus model run
└── synthesis/                          note creation bonus
    ├── synthesis_a_*.json              per query verification on Config A
    ├── synthesis_b_*.json              per query verification on Config B
    └── notes/                          the markdown notes the model created
```

The synthesis demo writes its new notes into `results/synthesis/notes/` rather than into `vault/`, so the main evaluation always reads the same 100 notes.


## Results

Headline numbers from the runs in `results/` (25 queries each, A = 4 coarse tools, B = 9 fine tools):

| Run | Success A | Success B | F1 A | F1 B | Tokens A | Tokens B |
|---|---|---|---|---|---|---|
| Baseline (shipped prompt) | 0.44 | 0.32 | 0.48 | 0.36 | 821 | 1,163 |
| Improved prompt, Gemini 2.5 Flash | 0.84 | 0.76 | 0.89 | 0.89 | 2,682 | 3,124 |
| Improved prompt, Claude Sonnet 4.5 | 0.84 | 0.72 | 0.90 | 0.89 | 4,909 | 7,886 |
| Improved prompt, DeepSeek V3.1 | 0.72 | 0.64 | 0.87 | 0.86 | 9,672 | 14,141 |
| Improved prompt, GPT 4o mini | 0.72 | 0.68 | 0.84 | 0.80 | 3,739 | 4,504 |
| Improved prompt, Llama 3.1 8B | 0.36 | 0.24 | 0.52 | 0.35 | 5,044 | 6,914 |

Per category, on Gemini 2.5 Flash with the improved prompts:

| Category | Baseline A | Baseline B | Improved A | Improved B |
|---|---|---|---|---|
| Simple lookup | 0.00 | 0.00 | 1.00 | 1.00 |
| Tag search | 1.00 | 1.00 | 1.00 | 1.00 |
| Temporal | 0.67 | 0.67 | 1.00 | 1.00 |
| Content search | 0.50 | 0.00 | 1.00 | 1.00 |
| Multi filter | 0.67 | 0.44 | 0.78 | 0.56 |
| Graph traversal | 0.00 | 0.00 | 0.71 | 0.71 |

Three things stand out. First, the rewritten prompts and tool descriptions roughly double success on both configurations, and the biggest gains come from categories the baseline failed on entirely (simple lookup, content search, graph traversal). Second, Configuration A wins on every one of the five models tested, with the gap ranging from four points on GPT 4o mini to twelve on Claude Sonnet, so the coarse-grained design is not a Gemini quirk. Third, the synthesis bonus passes three out of three on both configurations on Gemini, with the created notes containing all expected wiki links and tags.