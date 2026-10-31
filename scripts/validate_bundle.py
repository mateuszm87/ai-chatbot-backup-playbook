#!/usr/bin/env python3
"""Basic JSONL validator using only Python's standard library.

Usage: python scripts/validate_bundle.py path/to/records.jsonl
This checks required fields and common enumerations, not the full JSON Schema.
"""
import json
import sys
from pathlib import Path

REQUIRED = {"id", "type", "title", "content", "status", "confidence", "sensitivity", "created_at", "updated_at", "source"}
TYPES = {"fact", "preference", "decision", "project", "procedure", "open_question", "relationship", "event", "skill"}
STATUSES = {"draft", "reviewed", "approved", "superseded", "archived"}
CONFIDENCE = {"high", "medium", "low", "unknown"}
SENSITIVITY = {"public", "personal", "confidential", "restricted"}

def main():
    if len(sys.argv) != 2:
        print("Usage: python scripts/validate_bundle.py path/to/records.jsonl", file=sys.stderr)
        return 2
    path = Path(sys.argv[1])
    if not path.is_file():
        print(f"ERROR: file not found: {path}", file=sys.stderr)
        return 2
    errors, count, ids = [], 0, set()
    with path.open("r", encoding="utf-8") as stream:
        for line_no, line in enumerate(stream, 1):
            if not line.strip():
                continue
            count += 1
            try:
                record = json.loads(line)
            except json.JSONDecodeError as exc:
                errors.append(f"line {line_no}: invalid JSON: {exc.msg}")
                continue
            if not isinstance(record, dict):
                errors.append(f"line {line_no}: record must be an object")
                continue
            for key in sorted(REQUIRED - record.keys()):
                errors.append(f"line {line_no}: missing field {key}")
            for key in ("id", "title", "content", "created_at", "updated_at"):
                if key in record and (not isinstance(record[key], str) or not record[key].strip()):
                    errors.append(f"line {line_no}: {key} must be a non-empty string")
            for key, allowed in (("type", TYPES), ("status", STATUSES), ("confidence", CONFIDENCE), ("sensitivity", SENSITIVITY)):
                if key in record and record[key] not in allowed:
                    errors.append(f"line {line_no}: invalid {key}: {record[key]!r}")
            source = record.get("source")
            if not isinstance(source, dict) or not isinstance(source.get("system"), str) or not isinstance(source.get("kind"), str):
                errors.append(f"line {line_no}: source must contain string fields system and kind")
            record_id = record.get("id")
            if isinstance(record_id, str):
                if record_id in ids:
                    errors.append(f"line {line_no}: duplicate id {record_id}")
                ids.add(record_id)
    if count == 0:
        errors.append("bundle contains no records")
    if errors:
        print(f"FAILED: {len(errors)} issue(s) in {path}")
        print("\n".join("- " + error for error in errors))
        return 1
    print(f"OK: {count} record(s) validated in {path}")
    print("Note: basic checks only; use a JSON Schema validator for full schema conformance.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
