DATASET_NAME = "mbpp"
SPLIT = "test"
PROMPT_TEMPLATE = """
You are a Python expert. Your task is to implement a Python function that solves the task below.

{text}

Instructions:
- Write only valid Python code.
- Your output must start immediately with: def ...
- Do not include any markdown, comments, or explanations.
- Do not include any docstrings inside the function.
- Do not include "```".
- Return only the function implementation. Nothing else.
"""
FIELDS = {
    "task_id": "task_id",
    "text": "text",
    "solution": "code",
    "test": "test_list"
}
