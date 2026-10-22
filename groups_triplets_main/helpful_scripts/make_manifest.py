"""Create manifest.json for the image folder used by index.html.

Usage (from groups_triplets_main/):
    python3 make_manifest.py              # uses animals2/
    python3 make_manifest.py STIMULI/foo  # or any other folder
"""
import json
import sys
from pathlib import Path

EXTENSIONS = {".png", ".jpg", ".jpeg", ".gif", ".webp"}

folder = Path(sys.argv[1] if len(sys.argv) > 1 else "animals2")
images = sorted(p.name for p in folder.iterdir() if p.suffix.lower() in EXTENSIONS)

with open(folder / "manifest.json", "w") as f:
    json.dump({"images": images}, f, indent=2)

print(f"Wrote {len(images)} images to {folder / 'manifest.json'}")
