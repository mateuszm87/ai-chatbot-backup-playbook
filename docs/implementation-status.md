# Implementation Status

This repository is an architecture starter kit, not a production synchronization service.

## Included
- Provider-neutral context-record schema.
- Synthetic JSONL examples.
- Source export and target import prompts.
- Manual synchronization and recovery procedures.
- Python standard-library JSONL validator.
- Python standard-library SHA-256 manifest generator.
- Security and privacy guidance.

## Not included
- Direct ChatGPT or Microsoft Copilot integration.
- Automatic full-history export or bidirectional synchronization.
- Conflict-resolution UI or database.
- Encryption/decryption implementation or key management.
- Scheduled backups or monitoring.
- Automated end-to-end restore tests.
- Guarantees that the target assistant will retain context permanently.

## Production readiness checklist
- [ ] Tests cover valid and invalid records.
- [ ] Manifest verification is implemented separately from generation.
- [ ] Encryption uses a vetted tool/library and keys are stored separately.
- [ ] Restore tests run in a clean environment.
- [ ] Provider adapters document permissions and data boundaries.
- [ ] Work/personal transfer is controlled by explicit policy.
- [ ] Logs exclude secrets and unnecessary personal data.
- [ ] Retention and recovery-point objectives are defined.
- [ ] Security review is completed before sensitive data is used.
