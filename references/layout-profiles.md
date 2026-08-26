# Layout Profiles

Choose a profile from scene facts, source orientation, dominant axis, subject location, visual center of gravity, and negative space. Selection is deterministic; never choose randomly. If no decisive trigger exists, use **Lower Editorial**.

| Canonical profile | Use when | Motif language | Typography |
|---|---|---|---|
| `lower-editorial` | Generic landscape, general street, or an ordinary scene without a stronger trigger | Lower-left optical grid, restrained horizontal relationship | Lower-left optical title |
| `wide-horizon` | Sea, lake, road, long horizon, long horizontal architecture, or strong horizontal rhythm | Broad lateral motif, restrained vertical height, generous side spacing | Lower editorial title block |
| `vertical-monument` | Pure Portrait, tower, tall building, or a decisive vertical subject/axis | Narrower vertical cue with editorial whitespace; never a poster icon | Calm centered title block |
| `centered-archive` | Centered subject, near symmetry, monumental composition, or calm archival feeling | Centered but optically imperfect motif | Centered title block |
| `sparse-object` | Still life, one object, minimal object scene, or generous negative space | Smaller motif, fewer marks, more silence | Restrained title with open margins |

The current `lower-left` compositor value remains a backward-compatible alias for `lower-editorial`. The current `bottom-center` value remains accepted as a legacy centered alias. New callers may use the canonical names or `auto` with scene facts.

The compositor maps each profile to explicit, bounded geometry. Motif and title must remain inside the panel, and omitted layout input must not alter the established Lower Editorial result.
