# Assignment 3 — Creating an LLM

> **Status: planning complete; implementation and training are scheduled for tomorrow.**
>
> This repository intentionally contains no starter code, corpus, executed notebook, model, training run, generated samples, plots, or experimental results yet. Every `TBD` field below must be replaced only with evidence from the student's own completed run.

## Purpose

This project will be the public submission for Assignment 3: a small language model trained **from scratch** with the supplied, inspectable nanoGPT notebook. The aim is to show how a permitted corpus becomes tokens, IDs, embedding vectors, next-token predictions, loss, gradients, weight updates, and generated text—not to produce a general-purpose chatbot.

The completed submission will be available at [patronofalltrades/Customer-LLM-Fundamentals-of-Agentic-AI](https://github.com/patronofalltrades/Customer-LLM-Fundamentals-of-Agentic-AI).

## Today's stop point

Today was reserved for understanding the assignment, its boundaries, and its grading evidence. The work completed today is:

- a detailed [assignment plan](ASSIGNMENT_PLAN.md);
- a durable [assignment context](assignment-context.md) for resuming tomorrow; and
- this evidence-first README scaffold.

No implementation decision has been made on the student's behalf. In particular, no corpus was selected, no source-material permission was asserted, no training settings were finalized, and no run was performed. The reference project's results are **not** this student's results and will not be presented as such.

## Assignment scope and fixed boundaries

The planned baseline uses the course-supplied `custom_llm.ipynb` and the pinned nanoGPT implementation. It is a compact word/punctuation-token transformer trained from scratch with PyTorch and AdamW—no pretrained weights, external model API, GPU purchase, web app, backend, or deployment is required.

The supplied classroom configuration has 2 transformer blocks, 4 attention heads, 64-dimensional token and position embeddings, and a 48-token context window. The word tokenizer is a classroom adaptation, not a claim about nanoGPT's default tokenizer.

For a fair before/during/after comparison, the final experiment will keep its train/validation split, fixed evaluation panels, random seed, and baseline generation settings unchanged. The temperature comparison will use the same starting token and sampling seed; it changes sampling at inference, never the trained weights.

## Student decision record — complete before training

| Required decision | Student answer | Reason / evidence to record |
| --- | --- | --- |
| Corpus mode | **TBD** — `classroom`, `classroom + permitted files`, or `folder` only | Why this corpus is appropriate for a small language model |
| Corpus topic and source(s) | **TBD** | Source names/links and what patterns they can and cannot teach |
| Permission to publish sources and derived artifacts | **TBD** | Explicit confirmation; remove or withhold material that cannot be public |
| Unique added passages | **TBD after validation** | `0` if classroom-only; folder-only requires at least 100 distinct passages |
| Training steps | **TBD** | A 10-step run is setup only; the recommended meaningful baseline is 3,000 optimizer updates |
| Learning rate | **TBD** | Start from `0.001` unless a justified alternative is chosen; explain too-large vs. too-small updates |
| Pre-training prediction | **TBD** | A testable expectation written before seeing final results |
| Token/word to trace | **TBD** | A meaningful retained word to follow from text to ID, 64D vector, probabilities, gradient, and update |
| Environment | **TBD** — local Jupyter/VS Code or Colab | Hardware/runtime details to report after the actual run |

## Tomorrow's workflow

1. Interview the student and record the decision table and prediction above.
2. Inspect this repository before adding anything; then bring in the supplied starter materials with attribution and the nanoGPT MIT license.
3. Set up the Python environment or Colab notebook and run a **10-step smoke test**, labeled only as a setup check.
4. Add only approved PDF, UTF-8 TXT, or UTF-8 Markdown source files; review extraction previews, warnings, duplicate removal, passage counts, `corpus_manifest.json`, and `vocabulary_report.json`.
5. Freeze one baseline: corpus mode, training steps, learning rate, split, seed, evaluation panels, and generation settings. Optional experiments come only after this baseline.
6. Run the notebook from top to bottom and keep all untrained, halfway, final, empty, and garbled outputs.
7. Save the final artifacts, download the complete results ZIP, and download the executed notebook separately (the ZIP does not include the active notebook).
8. Replace this scaffold's `TBD` fields with exact values from the notebook and artifacts—never reconstructed or reference values.
9. Review privacy, render the notebook and README on GitHub, test every link while signed out, and only then submit the public repository URL through the course portal.

## Planned experiment controls and limitations

- Passages are deduplicated before the planned 90/10 train/validation split. Validation passages do not update weights, but passages from the same source file can land on both sides; this does not test unseen-source generalization.
- Fixed loss panels contain at most 20 training and 20 validation passages. Their losses are estimates, not full-corpus measurements, and losses from different corpora/vocabularies are not directly comparable.
- Long documents are split into non-overlapping passages of at most 47 word/punctuation tokens. The vocabulary keeps the 509 most common training types plus `UNK`, `BOS`, and `EOS` (up to 512 total); training and held-out unknown-token rates must be reported.
- A falling training loss alone does not demonstrate generalization. Plausible output from a small or template-heavy corpus does not show broad knowledge or language understanding.
- Token lookup embeddings are not context-dependent representations after attention. A 3D PCA embedding view is lossy; cosine-neighbor comparisons use the full 64-dimensional vectors.
- `checkpoint.json` and `model.pt` are useful saved artifacts, but neither is an exact resume checkpoint with optimizer and random state.

## Evidence that will be added after the final run

All links in this section are intentionally pending. The final README will link real committed artifacts and display actual notebook outputs.

### Run facts and reproducibility

| Item | Actual value / link |
| --- | --- |
| Executed notebook | **TBD** — [`custom_llm.ipynb`](custom_llm.ipynb) with all final outputs visible |
| Final run status and completed steps | **TBD** |
| Elapsed time and hardware | **TBD** |
| Parameter count | **TBD** |
| Corpus/document count and 90/10 split sizes | **TBD** |
| Vocabulary size | **TBD** |
| Training / held-out unknown-token rates | **TBD** |
| Configuration | **TBD** — [`config.json`](config.json) |
| Training summary | **TBD** — [`training_summary.json`](training_summary.json) |
| Full training rows | **TBD** — [`training.csv`](training.csv) |
| Corpus extraction and duplicates | **TBD, if safe to share** — [`corpus_manifest.json`](corpus_manifest.json) |
| Vocabulary coverage | **TBD** — [`vocabulary_report.json`](vocabulary_report.json) |

If a run is interrupted or fails, this section will state what happened, how many steps completed, and which evidence was still saved. It will not be hidden or relabeled as a complete run.

### Losses and samples

The completed README will embed [`training_curves.svg`](training_curves.svg), link [`history.json`](history.json), and list every measured value from the fixed panels. Panel sizes will be stated alongside the table.

| Step | Training-panel loss | Validation-panel loss |
| ---: | ---: | ---: |
| 0 | **TBD** | **TBD** |
| halfway: **TBD** | **TBD** | **TBD** |
| final: **TBD** | **TBD** | **TBD** |

The untrained, halfway, and final samples—including any empty or garbled text—will be quoted here and linked to their full saved files:

| Checkpoint | Same fixed generation settings? | Sample / link | Observation |
| --- | --- | --- | --- |
| Untrained | **TBD** | **TBD** | **TBD** |
| Halfway | **TBD** | **TBD** | **TBD** |
| Final | **TBD** | **TBD** | **TBD** |

### From text to learned predictions

The student will fill the following from [`tokenization.json`](tokenization.json) and [`inspection.json`](inspection.json), using a real retained token and exact notebook values.

| Evidence | Actual value and explanation |
| --- | --- |
| Word/token | **TBD** |
| Token ID | **TBD** — an integer lookup key, not the embedding itself |
| Initial 64-number token-lookup vector | **TBD** |
| Final 64-number token-lookup vector | **TBD** |
| One prefix and next-token probability comparison | **TBD** |
| Saved parameter value before update | **TBD** |
| Gradient for that parameter | **TBD** |
| Parameter value after optimizer update | **TBD** |

The final explanation will connect these facts: text is tokenized; IDs index learned embedding vectors; the causal transformer combines each position with earlier context only; it produces next-token probabilities; loss measures mismatch with the observed next token; backpropagation calculates gradients; AdamW updates weights. It will distinguish token lookup vectors from contextual representations and describe the actual evidence rather than assigning individual vector coordinates human-readable meanings.

### Temperature comparison

The final README will link [`temperature_comparison.json`](temperature_comparison.json) and compare three temperatures with the same starting token and sampling seed.

| Temperature | Actual sample | What changed? | Did weights change? |
| ---: | --- | --- | --- |
| **TBD** | **TBD** | **TBD** | No — inference sampling only |
| **TBD** | **TBD** | **TBD** | No — inference sampling only |
| **TBD** | **TBD** | **TBD** | No — inference sampling only |

## Interpretation, limitation, and next experiment

After training, this section will answer these questions using the actual loss curves, held-out panel, samples, vectors, probabilities, gradient, and update:

- Did the evidence support the pre-training prediction? **TBD**
- What can the chosen corpus teach, and what is outside its scope? **TBD**
- What does the training/validation comparison support—and not support—about generalization? **TBD**
- One observed limitation: **TBD**
- One controlled next experiment (change one variable, why, and predicted effect): **TBD**

## Privacy and publication review

Only material that the student has permission to use **and publicly share** will be placed in or derived into this repository. `corpus/` will be Git-ignored after starter materials are added, but that is not a privacy guarantee: extracted text, filenames, hashes, samples, notebook outputs, and learned weights may expose source information. Before publishing, the student will review the executed notebook and every artifact for confidential, personal, copyrighted, or otherwise restricted information.

Supported added inputs are PDF, UTF-8 TXT, and UTF-8 Markdown. Scanned PDFs require OCR; encrypted, unreadable, or entirely textless PDFs stop the run, and partly textless PDFs produce warnings. The planned review will document these warnings and the resolution rather than silently ignoring them.

## How the completed work will be inspected and reproduced

When implementation begins, the final repository will include the starter's environment instructions and the executed `custom_llm.ipynb`. A reviewer will be able to install the documented dependencies (or open the notebook in Colab), place only permitted inputs in `corpus/` when applicable, select the recorded corpus mode/steps/learning rate, and run the notebook from the top.

For grading, rerunning should not be necessary: the executed notebook, loss curve, full loss data, sample timeline, configuration, tokenization/inspection evidence, and temperature comparison will remain visible and linked. The complete results ZIP will be retained locally as a backup; the executed notebook will be preserved separately.

## Sources and attribution

- [Assignment instructions](https://docs.google.com/document/d/1MQ3YQl2ywWZF7W5_l_91FiIp7pTYPO_3viI2JVapRcc/edit?tab=t.0)
- [Course reference repository](https://github.com/pepealonso95/custom-llm)
- [Course student README template](https://github.com/pepealonso95/custom-llm/blob/main/STUDENT_README.md)
- [Pinned nanoGPT model source](https://github.com/karpathy/nanoGPT/blob/3adf61e154c3fe3fca428ad6bc3818b27a3b8291/model.py) (MIT license will be included with the starter materials)

The assignment instructions are authoritative. This README is a planning-stage scaffold based on them and will be updated only after the student's interview and final experiment.
