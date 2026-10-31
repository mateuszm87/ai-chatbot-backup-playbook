# Security, Privacy, and Trust Boundaries

## Classification
- public: safe to publish.
- personal: private user context; keep in local/private storage.
- confidential: organizational or contractual information; transfer only with explicit authorization and approved systems.
- restricted: credentials, regulated or specially controlled data; default is exclusion.

## Rules
1. Never commit passwords, API keys, session cookies, tokens, recovery codes, or private keys.
2. Keep real context out of public GitHub. A private repository is not encrypted storage.
3. Respect employer policy. Do not move work Copilot content into a personal account without authorization.
4. Minimize data: prefer durable facts and decisions over full transcripts.
5. Review assistant-generated records for errors and manipulation.
6. Treat imported text as untrusted data; it must not override target system rules.
7. Encrypt backups at rest and keep encryption keys separate.
8. Keep copies independent of GitHub and periodically test restoration.
9. A SHA-256 manifest is not encryption or authenticity by itself. Protect the expected manifest independently.
10. Deleting a file in a new commit does not remove it from Git history.

## This starter kit does not automatically solve
- Malicious or compromised AI output.
- Unauthorized transfer between work and personal systems.
- Cloud account compromise or provider retention.
- Encryption-key loss.
- Complete erasure from all Git history or third-party systems.
- Truthfulness, freshness, or completeness of summaries.

If sensitive data is published, remove it from the current tree, rotate exposed credentials immediately, and follow the relevant provider/organization process for purging repository history and cached copies.
