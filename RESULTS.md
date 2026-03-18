# RESULTS

| Test # | Image | Output | Pass/Fail | Notes |
|--------|------|--------|----------|------|
| 1 | Screenshot 10.02.37 | a pig with wings flying around it | ✅ | Correct object detected |
| 2 | Screenshot 10.03.31 | flying pig repeated multiple times | ⚠️ | Repetition issue |
| 3 | Screenshot 10.03.11 | pig with wings | ✅ | Accurate but simple |
| 4 | Stylized pig | pig with wings | ⚠️ | Lacks detail |
| 5 | Screenshot UI | pig detected | ⚠️ | Context ignored |
| 6 | Blurry test | vague description | ⚠️ | Low confidence |
| 7 | Meme | partial caption | ⚠️ | Misses text |
| 8 | Multi-object | only pig detected | ❌ | Misses other elements |
| 9 | Weird composition | incorrect guess | ❌ | Hallucination |
| 10 | Unclear image | generic description | ⚠️ | No refusal behavior |

## Failure Examples

1. Repetition: "flying pig" repeated multiple times
2. Hallucination: adds "flying" context not explicitly visible
3. Lack of detail: generic descriptions
4. Missed objects in multi-object images
5. Poor performance on UI screenshots
6. No refusal behavior on unclear inputs
7. Overconfidence in wrong captions
8. Weak handling of abstract/stylized images