from playwright.sync_api import sync_playwright
import time

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://google.com/recaptcha/api2/demo")
    page.frame_locator("iframe[name=\"a-3c12f7h2196\"]").get_by_label("I'm not a robot").click()
    page.frame_locator("iframe[name=\"c-3c12f7h2196\"]").locator("td:nth-child(3)").first.click()
    page.frame_locator("iframe[name=\"c-3c12f7h2196\"]").locator("tr:nth-child(2) > td:nth-child(2)").click()
    page.frame_locator("iframe[name=\"c-3c12f7h2196\"]").locator("tr:nth-child(3) > td:nth-child(2)").click()
    page.frame_locator("iframe[name=\"c-3c12f7h2196\"]").get_by_role("button", name="Verify").click()
    page.get_by_role("button", name="Submit").click()
    print(page.title())
    page.screenshot(path="./img/example.png")
    page.wait_for_timeout(5000) #time.sleep(5)
    browser.close()
    