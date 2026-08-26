# Creative Control System

Use four internal control axes. Every value is clamped to `0–100`; an explicit user value overrides a Scene Profile default.

| Axis | Meaning | General default |
|---|---|---:|
| Abstraction | Distance from recognizable depiction toward relationships, rhythm, intervals, color roles, and negative space. `0` is highly concrete; `100` is strongly relational. | 60 |
| Creative Freedom | Design latitude that remains inside the source facts. Low values stay conservative; high values allow bolder offsets, mark character, and regrouping without inventing content. | 35 |
| Identity Preservation | Amount of identity cue retained for a meaningful person, landmark, or object. High values keep decisive silhouette, proportion, or cue; low values are suitable for anonymous rhythm or light. | Scene-dependent |
| Spatial Fidelity | Strictness of left/right, upper/lower, scale, intervals, overlap, orientation, axes, gravity, perspective, and spatial rhythm. | 85 |

## Natural-language mapping

Apply the following deltas to the active values, then clamp each result:

| User wording | Change |
|---|---|
| “更抽象一点” / “more abstract” | Abstraction `+15` |
| “稍微抽象一点” / “slightly more abstract” | Abstraction `+8` |
| “更写实” / “more literal” | Abstraction `-15` |
| “再接近原图一点” / “closer to the source” | Abstraction `-10`, Spatial Fidelity `+5` |
| “大胆一点” / “bolder” | Creative Freedom `+15` |
| “更克制” / “more restrained” | Creative Freedom `-15` |
| “更忠于原图” / “more faithful” | Spatial Fidelity `+10`, Creative Freedom `-10` |
| “人物要明显一些” / “make the person clearer” | Identity Preservation `+20` |
| “地标要看得出来” / “keep the landmark legible” | Identity Preservation `+15` |

Do not force ordinary users to configure axes. Resolve Scene Profile defaults first, apply natural-language deltas second, and record the resolved values in the working decision or manifest when local composition is used.
