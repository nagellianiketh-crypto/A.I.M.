# Allied Algorithms — A.I.M.

A.I.M. (Allied Invasive Mapping) is the browser frontend for the Multiflora Rose identification and reporting project.

## One-service Render deployment

The production website and API run together as **one Render web service**.

- Frontend source: `index.html` in this repository.
- Production frontend copy: `frontend/index.html` in the backend repository.
- Backend and Render deployment: [Allied-Algorithms-AI-Plant-Identifier](https://github.com/nareddyt1-cell/Allied-Algorithms-AI-Plant-Identifier), branch `backend`.

The FastAPI application serves the website at `/` and its API at `/scan`, `/consent`, `/sightings`, `/sightings/public`, and `/consent/revoke`. The frontend calls these same-origin paths directly. There is no separate frontend Render service and no `PLANT_IDENTIFIER_API_URL` proxy setting.

**Important for future frontend edits:** after changing `index.html` here, copy the same contents to `frontend/index.html` in the backend repository's `backend` branch. Render is connected only to that backend repository/branch, so that is the commit that deploys the combined application.

## Deploy configuration

Use the existing Render service defined by the backend repository's root `render.yaml`. Do not create a second Render service from this repository.

The backend requires `PLANTNET_API_KEY` in Render. SMTP settings are optional and enable environmental-group email notifications. The backend Blueprint keeps SQLite on its persistent disk at `/var/data/consent.db`; keep that disk attached so sightings survive restarts. Render persistent disks require a paid web-service plan.

## Website functionality

- Upload a JPEG, PNG, or WebP image (maximum 10 MB) for Pl@ntNet identification.
- Display identification candidates and Prompt A net-cutter guidance.
- Offer Prompt B with separate opt-ins for public map display and environmental-group sharing.
- Request browser geolocation only after the user explicitly chooses to submit a sighting.
- Submit coordinates only after browser location permission and consent.
- Allow consent revocation.
- Display active, non-revoked, map-opted-in community sightings using approximate public coordinates.

## Current prototype limitations

The backend uses Pl@ntNet; a separate trained ViT classifier is not integrated. Consent IDs are bearer capabilities rather than authenticated user accounts. Review the backend README for privacy and production-readiness limitations.

## Local preview

You can preview the static interface with:

```bash
python -m http.server 8000
```

That previews the page only. To exercise scanning, consent, and map API calls locally, run the FastAPI backend and serve this page from its `frontend/index.html` path.
