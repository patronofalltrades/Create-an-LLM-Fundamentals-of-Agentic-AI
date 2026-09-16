# Assignment 3 — Creating an LLM: Plan

Planning date: September 15, 2026  
Status: baseline implementation and training complete; final repository QA pending
Target submission repository: [patronofalltrades/Customer-LLM-Fundamentals-of-Agentic-AI](https://github.com/patronofalltrades/Customer-LLM-Fundamentals-of-Agentic-AI)

## 1. Assignment in one sentence

Run the supplied, inspectable nanoGPT notebook from scratch on a permitted corpus; preserve the completed notebook and evidence; then explain, using actual values from that run, how text becomes token IDs, embeddings, predictions, loss, gradients, weight updates, and generated text.

This is an understanding-and-evidence assignment, not a contest to build the largest or most fluent model.

## 2. Authoritative sources

- [Assignment Google Doc](https://docs.google.com/document/d/1MQ3YQl2ywWZF7W5_l_91FiIp7pTYPO_3viI2JVapRcc/edit?tab=t.0)
- [Reference repository](https://github.com/pepealonso95/custom-llm)
- [Starter notebook](https://github.com/pepealonso95/custom-llm/blob/main/custom_llm.ipynb)
- [Student README template](https://github.com/pepealonso95/custom-llm/blob/main/STUDENT_README.md)
- [Pinned nanoGPT model source](https://github.com/karpathy/nanoGPT/blob/3adf61e154c3fe3fca428ad6bc3818b27a3b8291/model.py)

Source-access note: the Google Doc was read in view-only mode and exported to Markdown through the authenticated browser. The reference repository was inspected at commit `f520511` and its pinned starter files were used. A local Jupyter kernel executed both the 10-step setup run and the 3,000-step baseline.

## 3. Required outcome and deliverable

The single submitted deliverable is one **public GitHub repository URL** submitted through the course portal. That repository must make the experiment understandable without rerunning it.

The repository must include, at minimum:

- `custom_llm.ipynb`, saved after the final run with outputs visible
- a final student `README.md` containing the explanation and evidence
- selected output artifacts linked from the README
- the untrained, halfway, and final samples, including empty or garbled samples
- `training_curves.svg` and the complete measured loss table
- links to `history.json`, `tokenization.json`, `inspection.json`, `config.json`, `training.csv`, `training_summary.json`, and `temperature_comparison.json`
- a word-to-ID-to-64-number-vector example before and after training
- one saved parameter value, its gradient, and its update
- a next-token probability comparison
- a temperature comparison using the same starting token and sampling seed
- one observed limitation and one proposed next experiment

Keep the complete results ZIP locally. The ZIP does not contain the currently open notebook, so the executed notebook must be downloaded separately.

## 4. The three student decisions

The student interview is complete. The baseline decisions are:

- `CORPUS = "classroom"` plus one permitted Markdown or TXT file made from the main prose of [“The New World’s Bottleneck: Jevons, Baumol, and Who Captures the Gains from AI”](https://hanif.info/posts/the-new-worlds-bottleneck.html).
- Include the title, headings, and body paragraphs; exclude citations, footnotes, URLs, navigation, image labels, and acknowledgements.
- Disclose that the essay was student-directed and edited with AI assistance for brainstorming, outlining, editing, and generating some passages.
- Train for 3,000 optimizer steps at learning rate `0.001`, retaining the notebook's default warmup and cosine decay.
- Prediction: training and held-out loss should fall, while samples should increasingly combine the essay's recurring concepts but may remain repetitive, fragmented, or source-like. Lower-temperature samples should be more predictable; higher-temperature samples should be more varied and potentially incoherent.

### Corpus

Choose one:

1. `CORPUS = "classroom"` with only the supplied synthetic teaching corpus.
2. `CORPUS = "classroom"` plus permitted PDF/TXT/Markdown files in `corpus/`.
3. `CORPUS = "folder"` using only added files; this requires at least 100 distinct extracted passages.

The README must explain the corpus source and permissions, the number of unique passages added, what patterns the corpus could teach, and what it cannot teach.

### Training steps

- Use 10 steps only as a setup check.
- The assignment recommends 3,000 steps as the starting final training budget.
- Steps are optimizer updates, not full passes through the corpus.
- A positive whole number is required.

### Learning rate

- Start with `0.001` unless the student has a justified alternative.
- The notebook applies warmup and cosine decay.
- The explanation must address why too-large updates can destabilize or overshoot learning and why too-small updates can make learning ineffective within the budget.

The safest baseline is the classroom corpus, 3,000 steps, and learning rate 0.001. That is a recommendation, not a decision made for the student.

## 5. Fixed experiment controls

For a fair before/after comparison, do not change these between evaluation checkpoints:

- train/validation split
- fixed evaluation panels
- random seed
- baseline generation settings
- generation settings for untrained, halfway, and final samples
- starting token and sampling seed for the temperature comparison

Only the three required choices should change for the baseline. Optional experiments should change one variable at a time and come only after completing and understanding the baseline.

Important interpretation limits:

- Duplicate passages are removed before a 90/10 passage split.
- Validation passages do not update weights.
- Passages from one source file may appear in both training and validation, so validation does not test unseen-source generalization.
- The fixed loss panels contain at most 20 training and 20 validation passages; their values are small estimates, not full-corpus loss.
- Different corpora and vocabularies do not produce directly comparable loss scores.
- Falling training loss alone is not evidence of generalization.
- The classroom corpus repeats templates, so plausible samples do not prove broad understanding.

## 6. Technical boundaries and limitations

### Model scope

- Use the supplied nanoGPT implementation; rewriting the network is optional and unnecessary.
- The model is trained from scratch, with no API key and no pretrained weights.
- Default CPU runtime is sufficient; no GPU purchase is required.
- Classroom configuration: 2 transformer blocks, 4 attention heads, 64-dimensional token and position embeddings, 48-token context, PyTorch backpropagation, and AdamW.
- Tokenization uses words and punctuation for this classroom adaptation; that is not an intrinsic nanoGPT tokenizer choice.
- The model generates short, narrow-corpus sentences, not general chat answers.

### Corpus handling

- Supported added-file types: PDF, UTF-8 TXT, and UTF-8 Markdown.
- Scanned PDFs require OCR. Encrypted, unreadable, or entirely textless files stop the run. Partly textless PDFs create warnings.
- Markdown is treated as text; links and code are not fetched or executed.
- Long documents are split into non-overlapping passages of at most 47 word/punctuation tokens.
- The vocabulary retains the 509 most frequent training token types plus `UNK`, `BOS`, and `EOS` (up to 512 total).
- Report training and held-out unknown-token rates; rates above 5% trigger a warning in the notebook.
- Limits: 50 supported files, 25 MB per file, 100 MB total, 200 PDF pages per file, and 2 million extracted characters per file.
- Hidden files, symlinks, unsupported formats, and `corpus/README.md` are ignored.

### Privacy and sharing

- Use only material the student has permission to use and publish.
- `corpus/` is Git-ignored, but derived artifacts can reveal source text, filenames, hashes, and learned weights.
- Review the executed notebook and every shared artifact before publishing.
- Do not treat `.gitignore` as a privacy guarantee.

### Saved-model limitations

- `checkpoint.json` contains labels plus initial/final embeddings for the viewer.
- `model.pt` contains the full network weights and settings for inference.
- Neither is a complete exact-resume checkpoint with optimizer and random state.

## 7. Operative grading rubric

The supplied sources do **not** state a numerical point allocation. The following is the operative rubric inferred directly from the required evidence, README requirements, learning focus, definition of done, and submission checklist.

| Grading dimension | Evidence the grader should find | Failure mode to avoid |
| --- | --- | --- |
| Reproducibility and completeness | Executed notebook with outputs; actual config, run status, completed steps, time, hardware, parameter count, and linked artifacts | Uploading the untouched starter or clearing outputs |
| Experimental design | Corpus, permissions, unique passages, steps, learning rate, reasons, prediction, fixed controls, 90/10 split, panel sizes, and unknown-token rates | Changing evaluation settings or hiding failed/interrupted work |
| Before/during/after comparison | All untrained, halfway, and final samples plus the complete loss table and plot | Cherry-picking fluent samples or reporting training loss only |
| Token and embedding understanding | One real word, token ID, and full 64-number vector before/after; correct distinction among token, ID, vector, and embedding | Describing coordinates as named concepts or inventing values |
| Learning mechanics | One real parameter value, gradient, update, loss, optimizer role, and changed prediction | Giving a generic explanation unconnected to notebook evidence |
| Attention and generation | Explain causal context, next-token probabilities, sampling, and temperature; state that temperature does not update weights | Claiming the model sees future tokens or retrains at each temperature |
| Honest interpretation | Compare training and held-out loss with samples; identify a limitation; avoid broad generalization claims | Calling plausible output proof of understanding/general intelligence |
| Next experiment | One specific change, reason, and predicted effect; second run optional | Proposing several uncontrolled changes without a hypothesis |
| Public submission quality | README works as entry point; evidence links resolve while signed out; notebook renders on GitHub | Broken/private links or evidence available only locally |

## 8. Phased implementation plan — baseline completed

### Phase 0 — Interview and decisions

Before touching code, ask the student:

1. What topic or material should the model learn from?
2. Does the student have permission to publish that material and derived excerpts/artifacts?
3. Which corpus mode should be used: classroom only, classroom plus files, or folder only?
4. What training budget is practical on the student's machine or Colab session?
5. Does the student accept the recommended baseline of 3,000 steps and learning rate 0.001?
6. What behavior or pattern does the student predict before training?
7. Which word will be easy and meaningful to trace through ID, embedding, probabilities, gradient, and update evidence?

Record the answers in the README's choices-and-prediction section before running the final experiment.

### Phase 1 — Repository and environment setup

- Confirm the target repository is the intended public submission repository.
- Bring in the starter materials while preserving upstream attribution and the nanoGPT license.
- Use Python 3 and install `requirements.txt`, or open the notebook in Colab.
- Confirm the notebook and pinned model source load without changing model logic.
- Ensure `corpus/` remains ignored and no private source file is staged.

Acceptance check: a 10-step setup run completes, but its results are clearly labeled as a setup check and not the final experiment.

### Phase 2 — Corpus validation

- Add only approved source files.
- Run the setup/data sections to create and inspect `corpus/`.
- Read extraction previews, page warnings, passage counts, duplicates, and ignored files.
- Inspect `corpus_manifest.json`, `corpus.txt`, and `vocabulary_report.json`.
- Confirm at least 100 distinct passages if using folder-only mode.
- Confirm meaningful tokens are retained and both unknown-token rates are acceptable or honestly explained.

Acceptance check: the student can explain what the model can learn from these passages and what remains out of scope.

### Phase 3 — Freeze the baseline experiment

- Set corpus mode, training steps, and learning rate.
- Write reasons and a pre-training prediction.
- Record the fixed split, seeds, panel sizes, and generation settings.
- Avoid optional architecture or evaluation changes.

Acceptance check: the experiment has a single, testable baseline and no results have been invented in advance.

### Phase 4 — Final run in notebook order

- Run All from the top.
- Let data inspection, untrained evaluation, training, halfway/final evaluation, inspection, plots, and saving finish in order.
- If training is interrupted, continue through inspection/plot/download cells and report completed steps. For other errors, fix the cause and rerun from the top.
- Do not delete empty, garbled, or unfavorable outputs.

Acceptance check: all expected cells have visible outputs and the final notebook records the actual training budget.

### Phase 5 — Preserve and inspect evidence

- Download the complete results ZIP before ending a Colab session.
- Download the executed `.ipynb` separately.
- Open `embedding-viewer.html` locally and load the run's `checkpoint.json`.
- Inspect a token's initial/final 64D vector and cosine neighbors; remember that 3D PCA is a lossy projection.
- Collect the exact loss values, panel sizes, samples, probability comparison, saved gradient, parameter update, and temperature outputs.

Acceptance check: every README claim can point to a specific notebook output or saved artifact.

### Phase 6 — Write the evidence-first README

Use this order:

1. Overview and how to run/inspect
2. Corpus sources, permission, extraction validation, and warnings
3. Choices, reasons, and pre-training prediction
4. Actual run facts and interruptions/failures
5. Full loss table and embedded curve
6. Untrained, halfway, and final samples
7. Word → ID → vector before/after
8. Parameter → gradient → update
9. Next-token probabilities and attention/context explanation
10. Temperature comparison and why weights did not change
11. What the evidence supports and does not support
12. One limitation and one next experiment

Acceptance check: a reader can grade the work from the README without rerunning the notebook.

### Phase 7 — Final QA and submission

- Open the notebook on GitHub and verify its outputs render.
- Test every README link and image.
- Verify the repository while signed out.
- Scan committed files and notebook outputs for private/confidential source content.
- Keep the complete ZIP locally.
- Submit the single public repository URL through the course portal.

## 9. Likely pitfalls

- Treating the starter's reference results as the student's results
- Running 10 steps and presenting it as meaningful final training
- Editing multiple settings at once, which destroys causal interpretation
- Forgetting to write the prediction before seeing results
- Comparing losses across different corpora as if lower always means better
- Reporting only training loss or omitting panel sizes
- Cherry-picking samples or omitting empty/garbled outputs
- Claiming validation proves unseen-document generalization
- Confusing token lookup embeddings with contextual representations after attention
- Treating a PCA plot coordinate as a human-readable semantic concept
- Saying temperature retrains the model or changes weights
- Uploading source files or derived text without permission
- Assuming the results ZIP contains the executed notebook
- Clearing notebook outputs before pushing
- Publishing broken/private evidence links
- Claiming fluent text proves understanding or broad knowledge

## 10. Baseline completion status

Completed:

- imported the pinned starter notebook and nanoGPT source with its license
- created the agreed main-prose essay corpus with no extraction warnings
- completed a separate 10-step Jupyter setup run
- completed the 3,000-step baseline at learning rate `0.001`
- preserved the executed notebook and complete selected evidence
- replaced README placeholders with actual measurements and honest interpretation

Still pending:

- commit and push the completed baseline after user authorization
- verify GitHub notebook rendering, evidence links, and signed-out public access
- submit the repository URL only when the student requests submission
- keep the CIA/FBI corpus experiment deferred until Friday
