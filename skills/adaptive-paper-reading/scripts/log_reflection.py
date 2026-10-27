#!/usr/bin/env python3
"""Record consented, short, local learning observations. No network access."""
from __future__ import annotations

import argparse
import json
import re
from datetime import datetime, timezone
from pathlib import Path
from uuid import uuid4


ROOT = Path(__file__).resolve().parents[1]
PRIVATE_LOG = ROOT / "data" / "private" / "learning.jsonl"
MAX_NOTE_LENGTH = 500

PII_PATTERNS = (
    re.compile(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b"),
    re.compile(r"\b(?:\+?\d[\d\s-]{8,}\d)\b"),
)


def validate_note(note: str) -> str:
    cleaned = note.strip()
    if not cleaned or len(cleaned) > MAX_NOTE_LENGTH:
        raise ValueError(f"Note must contain 1..{MAX_NOTE_LENGTH} characters.")
    if any(pattern.search(cleaned) for pattern in PII_PATTERNS):
        raise ValueError("Possible email address or phone number detected; redact first.")
    return cleaned


def make_event(note: str, kind: str, evidence: str, paper: str) -> dict[str, str]:
    return {
        "schema_version": "1",
        "id": str(uuid4()),
        "created_at_utc": datetime.now(timezone.utc).isoformat(),
        "kind": kind,
        "evidence": evidence,
        "paper": paper.strip()[:120],
        "observation": validate_note(note),
        "visibility": "local-private",
        "profile_promotion": "not-approved",
    }


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Preview or save one explicitly consented, private learning observation."
    )
    parser.add_argument("--note", required=True, help="Short, de-identified observation.")
    parser.add_argument(
        "--kind",
        choices=("preference", "confusion", "insight", "feedback"),
        default="insight",
    )
    parser.add_argument(
        "--evidence",
        choices=("user-explicit", "repeated-observation", "one-off"),
        default="one-off",
    )
    parser.add_argument("--paper", default="", help="Title only, not PDF contents.")
    parser.add_argument(
        "--approve-write",
        action="store_true",
        help="Write to local private JSONL only after user approval.",
    )
    args = parser.parse_args()

    try:
        event = make_event(args.note, args.kind, args.evidence, args.paper)
    except ValueError as exc:
        parser.error(str(exc))
        return

    payload = json.dumps(event, ensure_ascii=False)
    if not args.approve_write:
        print(payload)
        print("DRY RUN — add --approve-write only after the user explicitly approves.")
        return

    PRIVATE_LOG.parent.mkdir(parents=True, exist_ok=True)
    with PRIVATE_LOG.open("a", encoding="utf-8") as handle:
        handle.write(payload + "\n")
    print(f"Saved one local-private event: {PRIVATE_LOG}")
    print("Nothing was uploaded or added to the public Git repository.")


if __name__ == "__main__":
    main()
