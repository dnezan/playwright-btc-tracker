from playwright.sync_api import sync_playwright
import time

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("http://playwright.dev")
    print(page.title())
    page.screenshot(path="./img/example.png")
    page.wait_for_timeout(5000) #time.sleep(5)
    browser.close()