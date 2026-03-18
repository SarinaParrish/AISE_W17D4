# PIPELINE

## Flow

Image → BLIP Model → Caption Output

## Steps
1. Load image from folder
2. Pass image to HuggingFace pipeline
3. Generate caption
4. Print output

## Success Criteria
- Produces readable captions
- Identifies main object correctly

## Predicted Failures
- Hallucination (adds details not present)
- Repetition in output
- Poor performance on abstract images

## Fallback Behavior
- Return generic caption if uncertain