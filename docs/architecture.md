# Portable AI Context Architecture

## Purpose

A provider-neutral, human-reviewable method for moving useful context between AI assistants without depending on hidden model memory or a provider-specific export format.

## Components

1. Source assistant — summarizes selected, permitted context.
2. Export prompt — requests structured records and calls out uncertainty.
3. Import inbox — stages raw output for review; it is not trusted automatically.
4. Validation — checks JSONL syntax and required fields.
5. Canonical context bundle — reviewed records stored as JSONL.
6. Target import prompt — sends a relevant subset to the receiving assistant.
7. Change and conflict review — records updates and contradictions.
8. SHA-256 manifest — inventories files for integrity checks.
9. Offline recovery copy — encrypted archive stored independently of this repository.

## Data flow

~~~mermaid
flowchart LR
  A[Source assistant] --> B[Export prompt]
  B --> C[Import inbox]
  C --> D[Human privacy and accuracy review]
  D --> E[Local validation]
  E --> F[Canonical JSONL bundle]
  F --> G[SHA-256 manifest]
  F --> H[Target import prompt]
  H --> I[Target assistant]
  F --> J[Encrypted offline archive]
~~~

## Record types

Use the type field to classify records: fact, preference, decision, project, procedure, open_question, relationship, event, or skill.

Do not convert speculation into fact. Label inference explicitly and use low or unknown confidence where appropriate.

## Record lifecycle

draft -> reviewed -> approved -> superseded or archived

Imported records start as draft. A human reviews accuracy, relevance, sensitivity, and freshness before approving. Contradictions become review items; they are not silently overwritten.

## Versioning

- Give every record a stable identifier; UUID is recommended.
- Increment version when a record changes materially.
- Keep created_at and updated_at in ISO 8601 UTC format.
- Mark replaced records as superseded and set supersedes to the old record ID.
- Use Git commits for architecture and synthetic examples only, not sensitive real context.
- Store real context in a separate encrypted local bundle.

## Boundaries

This architecture stores portable summaries and selected context. It is not a full-fidelity backup of provider chat history, hidden system prompts, model weights, or internal memory.
