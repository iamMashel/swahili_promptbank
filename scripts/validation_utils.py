import os
import json

# Configuration
ROOT_DIR = "../prompts"
REQUIRED_FIELDS = ["task", "language", "prompt", "expected_output"]
ALLOWED_TASKS = [
    "instruction-following",
    "classification",
    "summarization",
    "conversational"
]

def validate_prompt(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        try:
            data = json.load(f)
        except json.JSONDecodeError as e:
            return f"[ERROR] Invalid JSON in {file_path}: {e}"

    # Check required fields
    for field in REQUIRED_FIELDS:
        if field not in data:
            return f"[ERROR] Missing field '{field}' in {file_path}"

    # Validate task type
    if data["task"] not in ALLOWED_TASKS:
        return f"[ERROR] Invalid task '{data['task']}' in {file_path}"

    # Validate language
    if data["language"].lower() != "swahili":
        return f"[ERROR] Expected language to be 'Swahili' in {file_path}, got '{data['language']}'"

    # Check prompt and output are non-empty
    if not data["prompt"].strip():
        return f"[ERROR] Empty 'prompt' field in {file_path}"
    if not data["expected_output"].strip():
        return f"[ERROR] Empty 'expected_output' field in {file_path}"

    return f"[OK] {file_path}"

def validate_all_prompts():
    print("🔍 Validating all prompt files...\n")

    for subdir, _, files in os.walk(ROOT_DIR):
        for file in files:
            if file.endswith(".json"):
                file_path = os.path.join(subdir, file)
                result = validate_prompt(file_path)
                print(result)

if __name__ == "__main__":
    validate_all_prompts()
