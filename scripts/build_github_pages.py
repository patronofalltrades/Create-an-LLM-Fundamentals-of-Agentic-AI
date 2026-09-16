#!/usr/bin/env python3
"""Build the minimal public artifact for the GitHub Pages deployment."""
from __future__ import annotations

import argparse
import shutil
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PUBLIC_FILES = {"embedding-viewer.html": "index.html", "tokens.css": "tokens.css", "redesign.css": "redesign.css"}


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    output = (ROOT / args.output).resolve() if not args.output.is_absolute() else args.output.resolve()
    try:
        output.relative_to(ROOT)
    except ValueError as error:
        raise SystemExit("Output must be inside the repository.") from error
    if output == ROOT:
        raise SystemExit("Output cannot be the repository root.")
    if output.exists():
        shutil.rmtree(output)
    output.mkdir(parents=True)
    for source_name, target_name in PUBLIC_FILES.items():
        source = ROOT / source_name
        if not source.is_file():
            raise SystemExit(f"Missing required file: {source_name}")
        shutil.copy2(source, output / target_name)
    (output / ".nojekyll").touch()
    print(f"Built GitHub Pages artifact in {output}")


if __name__ == "__main__":
    main()
