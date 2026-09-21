# Assignment 3 — Custom LLM: Class Brief

## One-minute overview

I trained two small nanoGPT language models from random weights using word and punctuation tokens. The model predicts the next token in a short context; it is not a general chatbot.

The assignment compared a starter-corpus control with an expanded corpus. The added teaching material targeted **grammar** and **opposites**, using 109 original passages that did not copy the provided evaluations.

## What I tested

The fixed 48-case language-evaluation suite stayed outside the training corpus. I ran every case before and after training for both experiments and saved case-level JSON/CSV evidence, free continuations, and separation audits.

| Run | All-case success | Scorable accuracy | Coverage |
| --- | ---: | ---: | ---: |
| Starter, untrained | 18.75% | 37.50% | 50.00% |
| Starter, trained | 41.67% | 83.33% | 50.00% |
| Expanded, untrained | 10.42% | 16.67% | 62.50% |
| Expanded, trained | 58.33% | 93.33% | 62.50% |

## Main finding

The expanded corpus increased vocabulary coverage and made grammar and opposites measurable. The trained expanded model answered grammar correctly in all three cases, but only one of three opposites cases. More vocabulary made evaluation possible; it did not guarantee that the intended relationship was learned.

## Important limitation

Eighteen expanded-model cases remained out of vocabulary: negation, references, sequence, spatial relations, everyday knowledge, and categories/analogies. These cases receive zero in the all-case metric by design. The model also produces awkward free continuations, even when it selects the right answer among four choices.

## Evidence to show in class

- [Repository and executed notebooks](https://github.com/patronofalltrades/Create-an-LLM-Fundamentals-of-Agentic-AI)
- [Hosted embedding explorer](https://patronofalltrades.github.io/Create-an-LLM-Fundamentals-of-Agentic-AI/)
- [Literal terminal interaction GIF](assets/chat-terminal-recording.gif)
- [Full terminal recording](assets/chat-terminal-recording.mov)
- [Recorded interaction transcript](../results/expanded-evals/chat-terminal-recording-20260921.json)

## Discussion prompts

1. Why are all-case success and scorable accuracy different metrics?
2. Why is it misleading to call the 48 fixed public cases an unseen generalization test?
3. Why can a constrained four-choice score be high while free text remains poor?
4. What would a valid next experiment change? Keep architecture, seed, learning rate, and test suite fixed; add original non-eval examples for one unscorable category; retrain a fresh model; compare coverage, scores, and continuations.

## Submission

Assignment 3 was submitted through bCourses as an online URL pointing to the public GitHub repository above.
