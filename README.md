# RA's NYC Birthday Bash

A responsive, buildless birthday-weekend itinerary for November 20–22, 2026.

## Design inspiration

The main visual reference is **Webagent 007 (2003)**, archived by Web Design Museum:

https://www.webdesignmuseum.org/flash-websites-in-the-early-00s/webagent-007-2003

Its layered Flash-era panels, metallic frames, cables, gold logo ornaments, and compact controls inspired this site's synthwave interpretation. The reference was used for visual direction; its original artwork was not extracted into the website.

## Development

Serve `dist/` with a static web server. The site uses HTML, CSS, and JavaScript; no build step is needed.

## Asset credits

No AI-generated imagery is included in the website. Layout, metallic frames, gold ornaments, cables, patterns, and question mark are custom code and SVG.

### Skyline Background

- Creator: FabinhoSC
- Source: https://opengameart.org/content/skyline-background
- License: [CC0](https://creativecommons.org/publicdomain/zero/1.0/)
- File: `dist/assets/city.png`
- Modifications: Unmodified example 03 from original 2021 archive

### Roller Skate

- Creator: Delapouite
- Source: https://game-icons.net/1x1/delapouite/roller-skate.html
- License: [CC BY 3.0](https://creativecommons.org/licenses/by/3.0/)
- File: `dist/assets/skate.svg`
- Modifications: Removed background and recolored foreground for synthwave palette.

### Martini

- Creator: Lorc
- Source: https://game-icons.net/1x1/lorc/martini.html
- License: [CC BY 3.0](https://creativecommons.org/licenses/by/3.0/)
- File: `dist/assets/cocktail.svg`
- Modifications: Removed background and recolored foreground for synthwave palette.

### Press Start 2P

By CodeMan38. SIL Open Font License 1.1.

https://fonts.google.com/specimen/Press+Start+2P

Full license: `dist/assets/font-license.txt`. Game-icons license: `dist/assets/game-icons-license.txt`.

## Content notes

Player colors are provisional. The skyline is decorative, not an image of the Airbnb. Exact address, reservations, and remaining itinerary details are pending.

### Munroe pixel sprite

Dog by inmenus, built upon Shepardskin and Hellkipz. CC0. The creator explicitly states no generative AI was used.

- Source: https://inmenus.itch.io/dog
- License: https://creativecommons.org/publicdomain/zero/1.0/
- Upstream: https://opengameart.org/content/german-shepherd-0 and https://opengameart.org/content/husky-sprites
- Files: `dist/assets/munroe-sheet.png` (original downloaded 360×228 sprite sheet) and `dist/assets/munroe-pixel.png` (idle standing frame, cropped with transparent margins trimmed).

Munroe portrait and connected nameplate: original hand-coded SVG artwork, drawn from the owner-provided dog photograph. No AI-generated image assets.

## Future improvements

### Optional entry screen

Explore an introductory “Enter” screen inspired by **Cyphen (1998)**, archived by Web Design Museum:

https://www.webdesignmuseum.org/exhibitions/cyphen-1998

This is a reference for a future iteration, not part of the current site. The immediate plan is to deploy the itinerary and collect feedback from RA on the weekend plans and placeholder content before deciding whether to add an entry screen.

## Social sharing previews

Open Graph and Twitter Card metadata are included in the initial HTML and use the production canonical URL: https://pythonidaer.github.io/nyc-bday-bash/

Cover: `dist/assets/social-preview-v1.png` (1200 × 630). Rebuild the cover and PNG browser icons with `python3 scripts/create-social-preview.py` (requires Pillow). The cover is rendered from code using the existing font and palette; no image generation is used. Font licensing remains as credited above.

Preview image: https://pythonidaer.github.io/nyc-bday-bash/assets/social-preview-v1.png

Social platforms may cache previews. Metadata supplies link previews where supported; it does not create an Instagram post or guarantee a thumbnail in every app.
