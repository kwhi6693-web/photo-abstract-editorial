# Legacy Skill Baseline

## Evidence observed before revision

The existing Skill and its public artifacts demonstrate the failures the strict-fidelity revision must prevent:

- The workflow never names or invokes an image-generation tool, and GitHub Issue #1 asks whether the Skill uses ChatGPT image generation or a local drawing tool.
- The repository contains completed composites but no standalone source photographs or manifests, so preservation of the photo region cannot be verified.
- `case-1.jpg` and `case-3.jpg` contain color swatches forbidden by the prompt.
- `case-4.jpg` renders the misspelled title `A Pagoda in Silenc` and extra Chinese text.
- `case-7.jpg` contains a Chinese wordmark/logo and no required English title.
- `case-8.jpg` contains a location-description subtitle forbidden by the prompt.
- README says there are five examples while seven files exist and six are displayed.

## Baseline scenarios

| Scenario | Required behavior | Legacy evidence of failure |
|---|---|---|
| User supplies one local photo | Use a named image tool with the photo explicitly labeled | No tool or image-role instruction exists |
| Final photo must remain unchanged | Preserve or deterministically reconstruct and compare the photo region | No source/output pair or validator exists |
| Title must be exact | Render exact local typography | `Silenc` typo appears in a published example |
| No extra text or symbols | Reject swatches, logos, location labels, and extra copy | Five published examples violate at least one rule |
| Final panel must be clean | Validate a uniform background and inspect the motif | No quality gate or retry limit exists |

These raw published artifacts serve as the RED baseline. They are not positive visual references for the revised Skill.
