# Source AI: Export selected context

Use this prompt in the assistant that currently holds the context. Replace the scope placeholder first. Do not request indiscriminate export of work or personal conversations.

---

Prepare a portable, reviewable context export for a different AI assistant.

**Scope:** [REPLACE WITH A SPECIFIC TOPIC OR PROJECT]

Rules:
1. Do not invent facts, dates, preferences, or decisions.
2. Separate explicit statements from inference; label uncertainty.
3. Exclude passwords, API keys, tokens, authentication data, and unnecessary sensitive information.
4. Do not export employer-confidential, customer, source-code, regulated, or restricted information unless explicitly authorized and the destination is approved.
5. Prefer concise durable context over full transcripts.
6. Preserve contradictions as separate draft records and explain the conflict.
7. Set status to draft and import_policy to manual_review for every generated record.
8. Use ISO 8601 UTC timestamps; do not fabricate unknown dates.
9. Return JSON Lines: one JSON object per line, no Markdown fences or surrounding prose.
10. Follow schemas/context-record.schema.json. Required fields: id, type, title, content, status, confidence, sensitivity, created_at, updated_at, source.

After the JSONL, if the interface permits separate text, report scope, known gaps, conflicts requiring review, and anything intentionally omitted. Do not claim this is a complete chat-history backup.
