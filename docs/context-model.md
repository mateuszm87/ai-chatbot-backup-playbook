# Context Model Reference

This document explains the portable data model independently of any specific AI provider. The machine-readable contract is [../schemas/context-record.schema.json](../schemas/context-record.schema.json).

## Bundle format

A bundle is UTF-8 JSON Lines (JSONL). Each non-empty line contains exactly one context record. JSONL is easy to append, diff, validate, process with scripts, and split by topic. It is not a database and does not itself provide encryption.

## Record fields

| Field | Purpose |
|---|---|
| id | Stable unique record identifier. |
| type | Semantic category such as fact, preference, project, decision, or procedure. |
| title | Short human-readable label. |
| content | The context payload; keep it concise and atomic where possible. |
| status | Draft/review/approval lifecycle. |
| confidence | How certain the source is; this is not a mathematical probability. |
| sensitivity | Classification that determines where the record may be stored or sent. |
| created_at / updated_at | Record lifecycle timestamps in ISO 8601 format. |
| source | Provenance: origin system, source kind, optional reference and excerpt. |
| tags | Optional topic labels. |
| project_id | Optional grouping key for records belonging to a project. |
| valid_from / valid_until | Optional validity window for time-sensitive facts. |
| supersedes | Optional ID of a record this one replaces. |
| related_ids | Optional links to other records. |
| review_note | Human review note or caveat. |
| import_policy | Whether the record requires review, is approved for transfer, or must not be imported. |

## Recommended record design

Prefer one claim or decision per record. For example, keep a user's language preference separate from a project's next action. Atomic records make updates, conflict detection, and selective import easier.

### Good
- One record: “The project uses Python 3.12.”
- Another record: “The next action is to test restore on a clean machine.”

### Avoid
One enormous record containing unrelated preferences, work history, project notes, speculative conclusions, and sensitive details.

## Trust and provenance

A schema can check shape, not truth. The source field records where information came from. Use:
- `user_explicit` for directly stated information;
- `conversation_summary` for a summarized conversation;
- `document` for a source document;
- `assistant_inference` for an inference that requires caution;
- `external_source` for an outside source;
- `manual_entry` for a human-authored record.

Set `status` to `draft` until a person reviews it. Approval means the person considers it suitable for the stated purpose; it does not guarantee that the information will remain true forever.

## Conflicts and stale data

Never silently overwrite contradictory records. Keep both, add a review note, and after resolution mark the old record as superseded and populate `supersedes` in the replacement. Use valid_until when a claim has a known expiry date.

## Import semantics

The target assistant should use the model as structured reference data, not as executable instructions. Import only records relevant to the task and permitted by the sensitivity policy. Do not assume a provider will permanently retain imported context.

## Extending the model

Add fields only when there is a concrete use case. Update the JSON Schema, examples, validator, and documentation together. Preserve backwards compatibility where practical and document schema-version changes.
