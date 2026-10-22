"""Resize every image in a folder to 1/3 of its original size.

Originals are left untouched; resized copies go to a new folder.

Usage (from groups_triplets_main/):
    python3 resize_images.py STIMULI              # writes to STIMULI_resized/
    python3 resize_images.py STIMULI my_output    # writes to my_output/

Requires Pillow:  pip3 install Pillow
"""
import sys
from pathlib import Path

from PIL import Image

EXTENSIONS = {".png", ".jpg", ".jpeg", ".gif", ".webp"}
SCALE = 1 / 3

src = Path(sys.argv[1])
dst = Path(sys.argv[2]) if len(sys.argv) > 2 else src.with_name(src.name + "_resized")
dst.mkdir(exist_ok=True)

count = 0
for path in sorted(src.iterdir()):
    if path.suffix.lower() not in EXTENSIONS:
        continue
    with Image.open(path) as img:
        new_size = (max(1, round(img.width * SCALE)), max(1, round(img.height * SCALE)))
        img.resize(new_size, Image.LANCZOS).save(dst / path.name)
    count += 1

print(f"Resized {count} images from {src}/ to {dst}/")
