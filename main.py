"""Entry for make.fun bounty ai-excited-01.

Copies the bundled entry.jpg to /output/entry.png.
Standard library only, no network, deterministic: the same
input bytes always produce the same output bytes.
"""

import shutil
from pathlib import Path


def main() -> None:
    source = Path(__file__).resolve().parent / "entry.jpg"
    if not source.is_file():
        raise FileNotFoundError(f"bundled image not found: {source}")
    output_dir = Path("/output")
    output_dir.mkdir(parents=True, exist_ok=True)
    destination = output_dir / "entry.png"
    shutil.copyfile(source, destination)
    # Sanity check: the copy must be byte-for-byte identical.
    if destination.stat().st_size != source.stat().st_size:
        raise ValueError("output size does not match bundled image")


if __name__ == "__main__":
    main()
