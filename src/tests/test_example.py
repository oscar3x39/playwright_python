def test_example_is_working(page):
    page.goto("https://example.com")
    assert page.inner_text('h1') == 'Example Domain'
    page.click("text=More information")

def test_dev_is_working(page):
    page.goto("https://dev.to")
    assert 1==0