# AI Chatbot Backup Playbook

A portable, model-agnostic reference architecture for preserving AI context, transferring it between assistants, and recovering from context loss. This repository includes a reusable context data model, import/export prompts, JSON Schemas, synthetic examples, and local validation tools.

> **Status:** architecture starter kit / manual-sync MVP. This is not a live integration with ChatGPT, Microsoft Copilot, or any provider. It does not automatically export chat histories or guarantee that an assistant will retain imported fields.

## Start here

- [Architecture](docs/architecture.md)
- [Context model reference](docs/context-model.md)
- [Context record schema](schemas/context-record.schema.json)
- [Synthetic JSONL example](examples/context-records.jsonl)
- [Export prompt for the source AI](templates/export-context-prompt.md)
- [Import prompt for the target AI](templates/import-context-prompt.md)
- [Manual sync runbook](docs/manual-sync-workflow.md)
- [Security and privacy](docs/security.md)
- [Recovery runbook](docs/recovery.md)
- [Implementation status and limitations](docs/implementation-status.md)

## Quick start

1. Clone or download this repository.
2. Read the architecture and confirm what data you are permitted to transfer.
3. Use the export prompt in the source assistant with a narrow topic scope.
4. Save the result as UTF-8 JSON Lines (one JSON object per line).
5. Review records for accuracy, freshness, sensitivity, secrets, and employer restrictions.
6. Validate the file:

   ~~~bash
   python scripts/validate_bundle.py examples/context-records.jsonl
   ~~~

7. For your own local bundle, create a SHA-256 inventory:

   ~~~bash
   python scripts/build_manifest.py ./my-context-bundle ./MANIFEST_SHA256.json
   ~~~

8. Import only reviewed records using the target import prompt.
9. Store an encrypted offline copy and periodically test restoration.

## Layout

- docs/ — architecture, manual workflow, security, recovery, status
- schemas/ — portable context record and manifest schemas
- templates/ — export/import prompts and record template
- examples/ — synthetic records only; no real personal or work data
- scripts/ — Python standard-library validation and hash inventory tools

## Design principles

- Provider-neutral records, independent of hidden model memory.
- Separate facts, preferences, decisions, projects, procedures, and open questions.
- Preserve provenance, confidence, timestamps, and sensitivity.
- Treat imported content as untrusted until reviewed.
- Keep work and personal data separate; employer policy takes precedence.
- Maintain version history and an encrypted offline copy independent of GitHub.

## Limitations and safety

This is a manual export/import workflow, not a bidirectional sync engine. A hash manifest detects file changes only if the expected manifest is trusted; it does not encrypt data or prove that the source is truthful. Do not commit real private context, secrets, private chat exports, or employer-confidential data to this public repository. Schema-valid data can still be false, stale, sensitive, or irrelevant. Human review is required.

See [LICENSE](LICENSE).
