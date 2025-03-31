DATASET_NAME = "humaneval"
SPLIT = "test"
PROMPT_TEMPLATE = """
ONLY return valid Python code.
Do NOT use code blocks like ``` or markdown.
Do NOT include docstrings (triple quotes).
Your response must start with: def function_name(...):

You are an expert Python programmer. Your task is to write a valid and complete Python function that solves the following task:

{task_prompt}

Remember:
- Do NOT explain anything.
- Do NOT include comments.
- Do NOT include anything except the Python function code.
"""
FIELDS = {
    "task_id": "task_id",
    "text": "prompt",
    "solution": "canonical_solution",
    "test": "test"
}
