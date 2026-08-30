# Deployment notes for the Streamlit Hello World app

## Build configuration
- Dockerfile: `./Dockerfile`
- Base image: `python:3.12-slim`
- Install step: `python -m pip install --upgrade pip && python -m pip install -r requirements.txt`
- Streamlit is started with `streamlit run app.py --server.headless true --server.port 8501 --server.address 0.0.0.0`

## Environment variables
- `STREAMLIT_SERVER_HEADLESS=true`
- `STREAMLIT_SERVER_PORT=8501`
- `STREAMLIT_SERVER_ADDRESS=0.0.0.0`

## Port mapping
- Host `6261` -> container `8501` (`http://localhost:6261`)
- The app is expected to respond on the root path `/` with a `200 OK` status after startup.

## Docker Compose configuration
- Service name: `app`
- Build entrypoint: local Dockerfile in the repo root.
- Health check: `curl -fsS http://localhost:8501/ >/dev/null || exit 1`
- Playwright helper service is configured as `playwright` using `mcr.microsoft.com/playwright:v1.52.0-noble` and shares the same Docker network with the `app` service.

## Startup sequence
1. `docker compose down --remove-orphans`
2. `docker compose build`
3. `docker compose up -d`
4. Wait for the `app` service health check to report healthy before using the site.

## Health check endpoint
- `GET http://localhost:6261/`
- Expected page title: `Hello World`
- Expected action button text: `Click me`

## Known gotchas and fixes discovered during validation
- Because the app runs in a container, Streamlit must bind to `0.0.0.0` instead of the default localhost-only address.
- The host port is intentionally isolated to `6261` to avoid collisions with other local Stack projects.
- A `.dockerignore` file is required so the Docker build context stays small and does not accidentally include local Node or virtual environment artifacts.
- The app uses a single-page Streamlit UI; no database or extra services are required for the current milestone.
- `curl` is not installed in the base Python slim image, so the app healthcheck would fail unless `apt-get install curl` is added to the Dockerfile before `docker compose up`.
- The Playwright helper container uses a bundled browser version that matches `@playwright/test` 1.52.0 exactly. A caret version like `^1.52.0` resolves to a newer library that cannot launch the image's browser binaries, so pin the dependency to `1.52.0` in `e2e/package.json`.
- The app root works at `http://localhost:6261/` but the HTML shell does not include the final rendered text directly; verify the visible UI with Playwright instead of checking raw page source alone.
