#!/usr/bin/env python3
"""Render the checkpoint-backed embedding evidence GIF without dependencies."""
from __future__ import annotations

import argparse
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path
from urllib.parse import urlencode


ROOT = Path(__file__).resolve().parents[1]
VIEWER = ROOT / "embedding-viewer.html"
DEFAULT_OUTPUT = ROOT / "docs/assets/embedding-space-training.gif"
CHROME_CANDIDATES = (
    Path("/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"),
    Path("/Applications/Chromium.app/Contents/MacOS/Chromium"),
)
FPS = 10
VIEWPORT = "1280,720"


def command_exists(name: str) -> str:
    value = shutil.which(name)
    if not value:
        raise RuntimeError(f"Required command not found: {name}")
    return value


def chrome_path() -> str:
    for candidate in CHROME_CANDIDATES:
        if candidate.is_file():
            return str(candidate)
    value = shutil.which("google-chrome") or shutil.which("chromium")
    if value:
        return value
    raise RuntimeError("Google Chrome or Chromium is required to capture the viewer.")


def states() -> list[tuple[dict[str, str], int]]:
    """Return unique visual states and their frame holds; ends where it starts."""
    common = {"capture": "1", "token": "bottleneck", "zoom": "1"}
    sequence: list[tuple[dict[str, str], int]] = []

    def add(phase: str, trails: bool, yaw: float, pitch: float, hold: int) -> None:
        params = common | {
            "phase": phase,
            "trails": "1" if trails else "0",
            "yaw": f"{yaw:.2f}",
            "pitch": f"{pitch:.2f}",
        }
        sequence.append((params, hold))

    add("before", False, -0.35, 0.25, 12)
    add("before", True, -0.35, 0.25, 6)
    for yaw in (-0.35, -0.12, 0.12, 0.36, 0.60, 0.84):
        add("after", True, yaw, 0.25, 2)
    add("after", False, 0.84, 0.25, 18)
    for yaw in (0.60, 0.36, 0.12, -0.12, -0.35):
        add("after", True, yaw, 0.25, 2)
    add("before", True, -0.35, 0.25, 6)
    add("before", False, -0.35, 0.25, 12)
    return sequence


def render_frame(chrome: str, params: dict[str, str], path: Path) -> None:
    url = VIEWER.as_uri() + "?" + urlencode(params)
    command = [
        chrome,
        "--headless=new",
        "--disable-gpu",
        "--hide-scrollbars",
        "--force-color-profile=srgb",
        "--force-device-scale-factor=1",
        f"--window-size={VIEWPORT}",
        "--virtual-time-budget=1000",
        "--run-all-compositor-stages-before-draw",
        f"--screenshot={path}",
        url,
    ]
    subprocess.run(command, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.PIPE, text=True)
    if not path.is_file() or path.stat().st_size == 0:
        raise RuntimeError(f"Chrome did not write {path.name}")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT, help="GIF destination")
    args = parser.parse_args()
    if not VIEWER.is_file():
        raise RuntimeError(f"Missing viewer: {VIEWER}")
    chrome, ffmpeg = chrome_path(), command_exists("ffmpeg")
    output = args.output.resolve()
    output.parent.mkdir(parents=True, exist_ok=True)

    with tempfile.TemporaryDirectory(prefix="embedding-gif-") as temporary:
        frames_dir = Path(temporary)
        frame_number = 0
        for state_number, (params, hold) in enumerate(states()):
            still = frames_dir / f"still-{state_number:02d}.png"
            render_frame(chrome, params, still)
            for _ in range(hold):
                target = frames_dir / f"frame-{frame_number:04d}.png"
                shutil.copyfile(still, target)
                frame_number += 1

        palette = frames_dir / "palette.png"
        frames = str(frames_dir / "frame-%04d.png")
        subprocess.run(
            [ffmpeg, "-y", "-framerate", str(FPS), "-i", frames, "-vf", "palettegen=stats_mode=diff", str(palette)],
            check=True,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.PIPE,
            text=True,
        )
        subprocess.run(
            [
                ffmpeg, "-y", "-framerate", str(FPS), "-i", frames, "-i", str(palette),
                "-lavfi", "paletteuse=dither=bayer:bayer_scale=5", "-loop", "0", str(output),
            ],
            check=True,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.PIPE,
            text=True,
        )
    print(f"Wrote {output.relative_to(ROOT)}: {frame_number / FPS:.1f}s at {FPS} fps")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except RuntimeError as error:
        print(f"error: {error}", file=sys.stderr)
        raise SystemExit(1)
