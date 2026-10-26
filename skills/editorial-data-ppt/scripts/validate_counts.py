#!/usr/bin/env python3
"""Validate chart claims before building/editing a Figma research slide.

Input is an ANONYMIZED JSON spec, not a project's original workbook.
Usage: python scripts/validate_counts.py path/to/chart-claims.json

Example JSON:
{
  "case_count": 100,
  "exclusive_categories": {"A": 40, "B": 60},
  "first_class_memberships": {"C1": 60, "C2": 48},
  "unclassified_cases": 0,
  "overlay_counts": {"internal_ecosystem": 11},
  "tag_rates": [{"class_case_count": 60, "tag_case_count": 25}]
}
"""
import json
import math
import sys
from pathlib import Path


def integer(value, name):
    if isinstance(value, bool) or not isinstance(value, int) or value < 0:
        raise ValueError(f"{name}: expected nonnegative integer, got {value!r}")
    return value


def validate(doc):
    n = integer(doc["case_count"], "case_count")
    if n == 0:
        raise ValueError("case_count must be positive")
    counts = doc.get("exclusive_categories")
    if counts is not None:
        vals = [integer(v, f"exclusive_categories/{k}") for k, v in counts.items()]
        if sum(vals) != n:
            raise ValueError(f"exclusive counts sum to {sum(vals)}, expected {n}")
    memberships = doc.get("first_class_memberships")
    missing = integer(doc.get("unclassified_cases", 0), "unclassified_cases")
    if missing > n:
        raise ValueError("unclassified_cases exceeds case_count")
    if memberships is not None:
        vals = [integer(v, f"first_class_memberships/{k}") for k, v in memberships.items()]
        if sum(vals) < n - missing:
            raise ValueError("multi-select membership counts cannot cover classified cases")
        if any(v > n for v in vals):
            raise ValueError("a class has more distinct cases than the entire collection")
    for k, v in doc.get("overlay_counts", {}).items():
        if integer(v, f"overlay_counts/{k}") > n:
            raise ValueError("overlay count exceeds case_count")
    for i, item in enumerate(doc.get("tag_rates", [])):
        parent = integer(item["class_case_count"], f"tag_rates/{i}/class_case_count")
        tag = integer(item["tag_case_count"], f"tag_rates/{i}/tag_case_count")
        if tag > parent or parent == 0:
            raise ValueError("tag count exceeds class case count or class size is zero")
        if "display_percent" in item:
            actual = round(tag / parent * 100, 1)
            shown = float(item["display_percent"])
            if not math.isclose(shown, actual, abs_tol=0.06):
                raise ValueError(f"tag percentage mismatch: {shown} versus {actual}")
    return {"case_count": n, "exclusive_sum": sum(counts.values()) if counts is not None else None,
            "membership_sum": sum(memberships.values()) if memberships is not None else None,
            "overlay_counts": doc.get("overlay_counts", {}), "valid": True}


if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise SystemExit("Usage: validate_counts.py claims.json")
    result = validate(json.loads(Path(sys.argv[1]).read_text(encoding="utf-8")))
    print(json.dumps(result, ensure_ascii=False, indent=2))
