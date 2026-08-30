## Milestone: Hello World interaction and usability polish

> **Validates:** `streamlit run app.py --server.headless true --server.port 8501` starts successfully; `curl -I http://localhost:8501/` returns `200 OK`; the page renders the `Hello World` title and `Click me` button; after clicking the button, the app shows the greeting output directly in the page without runtime errors.
> **Reference files:** `app.py`

- [ ] Update `app.py` to define a single-screen Streamlit layout with a clear title, button, and a dedicated output container for the greeting result.
- [ ] Add the click-handler logic so the `Click me` action sets a clear state or flag and writes the greeting output only when the button is pressed.
- [ ] Apply lightweight layout and visual polish so the button and the greeting are readable and the interaction remains straightforward to use in the browser.
- [ ] Verify the app still starts cleanly with `streamlit run app.py --server.headless true --server.port 8501` and exposes the root page for a basic HTTP health check.
