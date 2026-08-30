import importlib
import os
import sys
import types

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)


def load_app(monkeypatch, click_result=False):
    calls = []
    session_state = {"show_greeting": False}

    def fake_button(label):
        calls.append(("button", label))
        if click_result:
            session_state["show_greeting"] = True
        return click_result

    fake_streamlit = types.SimpleNamespace(
        set_page_config=lambda **kwargs: calls.append(("set_page_config", kwargs)),
        markdown=lambda *args, **kwargs: calls.append(("markdown", args, kwargs)),
        title=lambda *args, **kwargs: calls.append(("title", args, kwargs)),
        button=fake_button,
        success=lambda *args, **kwargs: calls.append(("success", args, kwargs)),
        session_state=session_state,
    )
    monkeypatch.setitem(sys.modules, "streamlit", fake_streamlit)
    sys.modules.pop("app", None)
    app_module = importlib.import_module("app")
    return app_module, calls


def test_app_sets_the_button_and_waits_for_user_click(monkeypatch):
    _, calls = load_app(monkeypatch)

    button_calls = [call for call in calls if call[0] == "button"]
    title_calls = [call for call in calls if call[0] == "title"]
    page_title_calls = [call for call in calls if call[0] == "set_page_config"]

    assert page_title_calls and page_title_calls[0][1]["page_title"] == "Hello World"
    assert button_calls and button_calls[0][1] == "Click me"
    assert not title_calls


def test_clicking_button_displays_the_greeting(monkeypatch):
    _, calls = load_app(monkeypatch, click_result=True)

    success_calls = [call for call in calls if call[0] == "success"]
    title_calls = [call for call in calls if call[0] == "title"]
    assert success_calls and success_calls[0][1][0] == "Hello World"
    assert title_calls and title_calls[0][1][0] == "Hello World"


def test_app_enables_matrix_style_after_click(monkeypatch):
    _, calls = load_app(monkeypatch, click_result=True)

    markdown_calls = [call for call in calls if call[0] == "markdown"]
    css_blocks = [call[1][0] for call in markdown_calls if call[1]]
    matrix_css = any(".stApp" in block and ".hello-card" in block for block in css_blocks)

    assert matrix_css

    no_click_calls = [call for call in load_app(monkeypatch)[1] if call[0] == "markdown"]
    assert not no_click_calls
