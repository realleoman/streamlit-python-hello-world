## Milestone: Hello World interaction UI

> **Validates:** `streamlit run app.py --server.headless true --server.port 8501` starts successfully; `curl -I http://localhost:8501/` returns `200 OK`; the rendered page includes the `Hello World` title and `Click me` button; when the button is clicked, the page shows the greeting text `Hello World` without page reloads or extra screens; any runtime issue surfaces as a concise Streamlit error instead of a silent failure.
> **Reference files:** `requirements.txt`, `app.py`

- [x] Create the Streamlit page shell in `app.py` with a centered layout, a clear page title, and a single visible action button named `Click me` so the interaction remains deterministic and easy to extend.
- [ ] Add an explicit `show_hello` or equivalent `st.session_state` flag in `app.py` that is set only when the button is clicked so the greeting is rendered by a single, stable click path and not by hidden side effects.
- [ ] Implement the `st.button("Click me")` click handler in `app.py` to render the exact greeting text `Hello World` in-place on the same screen and keep the UI state straightforward for future one-screen enhancements.
- [ ] Add concise error surfacing around the button action in `app.py` so runtime problems display a short message without breaking the app or leaving the page in a confusing state.
- [ ] Verify the end-to-end interaction by starting the app with `streamlit run app.py --server.headless true --server.port 8501` and confirming the root page loads successfully before and after the click path.
