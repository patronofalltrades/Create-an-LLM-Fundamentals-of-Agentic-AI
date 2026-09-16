"""Create a configured assignment notebook without editing outputs by hand."""

from pathlib import Path
import argparse

import nbformat


PREDICTION = """### My choices and pre-training prediction

- **Corpus:** supplied classroom corpus plus the main prose from *The New World's Bottleneck: Jevons, Baumol, and Who Captures the Gains from AI*. The essay was student-directed and edited with AI assistance for brainstorming, outlining, editing, and generating some passages. Citations, footnotes, URLs, navigation, image labels, and acknowledgements are excluded.
- **Training budget:** {steps:,} optimizer updates. A separate 10-step run is only a setup check.
- **Learning rate:** 0.001 with the notebook's default warmup and cosine decay.
- **Trace token:** `bottleneck`, a frequent and central word in the essay.

Before training, I predict that training and held-out loss will fall. Samples should increasingly combine words such as *bottleneck*, *constraint*, *automation*, *demand*, and *AI* in more plausible ways, although this small model may remain repetitive, fragmented, or overly similar to its source text. Lower-temperature output should be more predictable and repetitive; higher-temperature output should be more varied and more likely to become incoherent.
"""


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("input", type=Path)
    parser.add_argument("output", type=Path)
    parser.add_argument("--steps", type=int, required=True)
    args = parser.parse_args()

    notebook = nbformat.read(args.input, as_version=4)
    settings_changed = False
    probe_changed = False
    prediction_changed = False

    for cell in notebook.cells:
        source = cell.source
        if cell.cell_type == "code" and "TRAINING_STEPS =" in source:
            lines = []
            for line in source.splitlines():
                if line.startswith("TRAINING_STEPS ="):
                    line = f"TRAINING_STEPS = {args.steps}      # 10 for setup; 3000 for the main experiment"
                    settings_changed = True
                lines.append(line)
            cell.source = "\n".join(lines)
        elif cell.cell_type == "code" and "probe_word =" in source:
            if 'probe_word = "customer"' in source:
                cell.source = source.replace(
                    'probe_word = "customer" if "customer" in stoi else vocabulary[3]\n'
                    'probe_id = stoi[probe_word]\n'
                    'prefix = "the customer" if "customer" in stoi else decode(encode(example)[:3])',
                    'probe_word = "bottleneck" if "bottleneck" in stoi else vocabulary[3]\n'
                    'probe_id = stoi[probe_word]\n'
                    'prefix = "the bottleneck" if "bottleneck" in stoi else decode(encode(example)[:3])',
                )
            probe_changed = 'probe_word = "bottleneck"' in cell.source
        elif cell.cell_type == "markdown" and (
            "### My prediction" in source or "### My choices and pre-training prediction" in source
        ):
            cell.source = PREDICTION.format(steps=args.steps)
            prediction_changed = True

    if not (settings_changed and probe_changed and prediction_changed):
        raise RuntimeError(
            f"Notebook structure changed: settings={settings_changed}, "
            f"probe={probe_changed}, prediction={prediction_changed}"
        )

    nbformat.write(notebook, args.output)
    print(f"Configured {args.output} for {args.steps} steps")


if __name__ == "__main__":
    main()
