# Assignment 3 durable context

Last updated: 2026-09-15  
Current state: planning only; no implementation or training performed

## Goal

Create one public GitHub submission that uses the supplied `custom_llm.ipynb`/nanoGPT model, preserves a completed final run, and explains the learning process using the student's actual evidence.

## Repositories and sources

- Assignment: https://docs.google.com/document/d/1MQ3YQl2ywWZF7W5_l_91FiIp7pTYPO_3viI2JVapRcc/edit?tab=t.0
- Reference: https://github.com/pepealonso95/custom-llm
- Target: https://github.com/patronofalltrades/Customer-LLM-Fundamentals-of-Agentic-AI
- Reference commit observed during planning: `f520511`
- Full planning document: `ASSIGNMENT_PLAN.md`

Access note: the assignment was read via a view-only Google Docs browser export. The reference repository was inspected at commit `f520511` through GitHub and a temporary local clone. The notebook was not executed.

## Assignment constants

- Supplied model only; writing a new network is optional.
- From-scratch, small word/punctuation-token nanoGPT; no pretrained weights/API key.
- Model config: 2 blocks, 4 heads, 64D embeddings, 48-token context, PyTorch + AdamW.
- Corpus mode choices: classroom; classroom + permitted files; folder-only.
- Folder-only requires >=100 distinct extracted passages.
- Recommended final baseline: 3,000 steps; learning rate 0.001.
- 10 steps is a setup check, not a meaningful final experiment.
- Vocabulary: top 509 training token types + UNK/BOS/EOS, max 512.
- Split: deduplicated passages, 90/10. Same source file can feed both sides.
- Loss panels: fixed, <=20 train and <=20 validation passages; report every value and panel sizes.
- Keep split, seeds, panels, and generation settings fixed across checkpoints.
- Temperature comparison uses the same start token and sampling seed; temperature changes inference, not weights.

## Inputs still required from the student

Do not assume these:

1. Corpus topic and source(s)
2. Permission to publish source/derived artifacts
3. Corpus mode
4. Training-step budget
5. Learning rate (default recommendation: 0.001)
6. Pre-training prediction
7. Meaningful token/word to trace
8. Local Jupyter/VS Code vs. Colab preference

## Required final evidence

- Executed `custom_llm.ipynb` with all final outputs visible
- README as grading entry point
- untrained, halfway, and final samples, including bad/empty samples
- `training_curves.svg` and complete loss table from `history.json`
- actual panel sizes
- actual run steps, elapsed time, hardware, parameter count, vocabulary size, passage/split sizes
- training and held-out UNK rates
- corpus permission/source/extraction discussion; links to manifest/report when shareable
- one word → token ID → full 64D vector before/after
- one real parameter value + gradient + update
- next-token probability comparison
- attention/causal-context explanation
- three-temperature comparison; explain no retraining/weight change
- honest conclusion, one observed limitation, one proposed next experiment
- links: `config.json`, `corpus_manifest.json`, `vocabulary_report.json`, `tokenization.json`, `inspection.json`, `history.json`, `training.csv`, `training_summary.json`, `temperature_comparison.json`
- public/signed-out link verification
- complete ZIP kept locally; executed notebook downloaded separately

## Corpus limits and privacy

- PDF/TXT/MD only; TXT/MD UTF-8; scanned PDF needs OCR.
- Max 50 files, 25 MB/file, 100 MB total, 200 PDF pages/file, 2M extracted chars/file.
- Long text becomes non-overlapping passages <=47 tokens.
- Inspect extraction previews/warnings, duplicates, `corpus_manifest.json`, and `vocabulary_report.json`.
- `corpus/` being Git-ignored does not protect derived text, filenames/hashes, notebook examples, or weights.
- Use only material permitted for public sharing; review every artifact before push.

## Interpretation guardrails

- No numeric point rubric was provided; grade coverage is inferred from required evidence, README requirements, definition of done, and checklist.
- Falling train loss alone != generalization.
- Validation split is by passage, not source file.
- Classroom held-out text shares templates with train text.
- Different corpus/vocabulary losses are not directly comparable.
- Plausible samples do not prove general knowledge/understanding.
- PCA 3D placement is lossy; cosine neighbors use full 64D vectors.
- Token lookup embeddings are not contextual post-attention representations.
- `checkpoint.json` and `model.pt` are not exact optimizer/random-state resume files.

## Tomorrow's entry sequence

1. Interview student and record decisions/prediction.
2. Inspect target repo state before modifying anything.
3. Bring in starter assets/license with attribution; preserve user work.
4. Set up environment; run 10-step smoke test and label it as such.
5. Validate corpus and vocabulary reports.
6. Freeze baseline settings/controls.
7. Run final notebook in order.
8. Download ZIP + executed notebook separately.
9. Inspect exact evidence and embedding viewer.
10. Replace README placeholders with actual values only.
11. Verify GitHub rendering, links, privacy, and signed-out access.

## Hard stop carried from today

No code, corpus, training, result claims, publishing, or submission was done today. Do not fill README results until the final run supplies them.
