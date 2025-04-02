DATASET_NAME = "humaneval"
SPLIT = "test"
PROMPT_TEMPLATE = """
You are a Python expert. Write a complete and correct Python function that solves the following task:

{task_prompt}

Requirements:
- The function MUST start with: def(...) or def candidate(...)
- Do NOT include any Markdown formatting (e.g., triple backticks ```), explanations, or comments
- Do NOT include docstrings (no triple quotes)

Output only the function code.
"""

FIELDS = {
    "task_id": "task_id",
    "text": "prompt",
    "solution": "canonical_solution",
    "test": "test"
}
