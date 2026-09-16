# Assignment 3 — Creating an LLM

This repository contains my completed experiment with the course-supplied nanoGPT notebook. I trained a 135,936-parameter word-token transformer from scratch on the classroom corpus plus the main prose of my published essay, [“The New World’s Bottleneck: Jevons, Baumol, and Who Captures the Gains from AI”](https://hanif.info/posts/the-new-worlds-bottleneck.html).

The goal was not to create a general chatbot. It was to trace how a corpus becomes tokens, IDs, 64-number embedding vectors, next-token probabilities, loss, gradients, weight updates, and generated text.

- [Executed notebook](custom_llm.ipynb)
- [Assignment plan](ASSIGNMENT_PLAN.md)
- [Durable assignment context](assignment-context.md)
- [Complete selected evidence](results/essay-baseline/)
- [Offline embedding viewer](embedding-viewer.html) — load [`checkpoint.json`](results/essay-baseline/checkpoint.json)

## Corpus, permission, and choices

I used `CORPUS = "classroom"`, combining the supplied synthetic teaching sentences with one added Markdown file. The file contains the essay title, headings, and body. It excludes citations, footnotes, URLs, navigation, image labels, and acknowledgements.

The essay was directed and edited by me. AI tools assisted with brainstorming, outlining, editing, and generating some passages. I reviewed the final text and had already published it publicly. The corpus therefore represents the final human-directed, AI-assisted document; it is not evidence of my unaided writing style.

| Choice | Value | Reason |
| --- | --- | --- |
| Corpus | Classroom corpus plus permitted essay prose | The classroom patterns make learning inspectable, while the essay adds vocabulary around AI, constraints, automation, and demand. |
| Training steps | 3,000 | The assignment’s recommended meaningful baseline; the separate 10-step run was only a setup check. |
| Learning rate | `0.001` | The recommended starting rate, with warmup and cosine decay. |

An excessively large learning rate could overshoot useful weights or destabilize loss. An excessively small rate could fail to learn enough within the budget.

### Extraction and split

The Markdown extraction produced no warnings. [`corpus_manifest.json`](results/essay-baseline/corpus_manifest.json) records the source filename, hash, preview, and counts.

| Corpus fact | Measured value |
| --- | ---: |
| Essay characters | 16,620 |
| New unique essay passages | 184 |
| Classroom passages before combined deduplication | 6,360 |
| Combined unique passages | 4,816 |
| Duplicate passages removed | 1,728 |
| Training passages | 4,334 |
| Validation passages | 482 |

The split is 90/10 by deduplicated passage, not source file. Validation passages do not update weights, but essay passages can occur on both sides. This tests held-out passage combinations, not generalization to an unseen source.

The vocabulary contained 512 entries: 509 retained training types plus `<UNK>`, `<BOS>`, and `<EOS>`. The training corpus contained 1,022 distinct types before truncation. Training unknown-token rate was **1.02%** and held-out unknown-token rate was **1.61%**, both below the notebook’s 5% warning threshold. See [`vocabulary_report.json`](results/essay-baseline/vocabulary_report.json).

## Prediction written before training

I predicted that training and held-out loss would fall. I expected samples to increasingly combine *bottleneck*, *constraint*, *automation*, *demand*, and *AI* plausibly, although the model might remain repetitive, fragmented, or source-like. I also expected lower-temperature output to be more predictable and higher-temperature output to be more varied.

## Actual run

| Run fact | Actual value |
| --- | --- |
| Status | Completed without interruption or notebook errors |
| Optimizer updates | 3,000 |
| Training-loop elapsed time | 19.19 seconds |
| Device and hardware | CPU; Apple Silicon macOS arm64 |
| Python / PyTorch | Python 3.9.6 / PyTorch 2.8.0 |
| Parameters | 135,936 |
| Architecture | 2 blocks, 4 heads, 64D embeddings, 48-token context |
| Batch size / seed | 32 passages / 42 |
| Evaluation panels | 20 training and 20 validation passages |

Exact configuration and timing are in [`config.json`](results/essay-baseline/config.json) and [`training_summary.json`](results/essay-baseline/training_summary.json). Full training rows are in [`training.csv`](results/essay-baseline/training.csv).

## Loss evidence

![Training and validation loss](results/essay-baseline/training_curves.svg)

| Step | Training-panel loss | Validation-panel loss |
| ---: | ---: | ---: |
| 0 | 6.2454 | 6.2732 |
| 1,500 | 0.9090 | **1.1599** |
| 3,000 | **0.8691** | 1.2489 |

These fixed panels average all non-padding next-token targets. They are small estimates, not full-corpus loss. Complete values are in [`history.json`](results/essay-baseline/history.json).

Both losses improved dramatically from step 0. From step 1,500 to 3,000, however, training loss improved while validation loss worsened. That divergence is evidence of overfitting after the halfway point.

## Untrained, halfway, and final samples

Generation settings and the random seed stayed fixed. I kept every saved sample, including the garbled untrained text.

### Step 0 — untrained

```text
growing four price what someone southeast 000 bond week hold bottlenecks day first tutor replace teacher kept our dentist they're lesson grew developer doesn't language bus 003 cheap nurse doctor quadrant productivity
test volume operations management it productivity called demand hour what system efficiency competing needed higher do times enough harvest so cut payment consumption iese over went kept hold constraint right educator standing
doing application leisure advance office checking five power keep replaced than paradox compared interest power fall my expects disappear barely factory learning 000 and 1930 sitting as code against update teaching capital
development both as 2000 business well growing barely always seven 700 purchase operations jobs 1865 gain efficient will increased second technology % whose mango speed fulfillment expects 65 think lecturer booking leisure
```

### Step 1,500 — halfway

```text
our office has a question about the new platform and update .
the new teacher was mentioned in the lesson report yesterday .
the different lecturer was mentioned in the learning report yesterday .
today the kitchen focused on juice and the new pear .
```

### Step 3,000 — final

```text
our office has a question about the new platform and update .
the new teacher was mentioned in the lesson report yesterday .
the different lecturer was mentioned in the learning report yesterday .
today the kitchen focused on juice and the new pear .
```

The model changed from random sequences into grammatical classroom templates, but halfway and final samples were identical. The essay was only 184 of 4,816 unique passages, so classroom patterns dominated unconditional generation. Full files: [untrained](results/essay-baseline/samples/step_0000.txt), [halfway](results/essay-baseline/samples/step_1500.txt), and [final](results/essay-baseline/samples/step_3000.txt).

## One word from text to ID to vector

The word **`bottleneck`** was retained and assigned token ID **102**. The ID is an integer lookup key; it selects row 102 from the token-embedding table.

Initial 64-number vector:

```text
[0.035419, -0.024861, -0.033798, 0.016063, 0.030064, 0.006256, 0.003740, -0.026716, 0.006811, -0.019389, 0.003402, -0.018591, 0.009643, -0.000871, -0.002581, -0.016245, -0.003216, -0.016645, -0.007848, 0.010776, 0.007726, 0.021869, 0.009092, -0.030755, 0.003980, -0.020058, 0.009821, 0.036219, 0.011011, 0.023682, -0.002374, 0.066848, 0.012474, 0.004746, 0.020280, -0.013166, 0.000638, -0.017028, 0.031372, -0.009318, 0.022383, -0.055197, -0.003421, 0.043838, -0.005655, -0.012928, 0.013297, 0.011505, 0.009411, -0.001589, 0.040475, 0.001756, -0.024022, 0.006817, 0.003673, 0.027728, -0.004083, -0.028540, 0.031490, -0.028373, -0.036345, -0.007140, -0.012994, 0.024005]
```

Final 64-number vector:

```text
[0.068656, 0.082031, -0.034321, 0.033582, 0.090589, -0.067067, -0.006640, -0.126530, 0.076109, -0.034191, -0.072049, -0.040752, -0.032658, -0.082250, -0.032250, -0.074602, -0.012225, 0.138816, -0.015833, -0.031648, 0.005062, 0.018145, -0.066763, -0.000484, 0.031893, -0.041422, 0.097606, -0.120253, -0.025560, 0.021735, -0.121269, 0.056348, -0.022233, 0.068526, -0.039007, -0.032880, -0.017601, -0.057959, 0.085169, 0.044746, 0.089640, -0.091771, -0.023619, -0.013487, -0.108967, 0.005416, 0.084398, -0.002341, 0.179212, 0.056590, 0.141069, -0.023122, 0.095388, -0.169652, 0.047897, 0.029745, 0.095627, -0.029272, 0.145983, 0.002309, -0.026448, 0.087856, -0.049736, 0.059411]
```

The vector moved by an L2 distance of about **0.554**. Before training, its closest cosine neighbors were random words such as `me`, `as`, and `worth`. After training, they included **`constraint` (0.698), `robots` (0.626), `same` (0.612), `demand` (0.591), and `matrix` (0.567)**. Those relationships match repeated essay contexts but do not prove general semantic understanding. See [`inspection.json`](results/essay-baseline/inspection.json) and [`checkpoint.json`](results/essay-baseline/checkpoint.json).

## Loss, gradient, and one real update

Cross-entropy loss penalizes low probability on the observed next token. Backpropagation calculates how each parameter contributed to loss. AdamW then uses gradients, momentum, adaptive scaling, weight decay, and the current learning rate to update weights.

For coordinate 0 of the `bottleneck` embedding during the first update:

| Measurement | Value |
| --- | ---: |
| Parameter before | 0.0354193784 |
| Gradient | 0.0046224012 |
| Warmup learning rate | 0.0000100000 |
| Parameter after | 0.0354093760 |

The parameter decreased slightly. Its change is not simply `learning rate × gradient` because AdamW also uses optimizer state and weight decay.

## Next-token probabilities

For the prefix **“the bottleneck”**, the untrained distribution was nearly flat. Its highest entries included `bottleneck` at 0.402%, `keep` at 0.297%, and `reviewed` at 0.294%.

After training, probability concentrated on essay-like continuations: `didn't` at **7.386%**, `moved` at **4.807%**, `engineers` at **2.014%**, `shifts` at **1.946%**, and `rather` at **1.946%**. This demonstrates changed predictions rather than document retrieval.

## Attention, context, and generation

The model combines token and position embeddings, then passes them through two transformer blocks. Causal self-attention lets each position weight earlier positions inside the 48-token window. The causal mask prevents it from seeing future tokens. Feed-forward layers and residual connections transform the contextual representation, and final logits become probabilities through softmax.

Generation samples one next-token ID, appends it to the context, and repeats. It does not search the essay or copy a stored response. The vocabulary converts IDs back into words and punctuation.

## Temperature comparison

The start token, sampling seed, model weights, and procedure stayed fixed. Temperature changed only how sharply existing probabilities were sampled; it did not retrain the model.

| Temperature | Saved result |
| ---: | --- |
| 0.3 | All four samples matched the final baseline samples. |
| 0.8 | All four samples again matched the final baseline samples. |
| 1.2 | The first three matched; the fourth changed from “juice and the new pear” to “system and the new website.” |

The limited variation suggests that classroom continuations were sharply favored for this seed. The complete twelve outputs are in [`temperature_comparison.json`](results/essay-baseline/temperature_comparison.json).

## What I learned

The prediction was **partially supported**:

- Training and held-out loss both fell dramatically from step 0.
- The `bottleneck` embedding developed essay-related neighbors, and the prefix produced essay-like next-token probabilities.
- Validation loss worsened after step 1,500, indicating overfitting by the final checkpoint.
- Samples became grammatical but stayed in the much larger classroom distribution.
- Temperature changed little because the learned distribution was strongly peaked for the fixed seed.

The central limitation is **corpus imbalance**: 184 essay passages were mixed with thousands of synthetic classroom passages. The model learned measurable essay associations without making them prominent in unconditional samples. It cannot demonstrate broad knowledge or generalization beyond short patterns in this narrow corpus.

### Proposed controlled next experiment

Change only the corpus mode to `CORPUS = "folder"`, keeping the cleaned essay, 3,000 steps, learning rate, seed, architecture, and generation settings fixed. The essay has 184 unique passages, above the folder-only minimum of 100. I predict more essay-themed samples and stronger related probabilities, with greater overfitting risk. Because the vocabulary would change, raw loss values should be interpreted within each run rather than used to rank the corpora directly.

A later Friday experiment may instead use one officially released, substantially unredacted CIA or FBI analytical document. It is deferred until the exact document’s release status, OCR quality, privacy implications, and third-party copyright are checked.

## Reproduce and inspect

1. Create a Python environment and install `requirements.txt`.
2. Place the permitted essay Markdown in `corpus/`. It is Git-ignored; the public source and extraction boundary are documented above, and the exact extracted training text is preserved in [`corpus.txt`](results/essay-baseline/corpus.txt).
3. Open `custom_llm.ipynb` in Jupyter and run all cells from the top.
4. Keep `CORPUS = "classroom"`, `TRAINING_STEPS = 3000`, and `LEARNING_RATE = 0.001` to reproduce this baseline.
5. Inspect the notebook outputs and [`results/essay-baseline`](results/essay-baseline/).
6. Open `embedding-viewer.html` locally and load `results/essay-baseline/checkpoint.json`.

The notebook uses the pinned nanoGPT source at commit `3adf61e` under the included [MIT license](NANOGPT_LICENSE). No pretrained weights, external model API, GPU, backend, or deployment service was used.
