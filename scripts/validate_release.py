#!/usr/bin/env python3
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TOKENS = ["TODO_USER","[GITHUB_URL]","[RELEASE_TAG]","[DOI]","[DATA_DOI]","[CODE_DOI]","[CHOOSE_LICENSE]"]

hits = []
for path in ROOT.rglob("*"):
    if not path.is_file():
        continue
    if path.suffix.lower() not in {".md",".yaml",".yml",".csv",".json",".cff",".txt"} and path.name != "CITATION.cff":
        continue
    try:
        text = path.read_text(encoding="utf-8")
    except Exception:
        continue
    for token in TOKENS:
        if token in text:
            hits.append((str(path.relative_to(ROOT)), token))

if hits:
    print("Release is NOT complete. Remaining placeholders:")
    for p, token in hits:
        print(f" - {p}: {token}")
    raise SystemExit(1)

print("No known release placeholders remain.")
