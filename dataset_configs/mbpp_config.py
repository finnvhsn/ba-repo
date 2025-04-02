DATASET_NAME = "mbpp"
SPLIT = "test"
PROMPT_TEMPLATE = """
You are a Python expert. Write a complete, correct Python function that solves the following task:

{task_prompt}

Requirements:
- The function MUST start with: def candidate(...)
- Do NOT include explanations, comments, or markdown formatting
- Do NOT include docstrings (no triple quotes)

Output ONLY the function code.
"""
FIELDS = {
    "task_id": "task_id",
    "text": "text",
    "solution": "code",
    "test": "test_list"
}
