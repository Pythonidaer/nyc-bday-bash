# From Web Design Museum to RA’s NYC Birthday Bash

## Purpose

A birthday-weekend itinerary for ten friends and Munroe in NYC, November 20–22, 2026. The experience borrows the visual language of early-2000s Flash sites and character-selection screens: dense panels, metallic frames, cables, sharp tabs, pixel lettering, and bright interface accents.

## Design process

1. **Historical reference.** Johnny selected Webagent 007 (2003) from Web Design Museum: https://www.webdesignmuseum.org/flash-websites-in-the-early-00s/webagent-007-2003. We studied the layered panels, gold logo ornaments, industrial borders, tubing, calendar, and compact media controls. The reference informed the composition; its artwork was not extracted for the website.
2. **Synthwave moodboard.** AI-generated concept images explored replacing red/black/electric blue with hot pink, cyan, purple, and softer character colors. Those images served as visual references, not shipped image assets.
3. **Content mapping.** The hero became a ten-person character grid with initials; the featured panel became Home Base; lower panels became the November calendar, Xanadu skating, art and cocktails, and the music-video side quest. Munroe received a companion nameplate.
4. **Working implementation.** Buildless HTML, CSS, and JavaScript replaced the historical Flash interface. CSS handles layout, stripes, tabs, colors, textures, and the question mark. Custom SVGs provide metallic frames, cables, gold ornaments, and small interface icons. Press Start 2P supplies the pixel lettering.
5. **Asset sourcing.** Existing licensed icons and a skyline supplied specific illustrations. We recolored icons and composed them with CSS backgrounds and effects. A downloaded dog sprite was tried first; a custom pixel portrait based on Johnny’s photograph later replaced it.
6. **Iteration.** We adjusted armor framing, saturation, larger initials, RA’s inset birthday banner, the connected Munroe plaque, the translucent logo box and tilted ornaments, and alignment and spacing. Content was simplified as the design developed.
7. **Responsive behavior.** The main layout stacks at 960px; the character grid keeps square tiles and reduces columns at smaller widths. Home Base puts its image above the details on mobile/tablet. Modals provide details without permanently enlarging the dashboard.
8. **Interactions.** Character and itinerary modals, Home Base details, nearby food/bar lists with map links, and user-initiated Plaza Radio playback were added. Restaurant lists were transcribed from supplied images; they have not been independently fact-checked for current operation, addresses, or recommendations.

## Assets actually used

| Asset | Origin and author | License / changes | Local file |
|---|---|---|---|
| Home Base skyline | **Skyline Background**, FabinhoSC — https://opengameart.org/content/skyline-background | Recorded as CC0 in the project credits. Unmodified example 03 from the original 2021 archive. Decorative skyline, not a verified depiction of NYC or the Airbnb. The source page could not be re-fetched during this documentation review. | `dist/assets/city.png` |
| Roller skate | Delapouite — https://game-icons.net/1x1/delapouite/roller-skate.html | CC BY 3.0. Background removed; foreground recolored cyan. CSS adds pink/cyan shadows and the surrounding retro scene. | `dist/assets/skate.svg` |
| Cocktail | **Martini**, Lorc — https://game-icons.net/1x1/lorc/martini.html | CC BY 3.0. Background removed; foreground recolored pink. CSS supplies shadows and the surrounding scene. | `dist/assets/cocktail.svg` |
| Pixel font | **Press Start 2P**, CodeMan38 — https://fonts.google.com/specimen/Press+Start+2P | SIL Open Font License 1.1. Local license retained. | `dist/assets/press-start.ttf`, `font-license.txt` |
| Current Munroe portrait | Custom SVG code based on the owner-provided photograph | Pixel-grid portrait using tan/cream fur, white blaze, and blue eye. Assistant-authored SVG, not an image-generator output. | `dist/assets/munroe-portrait.svg` |
| Frames, ornaments, cables | Custom assistant-authored SVG code | Designed to approximate the reference’s industrial aesthetic; not downloaded from a metal-frame asset pack. | `armor-frame.svg`, `nameplate.svg`, `munroe-frame.svg`, `fin.svg`, `cables.svg`, `grit.svg` in `dist/assets/` |
| Small icons | Custom inline SVG and CSS | Person silhouette, calendar icons, Expand arrow, radio controls, and status dot. | `dist/index.html`, `dist/style.css`, `dist/app.js` |

The skate and cocktail are **SVG illustrations, not emoji and not custom-drawn original shapes**. Their original creators are credited above. They are scalable vector silhouettes rather than true pixel-art sprites. The website contains no image-generator-produced bitmap assets; some custom SVG/code was authored by the assistant, so this should not be described as having no AI assistance.

CC BY 3.0: https://creativecommons.org/licenses/by/3.0/
CC0: https://creativecommons.org/publicdomain/zero/1.0/
Game-icons license copy: `dist/assets/game-icons-license.txt`.

## Earlier dog asset, now superseded

We initially used **Dog by inmenus**, based on Shepardskin and Hellkipz:

- https://inmenus.itch.io/dog
- https://opengameart.org/content/german-shepherd-0
- https://opengameart.org/content/husky-sprites

Project credits record CC0 and the creator’s statement that no generative AI was used. The downloaded sheet and cropped standing frame remain as `munroe-sheet.png` and `munroe-pixel.png`, but the current interface and modal reference `munroe-portrait.svg`. Keep this distinction clear when listing active credits versus historical experiments.

## Resources saved for future exploration — not used in the current interface

- **Stealthix Pipes Tileset:** https://stealthix.itch.io/pipes-tileset — 32×32 pipe tiles, CC0; the page explicitly states no generative AI was used. Our current tubing is custom SVG, not this pack.
- **Cyberpunk pixel art collection:** https://opengameart.org/content/cyberpunk-pixel-art-collection — collection to explore; check each individual asset’s license.
- **Free drinks / pixel-art assets:** https://itch.io/game-assets/free/tag-drinks/tag-pixel-art — discovery page, not a single asset or shared license.
- **Kenney UI Pack: Sci-Fi:** https://kenney.nl/assets/ui-pack-sci-fi — possible future interface resource; not used. This page could not be re-fetched during this review; verify availability and licensing before adopting assets.

The originally pasted drinks/Kenney URL combined two URLs accidentally. They are separated above and tracking parameters removed.

## GitHub Pages handoff — preparation only

Target repository: https://github.com/Pythonidaer/nyc-bday-bash

On November 5, 2026, the GitHub contents API reported the repository was empty. Johnny reported Pages was configured to deploy through GitHub Actions; no workflow file was available to inspect yet. Nothing was pushed to that repository as part of this documentation task.

The app is static: upload/deploy **the contents of `dist/`**. There is no dependency installation or build step required. Paths to CSS, JS, fonts, and images are relative, suitable for a GitHub Pages project subpath.

Before the production push:

- Include source, this document, README, and asset/license credits.
- Add a Pages Actions workflow that checks JavaScript syntax, uploads `dist` as the Pages artifact, and deploys with `pages: write` and `id-token: write` permissions.
- Keep the Sites-specific `.openai/hosting.json` out of the Pages artifact.
- Test the public project-subpath URL on desktop and mobile, including all modals, map links, fonts, and user-triggered HTTPS radio playback.
- Review birthday-trip content before making it public; the exact accommodation address is currently a placeholder.
- Preserve artist attribution in README and ship the retained license files. Confirm the skyline source/license record before release.

Production push and GitHub Pages deployment remain pending Johnny’s remaining questions.
