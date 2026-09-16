# Assignment 3 Plan

Plan date: September 16, 2026

Status: updated 48-eval work complete locally; publication still required
Repository: [Customer-LLM-Fundamentals-of-Agentic-AI](https://github.com/patronofalltrades/Customer-LLM-Fundamentals-of-Agentic-AI)

## September 16 assignment update

The instructor added four required 48-case result sets: starter untrained/trained
and expanded-corpus untrained/trained. The fixed eval suite must remain outside all
training inputs. The expanded corpus must target at least two extension categories,
and the submission must include a working interface with three real interactions.

The updated local work is complete:

| Experiment | Corpus | Final result | Coverage |
| --- | --- | ---: | ---: |
| Starter | Classroom only | 20 / 48 | 24 / 48 |
| Expanded | Classroom plus 109 grammar/opposites passages | 28 / 48 | 30 / 48 |

Both experiments ran all 48 cases before and after 3,000 training updates. The
expanded model scored 3/3 on grammar and 1/3 on opposites. Low scores and failures
remain valid evidence; improvement was not a grading threshold.

The old essay baseline below is supplemental. It predates the language-eval update.

## Objective

Use the supplied nanoGPT notebook to train a small language model from random weights. Use permitted text. Save the executed notebook and measured evidence. Explain how the model changes during training.

## Source files

- [Assignment document](https://docs.google.com/document/d/1MQ3YQl2ywWZF7W5_l_91FiIp7pTYPO_3viI2JVapRcc/edit?tab=t.0)
- [Starter repository](https://github.com/pepealonso95/custom-llm)
- [Pinned nanoGPT source](https://github.com/karpathy/nanoGPT/blob/3adf61e154c3fe3fca428ad6bc3818b27a3b8291/model.py)

The local file `ASSIGNMENT.md` preserves the instructor requirements. The student-authored files use Simplified Technical English.

## Student decisions

| Decision | Selected value |
| --- | --- |
| Corpus | Classroom corpus plus main essay prose |
| Essay | “The New World’s Bottleneck” |
| Training steps | 3,000 |
| Learning rate | `0.001` |
| Trace token | `bottleneck` |
| Device | Apple Silicon CPU |

The essay includes AI-assisted work. AI tools helped with brainstorming, outlining, editing, and some generated passages. The student directed and reviewed the final text.

## Prediction

Training loss and validation loss should decrease. The model should learn some relationships between essay terms. The generated text can remain repetitive because the classroom corpus is much larger than the essay corpus.

Low temperature should produce predictable text. High temperature should produce more varied text.

## Implementation steps

### Step 1 — Prepare the repository

1. Copy the starter notebook and pinned model source.
2. Preserve the nanoGPT license.
3. Create a local Python environment.
4. Install the required packages.

### Step 2 — Prepare the corpus

1. Download the public essay page.
2. Extract the title, headings, and main body.
3. Exclude citations, footnotes, URLs, navigation, image labels, and acknowledgements.
4. Save the extracted text as Markdown in `corpus/`.
5. Inspect the extracted text and warnings.

### Step 3 — Test the setup

1. Configure a 10-step test run.
2. Run the notebook in Jupyter.
3. Confirm that all cells finish.
4. Confirm that the notebook creates the expected result files.

The 10-step run is only a setup test. It is not the final experiment.

### Step 4 — Configure the baseline

1. Set `CORPUS = "classroom"`.
2. Set `TRAINING_STEPS = 3000`.
3. Set `LEARNING_RATE = 0.001`.
4. Keep the seed, split, evaluation panels, and generation settings fixed.
5. Record the prediction before training.

### Step 5 — Run the final experiment

1. Run all notebook cells in order.
2. Inspect the corpus and vocabulary.
3. Save the untrained measurements.
4. Train for 3,000 updates.
5. Save the halfway measurements.
6. Save the final measurements.
7. Save the inspection files and plots.

### Step 6 — Inspect the learning process

1. Compare training loss and validation loss.
2. Compare the step 0, step 1,500, and step 3,000 samples.
3. Trace `bottleneck` from text to token ID 102.
4. Compare its initial and final 64-number vectors.
5. Inspect one gradient and parameter update.
6. Compare next-token probabilities before and after training.
7. Compare temperatures 0.3, 0.8, and 1.2.

### Step 7 — Publish the evidence

1. Save the executed notebook with all outputs.
2. Copy the final result files to `results/essay-baseline/`.
3. Write the evidence-first README.
4. Test all local README links.
5. Confirm that GitHub renders the notebook and README.
6. Confirm public access while signed out.
7. Commit and push the final files.

## Final results

| Measurement | Result |
| --- | ---: |
| New essay passages | 184 |
| Combined unique passages | 4,816 |
| Training passages | 4,334 |
| Validation passages | 482 |
| Vocabulary size | 512 |
| Training unknown-token rate | 1.02% |
| Validation unknown-token rate | 1.61% |
| Completed updates | 3,000 |
| Training time | 19.19 seconds |
| Model parameters | 135,936 |

| Step | Training loss | Validation loss |
| ---: | ---: | ---: |
| 0 | 6.2454 | 6.2732 |
| 1,500 | 0.9090 | 1.1599 |
| 3,000 | 0.8691 | 1.2489 |

The model learned the corpus patterns. The validation loss increased after step 1,500. This result shows overfitting. The classroom patterns dominated the generated samples.

## Earlier baseline grading check

The assignment does not give a numerical point system. Use these dimensions to check the work.

| Dimension | Required evidence | Status |
| --- | --- | --- |
| Reproducibility | Executed notebook, configuration, timing, hardware, and result files | Complete |
| Experiment design | Corpus, permission, settings, prediction, split, and fixed controls | Complete |
| Model comparison | Untrained, halfway, and final samples, loss table, and plot | Complete |
| Token and embedding | Token ID and full initial and final vectors | Complete |
| Learning process | Loss, gradient, parameter update, and changed prediction | Complete |
| Attention and generation | Causal context, probabilities, sampling, and temperature | Complete |
| Honest interpretation | Validation comparison, limitation, and no broad claims | Complete |
| Next experiment | One controlled change and a predicted effect | Complete |
| Public submission | Public README, notebook, and working evidence links | Complete |

## Earlier proposed experiment

Change only the corpus mode to `folder`. Use only the cleaned essay. Keep the other settings fixed. This experiment can show whether corpus balance caused the classroom-style output.

Do not compare raw losses as a direct ranking. The vocabulary will change with the corpus.

## Deferred public-document experiment

The student can later test one officially released CIA or FBI document. Use a separate experiment. First check the official source, release status, redactions, OCR quality, privacy risks, and third-party copyright. Do not reconstruct redacted text.

## Submission state

The earlier baseline is public. The September 16 eval update is complete and
verified locally, but it has not yet been committed or pushed. After publication,
verify both executed notebooks, all four eval result sets, the transcript visual,
and every README link while signed out. Course-portal submission still requires a
separate student request.
