# conftest.py
from slugify import slugify
from pathlib import Path
import pytest

@pytest.mark.hookwrapper(scope='session', autouse=True)
def pytest_runtest_makereport(item, call) -> None:
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])
    if call.when == "call":
        if call.excinfo is not None and "page" in item.funcargs:
            page = item.funcargs["page"]
            screenshot_dir = Path(".playwright-screenshots")
            screenshot_dir.mkdir(exist_ok=True)
            filename=str(screenshot_dir / f"{slugify(item.nodeid)}.png")
            page.screenshot(path=filename)
            if filename:
                html = '<div><img src="%s" style="width:600px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % filename
                extra.append(pytest_html.extras.html(html))
    report.extra = extra