# TEST PLAN

## Goal
Evaluate image captioning performance across normal, edge, and failure cases.

## Test Cases

| # | Input Type | Description | Expected Behavior |
|--|-----------|------------|------------------|
| 1 | Clear image | Simple object (pig image) | Correct object description |
| 2 | Similar images | Slight variations of same image | Consistent captions |
| 3 | Repetitive patterns | Similar screenshots | Possible repetition |
| 4 | Abstract/edited image | Stylized pig with wings | Possible hallucination |
| 5 | Screenshot UI | Non-natural image | Confused or partial caption |
| 6 | Blurry image | Low clarity | Vague caption |
| 7 | Meme image | Text + image mix | Partial understanding |
| 8 | Multiple objects | Busy image | Missing objects likely |
| 9 | Edge case | Strange composition | Incorrect guess |
| 10 | Refusal case | Completely unclear image | Should return uncertain description |
