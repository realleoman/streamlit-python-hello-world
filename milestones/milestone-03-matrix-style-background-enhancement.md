## Milestone: Matrix-style background enhancement

> **Validates:** `streamlit run app.py --server.headless true --server.port 8501` starts successfully; `curl -I http://localhost:8501/` returns `200 OK`; the page renders the `Hello World` title and `Click me` button; after the button is clicked, the page shows the greeting and adds a matrix-like animated background layer behind the content without covering text or blocking the button.
> **Reference files:** `app.py`, `requirements.txt`

- [ ] Update `app.py` to keep the Hello World interaction deterministic by guarding the display state behind a single, explicit flag set only after the button click.
- [ ] Add a lightweight matrix-style background effect in `app.py` that activates only after the greeting appears and uses inline CSS or Streamlit styling to keep content readable.
- [ ] Ensure the background effect does not obscure text, buttons, or the primary greeting and that the screen remains easy to extend for future UI tweaks.
- [ ] Re-run the app start check with `streamlit run app.py --server.headless true --server.port 8501` and confirm the root page remains healthy under HTTP.
