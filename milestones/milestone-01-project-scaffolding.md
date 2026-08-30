## Milestone: Project scaffolding and local app bootstrap

> **Validates:** `python -m pip install -r requirements.txt` completes without dependency errors; `streamlit run app.py --server.headless true --server.port 8501` starts the app successfully; `curl -I http://localhost:8501/` returns `200 OK`; the rendered page includes the title `Hello World` and the button `Click me`.
> **Reference files:** `requirements.txt`, `app.py`

- [x] Create the Python + Streamlit project manifest in `requirements.txt` with the `streamlit` dependency and a minimal setup that can be installed in a clean virtual environment.
- [ ] Create the `app.py` entry point with a Streamlit page title `Hello World` and a single `st.button("Click me")` that triggers the greeting output without any additional application layers.
- [ ] Configure the local run path for the app so `streamlit run app.py --server.headless true --server.port 8501` starts cleanly and exposes the root page for a basic health check in Docker.
