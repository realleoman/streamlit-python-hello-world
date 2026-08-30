import importlib
import sys
import types


def load_app(monkeypatch, click_result=False):
    calls = []
    fake_streamlit = types.SimpleNamespace(
        set_page_config=lambda **kwargs: calls.append(("set_page_config", kwargs)),
        markdown=lambda *args, **kwargs: calls.append(("markdown", args, kwargs)),
        title=lambda *args, **kwargs: calls.append(("title", args, kwargs)),
        button=lambda label: calls.append(("button", label)) or click_result,
        success=lambda *args, **kwargs: calls.append(("success", args, kwargs)),
    )
    monkeypatch.setitem(sys.modules, "streamlit", fake_streamlit)
    sys.modules.pop("app", None)
    app_module = importlib.import_module("app")
    return app_module, calls


def test_app_sets_hello_world_title_and_button(monkeypatch):
    _, calls = load_app(monkeypatch)

    button_calls = [call for call in calls if call[0] == "button"]
    title_calls = [call for call in calls if call[0] == "title"]
    page_title_calls = [call for call in calls if call[0] == "set_page_config"]

    assert page_title_calls and page_title_calls[0][1]["page_title"] == "Hello World"
    assert button_calls and button_calls[0][1] == "Click me"
    assert title_calls and title_calls[0][1][0] == "Hello World"


def test_clicking_button_displays_the_greeting(monkeypatch):
    _, calls = load_app(monkeypatch, click_result=True)

    success_calls = [call for call in calls if call[0] == "success"]
    assert success_calls and success_calls[0][1][0] == "Hello World"


def test_app_includes_matrix_style_background(monkeypatch):
    _, calls = load_app(monkeypatch)

    markdown_calls = [call for call in calls if call[0] == "markdown"]
    css_blocks = [call[1][0] for call in markdown_calls if call[1]]
    matrix_css = any(".stApp" in block and ".hello-card" in block for block in css_blocks)

    assert matrix_css
