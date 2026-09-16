# Assignment 3 Context

Last updated: September 15, 2026

Current state: essay baseline complete, tested, and published

## Goal

Create one public GitHub repository for Assignment 3. Use the supplied nanoGPT notebook. Train a small model from random weights. Explain the process with evidence from the final run.

## Important links

- [Assignment document](https://docs.google.com/document/d/1MQ3YQl2ywWZF7W5_l_91FiIp7pTYPO_3viI2JVapRcc/edit?tab=t.0)
- [Starter repository](https://github.com/pepealonso95/custom-llm)
- [Submission repository](https://github.com/patronofalltrades/Customer-LLM-Fundamentals-of-Agentic-AI)
- [Published essay](https://hanif.info/posts/the-new-worlds-bottleneck.html)

## Corpus decision

Use the classroom corpus and one permitted essay file. Include the essay title, headings, and main body. Exclude citations, footnotes, URLs, navigation, image labels, and acknowledgements.

The student directed and edited the essay. AI tools helped with brainstorming, outlining, editing, and some generated passages. The student approved public use of the essay and derived experiment files.

## Training decision

- Corpus mode: `classroom`
- Training steps: 3,000
- Learning rate: `0.001`
- Warmup and cosine decay: enabled
- Trace token: `bottleneck`
- Execution: local Jupyter on Apple Silicon CPU

Keep the random seed, split, evaluation panels, and generation settings fixed.

## Model constants

- Transformer blocks: 2
- Attention heads: 4
- Embedding size: 64 numbers
- Context limit: 48 tokens
- Vocabulary limit: 512 entries
- Optimizer: AdamW
- Pretrained weights: none

## Final results

- The final run completed 3,000 of 3,000 updates.
- The run had no interruption and no notebook error.
- Training took 19.19 seconds.
- The model has 135,936 parameters.
- The essay added 184 unique passages.
- The combined corpus has 4,816 unique passages.
- The training set has 4,334 passages.
- The validation set has 482 passages.
- The vocabulary has 512 entries.
- The training unknown-token rate is 1.02%.
- The validation unknown-token rate is 1.61%.

| Step | Training loss | Validation loss |
| ---: | ---: | ---: |
| 0 | 6.2454 | 6.2732 |
| 1,500 | 0.9090 | 1.1599 |
| 3,000 | 0.8691 | 1.2489 |

The validation loss increased after step 1,500 while the training loss decreased. This result shows overfitting.

The final `bottleneck` neighbors include `constraint`, `robots`, `same`, `demand`, and `matrix`. The final unconditional samples still use classroom patterns. The classroom corpus dominates the data mixture.

## Evidence locations

- Grading explanation: `README.md`
- Executed notebook: `custom_llm.ipynb`
- Final evidence: `results/essay-baseline/`
- Experiment plan: `ASSIGNMENT_PLAN.md`
- Original instructor requirements: `ASSIGNMENT.md`

## Interpretation rules

- A lower training loss does not prove generalization.
- The validation split uses passages, not complete source files.
- A plausible sample does not prove understanding.
- Temperature changes sampling. It does not update model weights.
- A PCA view loses information. Cosine neighbors use the full 64-number vectors.
- Token embeddings are not the same as contextual values after attention.
- Loss values from different vocabularies are not directly comparable.

## Deferred experiment

The student can later use one officially released CIA or FBI document. Keep this work separate from the essay baseline.

Before use, check the official URL, release status, redactions, OCR quality, privacy risks, and third-party copyright. Do not reconstruct redacted text. Change one experiment variable at a time.

## Remaining action

Do not submit the repository to the course portal unless the student asks for submission.
