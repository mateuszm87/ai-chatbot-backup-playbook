#!/usr/bin/env python3
"""Create a SHA-256 inventory. Standard library only.

Usage: python scripts/build_manifest.py BUNDLE_DIR MANIFEST_PATH
Keep the manifest outside the directory being hashed to avoid self-reference.
"""
import hashlib
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

def main():
    if len(sys.argv) != 3:
        print("Usage: python scripts/build_manifest.py BUNDLE_DIR MANIFEST_PATH", file=sys.stderr)
        return 2
    root, out = Path(sys.argv[1]).resolve(), Path(sys.argv[2]).resolve()
    if not root.is_dir():
        print(f"ERROR: bundle directory not found: {root}", file=sys.stderr)
        return 2
    if out == root or root in out.parents:
        print("ERROR: manifest must be outside the directory being hashed", file=sys.stderr)
        return 2
    files = []
    for path in sorted(root.rglob("*")):
        if not path.is_file():
            continue
        digest, size = hashlib.sha256(), 0
        with path.open("rb") as stream:
            for chunk in iter(lambda: stream.read(1024 * 1024), b""):
                size += len(chunk)
                digest.update(chunk)
        files.append({"path": path.relative_to(root).as_posix(), "sha256": digest.hexdigest(), "size_bytes": size})
    manifest = {"manifest_version": "1.0", "created_at": datetime.now(timezone.utc).isoformat(timespec="seconds"), "algorithm": "SHA-256", "files": files}
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    print(f"Wrote {len(files)} file hash(es) to {out}")
    print("Protect this manifest independently; a replaced manifest cannot authenticate itself.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
