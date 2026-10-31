# Recovery and Restore Runbook

## Objective
Restore the latest known-good, reviewed context bundle from an independent copy. This does not restore hidden provider memory or necessarily recreate full chat history.

## Procedure
1. Stop editing the damaged bundle.
2. Identify the latest backup with a trusted manifest.
3. Copy the encrypted archive to a clean temporary location and decrypt it using the separately stored key.
4. Verify file hashes against the trusted manifest.
5. Run the JSONL validator on restored records.
6. Review changes made after the backup and document known gaps.
7. Restore the verified copy to the working location.
8. Import only relevant approved records into the target assistant.
9. Record restore date, source backup, validation outcome, and missing data.

## Restore test checklist
- [ ] Archive can be read and decrypted.
- [ ] Manifest is available and trusted.
- [ ] Hash validation succeeds.
- [ ] JSONL parses and required fields exist.
- [ ] Sample records are readable and intelligible.
- [ ] Sensitive content is not unintentionally exposed.
- [ ] Target assistant can use selected records for a sample task.
- [ ] Missing or stale records are documented.

A successful hash check confirms file equality against the chosen manifest; it does not prove records are correct, current, complete, or safe to import.
