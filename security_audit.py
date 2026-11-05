
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent
EXTENSIONS = {".py", ".json", ".csv", ".env", ".txt"}
EXCLUDED_DIRS = {".git", "__pycache__", ".venv", ".pytest_cache", ".ruff_cache"}

PATTERNS = {
    "Possible API key": r"(?i)(?:api_key|secret_key|access_token)\s*=\s*['\"][^'\"]+['\"]",
    "Email address": r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b",
    "Private key": r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----",
}

def scan():
    findings = []
    for path in ROOT.rglob("*"):
        if not path.is_file():
            continue
        if any(part in EXCLUDED_DIRS for part in path.relative_to(ROOT).parts):
            continue
        if path.name == "security_audit.py" or path.suffix not in EXTENSIONS:
            continue

        try:
            content = path.read_text(encoding="utf-8")
        except (UnicodeError, OSError):
            continue

        for label, pattern in PATTERNS.items():
            for match in re.finditer(pattern, content):
                line = content.count("\n", 0, match.start()) + 1
                findings.append((str(path.relative_to(ROOT)), line, label))

    if findings:
        for filename, line, label in findings:
            print(f"REVIEW: {filename}:{line} - {label}")
    else:
        print("No matches found for the configured patterns.")

    print(f"Total findings: {len(findings)}")

if __name__ == "__main__":
    scan()
