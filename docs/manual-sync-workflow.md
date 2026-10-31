# Manual Context Synchronization Runbook

## Export
1. Choose the exact topic or project.
2. Confirm transfer is permitted.
3. Use templates/export-context-prompt.md in the source assistant.
4. Save the JSONL response to a local import inbox.
5. Review every record for accuracy, freshness, secrets, sensitive data, and policy restrictions.

## Validate and approve
1. Run: python scripts/validate_bundle.py path/to/records.jsonl
2. Correct invalid JSON and missing fields.
3. Mark records reviewed, then approved only after human review.
4. Set import_policy to approved_for_import only for records safe and useful to transfer.
5. Resolve conflicts explicitly; use supersedes rather than silently deleting history.

## Import
1. Select only approved records.
2. Use templates/import-context-prompt.md in the target assistant.
3. Compare the target summary with the source records.
4. Correct misunderstandings before consequential use.

## Preserve
1. Keep canonical JSONL files locally.
2. Run: python scripts/build_manifest.py BUNDLE_DIR MANIFEST_PATH
3. Encrypt the archive with a reputable local encryption tool; store the key separately.
4. Keep an independent offline copy.
5. Periodically restore into a temporary directory and validate again.

## Suggested cadence
- After major project decisions: update relevant records.
- Weekly for active projects: review next steps and open questions.
- Monthly: create and verify an encrypted offline copy.

## Failure cases
- Bad export: quarantine it; do not overwrite approved records.
- Conflicting facts: preserve both until a human resolves the conflict.
- Hash mismatch: treat the file as changed or corrupted and restore a known-good copy.
- Target assistant does not retain context: re-import the portable bundle; do not assume persistent memory.
