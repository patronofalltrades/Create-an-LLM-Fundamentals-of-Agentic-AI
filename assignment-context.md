# Assignment 3 durable context

Last updated: 2026-09-15  
Current state: essay baseline implemented and trained; local final QA in progress; remote publication pending

## Goal

Create one public GitHub submission that uses the supplied `custom_llm.ipynb`/nanoGPT model, preserves a completed final run, and explains the learning process using the student's actual evidence.

## Repositories and sources

- Assignment: https://docs.google.com/document/d/1MQ3YQl2ywWZF7W5_l_91FiIp7pTYPO_3viI2JVapRcc/edit?tab=t.0
- Reference: https://github.com/pepealonso95/custom-llm
- Target: https://github.com/patronofalltrades/Customer-LLM-Fundamentals-of-Agentic-AI
- Reference commit observed during planning: `f520511`
- Full planning document: `ASSIGNMENT_PLAN.md`

Access note: the assignment was read via a view-only Google Docs browser export. The reference repository was inspected at commit `f520511`, and its pinned starter assets were imported. The notebook was executed locally in Jupyter.

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

## Student decisions recorded on 2026-09-15

- **Baseline corpus mode:** `classroom` plus one permitted file.
- **Essay source:** [“The New World’s Bottleneck: Jevons, Baumol, and Who Captures the Gains from AI”](https://hanif.info/posts/the-new-worlds-bottleneck.html).
- **Corpus-file boundary:** include main essay prose only—the title, headings, and body. Exclude citations, footnotes, URLs, navigation, image labels, and acknowledgements.
- **Provenance:** student-directed and edited with AI assistance for brainstorming, outlining, editing, and generating some passages.
- **Publication permission:** the student is comfortable sharing the essay and derived artifacts publicly, subject to the final privacy review.
- **Training baseline:** 3,000 optimizer updates; learning rate `0.001`; retain the notebook's default warmup and cosine decay.
- **Pre-training prediction:** training and held-out loss should fall; samples should increasingly combine “bottleneck,” “constraint,” “automation,” “demand,” and “AI” plausibly, while potentially remaining repetitive, fragmented, or source-like. Lower temperatures should be more predictable/repetitive; higher temperatures more varied and possibly incoherent.
- **Trace token:** `bottleneck`.
- **Execution environment:** local Jupyter on Apple Silicon CPU.

### Friday follow-up experiment — explicitly deferred and excluded from the baseline

After the essay baseline is complete, the student intends to consider a second corpus experiment on Friday using one focused, officially released CIA or FBI document. Prefer an analytical or historical document that is substantially unredacted and avoid a large case file centered on a private individual. This is not part of tomorrow's baseline and must not be sourced or implemented early.

Before use, verify the exact document's official CIA Reading Room or FBI Vault URL, public-release and redaction status, machine-readable text or OCR quality, privacy implications, and any embedded third-party copyright. Use only the officially released text and never reconstruct redacted passages. Run it as a separately documented experiment, changing one variable at a time. Because a new corpus can change the vocabulary, do not rank it against the essay run solely by comparing raw loss values.

## Completed baseline results

- **Status:** 3,000/3,000 steps completed without interruption or notebook errors.
- **Training runtime:** 19.19 seconds on CPU; Python 3.9.6; PyTorch 2.8.0.
- **Model:** 135,936 parameters; 2 layers; 4 heads; 64D embeddings; 48-token context.
- **Corpus:** 184 new unique essay passages; 4,816 combined unique passages; 4,334 train / 482 validation.
- **Vocabulary:** 512 entries; training UNK 1.02%; held-out UNK 1.61%.
- **Losses:** step 0 = 6.2454 train / 6.2732 validation; step 1,500 = 0.9090 / 1.1599; step 3,000 = 0.8691 / 1.2489.
- **Interpretation:** substantial learning from baseline, but validation worsened after step 1,500 while training improved, indicating overfitting.
- **Essay signal:** final `bottleneck` neighbors include `constraint`, `robots`, `same`, `demand`, and `matrix`; “the bottleneck” next-token probabilities shifted toward essay-like continuations.
- **Generation limitation:** halfway and final unconditional samples were identical classroom templates because the classroom corpus dominated the mixture.
- **Evidence location:** `results/essay-baseline/`; executed notebook: `custom_llm.ipynb`; grading narrative: `README.md`.

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

## Next actions

1. Finish local link, notebook-output, and privacy checks.
2. Commit and push only after the user grants the required repository-write approval.
3. Verify README rendering, notebook outputs, evidence links, and public access on GitHub.
4. Do not submit to the course portal unless the student explicitly requests it.
5. Keep the CIA/FBI follow-up deferred until Friday.
