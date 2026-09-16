"""Create a configured assignment notebook without editing outputs by hand."""

from pathlib import Path
import argparse

import nbformat


PREDICTIONS = {
    "starter": """### My choices and pre-training prediction

- **Corpus:** the supplied classroom corpus only. The added-corpus folder is intentionally empty for this control experiment.
- **Training budget:** {steps:,} optimizer updates. A separate 10-step run is only a setup check.
- **Learning rate:** 0.001 with the notebook's default warmup and cosine decay.
- **Trace token:** `customer`, a frequent word in the classroom corpus.

Before training, I predict that training and held-out loss will fall. The model should improve most on the starter-pattern tests because those associations are represented in the classroom data. Many extension tests should remain out of vocabulary or incorrect. Generated text may become more structured but should remain repetitive because the model and corpus are small.
""",
    "expanded": """### My choices and pre-training prediction

- **Corpus:** the supplied classroom corpus plus original focused teaching passages for grammar and opposites. The fixed evaluation prompts, choices, answers, explanations, and outputs remain outside the corpus.
- **Training budget:** {steps:,} optimizer updates. This matches the starter experiment.
- **Learning rate:** 0.001 with the notebook's default warmup and cosine decay.
- **Trace token:** `cold`, a contrast word in the added teaching material.

Before training, I predict that training loss will fall. The added examples should improve vocabulary coverage for grammar and opposites, but more coverage does not guarantee correct next-word predictions. Some category scores may stay flat or fall. The model may use contrast vocabulary while remaining repetitive, fragmented, or overly similar to its sources. Lower-temperature output should be more predictable; higher-temperature output should be more varied and more likely to become incoherent.
""",
}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("input", type=Path)
    parser.add_argument("output", type=Path)
    parser.add_argument("--steps", type=int, required=True)
    parser.add_argument("--experiment", choices=sorted(PREDICTIONS), required=True)
    parser.add_argument("--corpus-folder", type=Path, required=True)
    args = parser.parse_args()

    notebook = nbformat.read(args.input, as_version=4)
    settings_changed = False
    probe_changed = False
    prediction_changed = False

    probe = "customer" if args.experiment == "starter" else "cold"
    prefix = "the customer" if probe == "customer" else "the cold"

    for cell in notebook.cells:
        source = cell.source
        if cell.cell_type == "code" and "TRAINING_STEPS =" in source:
            lines = []
            for line in source.splitlines():
                if line.startswith("CORPUS_FOLDER ="):
                    line = f'CORPUS_FOLDER = "{args.corpus_folder.as_posix()}"'
                elif line.startswith("TRAINING_STEPS ="):
                    line = f"TRAINING_STEPS = {args.steps}      # fixed across both experiments"
                    settings_changed = True
                lines.append(line)
            cell.source = "\n".join(lines)
        elif cell.cell_type == "code" and "probe_word =" in source:
            old_probe = 'probe_word = "customer" if "customer" in stoi else vocabulary[3]'
            old_prefix = 'prefix = "the customer" if "customer" in stoi else decode(encode(example)[:3])'
            cell.source = source.replace(
                old_probe,
                f'probe_word = "{probe}" if "{probe}" in stoi else vocabulary[3]',
            ).replace(
                old_prefix,
                f'prefix = "{prefix}" if "{probe}" in stoi else decode(encode(example)[:3])',
            )
            probe_changed = f'probe_word = "{probe}"' in cell.source
        elif cell.cell_type == "markdown" and (
            "### My prediction" in source or "### My choices and pre-training prediction" in source
        ):
            cell.source = PREDICTIONS[args.experiment].format(steps=args.steps)
            prediction_changed = True

    if not (settings_changed and probe_changed and prediction_changed):
        raise RuntimeError(
            f"Notebook structure changed: settings={settings_changed}, "
            f"probe={probe_changed}, prediction={prediction_changed}"
        )

    nbformat.write(notebook, args.output)
    print(f"Configured {args.output} for {args.experiment} at {args.steps} steps")


if __name__ == "__main__":
    main()
