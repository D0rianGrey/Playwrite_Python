from playwright.sync_api import sync_playwright

playwright = sync_playwright().start()

browser = playwright.chromium.launch(headless=False)
page = browser.new_page()
page.goto("https://www.google.com.ua")
page.pause()
page.get_by_role("button", name="Accept all").click()
