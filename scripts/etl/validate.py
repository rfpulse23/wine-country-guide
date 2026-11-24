"""
Validate wineries.json for missing fields and data quality issues.

Usage:
    python validate.py
"""

import json
from pathlib import Path

DATA_PATH = Path(__file__).parent.parent.parent / "data/raw/wineries.json"

REQUIRED_FIELDS = [
    "tier", "name", "region", "ava", "restrained_style_match",
    "public_tasting", "known_for", "area", "book_via",
    "drive_from_healdsburg_min", "drive_from_napa_min", "info_status"
]

VALID_TIERS = {1, 2, 3, 4}
VALID_TASTING = {"appointment", "walk_in", "members_only", "no_public"}
VALID_STATUS = {"verified", "partly_verified", "last_known"}

def validate():
    with open(DATA_PATH) as f:
        wineries = json.load(f)

    errors = []
    warnings = []

    names = [w["name"] for w in wineries]
    dupes = [n for n in names if names.count(n) > 1]
    if dupes:
        errors.append(f"Duplicate names: {set(dupes)}")

    for w in wineries:
        name = w.get("name", "UNKNOWN")

        for field in REQUIRED_FIELDS:
            if field not in w or w[field] is None:
                errors.append(f"[{name}] Missing required field: {field}")

        if w.get("tier") not in VALID_TIERS:
            errors.append(f"[{name}] Invalid tier: {w.get('tier')}")

        if w.get("public_tasting") not in VALID_TASTING:
            errors.append(f"[{name}] Invalid public_tasting: {w.get('public_tasting')}")

        if w.get("info_status") not in VALID_STATUS:
            errors.append(f"[{name}] Invalid info_status: {w.get('info_status')}")

        if w.get("restrained_style_match") not in {1, 2, 3}:
            errors.append(f"[{name}] Invalid restrained_style_match: {w.get('restrained_style_match')}")

        if not w.get("ava"):
            warnings.append(f"[{name}] Empty AVA")

        if not w.get("price_pp") and w.get("public_tasting") == "appointment":
            warnings.append(f"[{name}] Bookable but no price listed")

    print(f"\n{'='*50}")
    print(f"Validated {len(wineries)} wineries")
    print(f"{'='*50}")

    if errors:
        print(f"\n❌ ERRORS ({len(errors)}):")
        for e in errors:
            print(f"  {e}")
    else:
        print("\n✅ No errors found")

    if warnings:
        print(f"\n⚠️  WARNINGS ({len(warnings)}):")
        for w in warnings:
            print(f"  {w}")
    else:
        print("✅ No warnings")

    print()
    return len(errors) == 0

if __name__ == "__main__":
    validate()
