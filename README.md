# Allied Algorithms — A.I.M.

A.I.M. (Allied Invasive Mapping) is the website interface for the Multiflora Rose identification and reporting project.

## Website deployment (Render)

This repository includes `render.yaml` for the website service. In Render, create a Blueprint from this repository and deploy the `allied-algorithms-aim-website` web service.

After the backend has been deployed, set the website service environment variable:

- `PLANT_IDENTIFIER_API_URL`: the backend service's base URL, for example `https://your-backend-name.onrender.com` (no trailing slash).

The website uses a same-origin `/api` proxy, so the browser does not need direct cross-origin access to the backend.

## Backend

The backend is maintained in [Allied-Algorithms-AI-Plant-Identifier](https://github.com/nareddyt1-cell/Allied-Algorithms-AI-Plant-Identifier). Its `backend` branch includes a Render Blueprint (`render.yaml`) for the FastAPI service.

Deploy that repository separately. The backend Blueprint currently requests a persistent disk for its SQLite database. Render persistent disks require a paid web service; a Free web service cannot attach one. Do not remove persistent storage if you need sightings to survive restarts.

Set the backend's `PLANTNET_API_KEY` environment variable in Render. Keep the key private; do not put it in website JavaScript or commit it to GitHub.

## Website functionality

- Upload a JPEG, PNG, or WebP image to the backend `POST /scan` endpoint.
- Display identification candidates and Prompt A cutter guidance returned by the backend.
- Offer Prompt B with separate opt-ins for map display and environmental-group sharing.
- Request browser geolocation only after the user clicks to continue and confirms the plant.
- Submit consent and coordinates to the backend only after browser location permission is granted.
- Allow the user to revoke consent.
- Display a marker on the map when map display was selected.

## Current backend limitations

The backend currently uses Pl@ntNet for identification; a separate trained ViT model is not integrated in the code inspected. Environmental-group sharing is recorded as authorized but email/notification delivery is not implemented. The current sightings endpoint returns sightings associated with the submitted consent ID, not a public, community-wide dataset. The map on this website therefore shows the active user's consent-authorized sighting only.

The backend repository is currently separate from this website repository. Its maintainer must deploy or update it; this website repository cannot change the backend's GitHub files.
