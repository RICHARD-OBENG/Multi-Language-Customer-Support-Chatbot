import os
import logging
from pathlib import Path

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')



project_name = "Multi-Language Customer Support Chatbot"


list_of_file = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/config/settings.py",
    f"src/{project_name}/config/prompt.yaml",
    f"src/{project_name}/core/reasoning.py",
    f"src/{project_name}/core/planner.py",
    f"src/{project_name}/core/executor.py",
    f"src/{project_name}/llm/client.py",
    f"src/{project_name}/llm/prompt.py",
    f"src/{project_name}/llm/response_parser.py",
    f"src/{project_name}/rules/rules_engine.py",
    f"src/{project_name}/rules/constraints.py",
    f"src/{project_name}/tools/calculator.py",
    f"src/{project_name}/tools/search.py",
    f"src/{project_name}/tools/validators.py",
    f"src/{project_name}/memory/short_term.py",
    f"src/{project_name}/memory/long_term.py",
    f"src/{project_name}/api/main.py",
    f"src/{project_name}/api/schemas.py",
    f"src/{project_name}/utils/logger.py",
    f"src/{project_name}/utils/error_handler.py",
    "test/test_reasoning.py",
    "test/test_rules.py",
    "test/test_llm.py",
    "deployment/Dockerfile",
    "deployment/run.sh",
    "docs/system_design.md",
    "docs/reasoning_flow.md",
    "docs/limitations.md",
    "requirements.txt",
    "setup.py"


]

for filepath in list_of_file:
    filepath = Path(filepath)
    filedir = filepath.parent
    filename = filepath.name

    # create directory if it doesn't exist (skip current dir)
    if filedir != Path('.'):
        filedir.mkdir(parents=True, exist_ok=True)
        logging.info(f"Created directory: {filedir} for the file: {filename}")

    # create the file if it doesn't exist or is empty
    if (not filepath.exists()) or (filepath.stat().st_size == 0):
        filepath.touch(exist_ok=True)
        logging.info(f"Created empty file: {filepath}")
    else:
        logging.info(f"File already exists: {filepath}")