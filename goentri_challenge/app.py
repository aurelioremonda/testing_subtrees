from playwright.sync_api import sync_playwright

from utils import login
from utils import settings
from utils import getSiteInfo

USERNAME='testinggoentri'
PASSWORD='G0Entri!123!'


def run():
    print(f"Running playwright challenge")

    with sync_playwright() as p:
        browser = p.firefox.launch()
        page = browser.new_page()

        page.goto("https://wordpress.com/log-in")

        # login to wordpress
        login(page, USERNAME, PASSWORD)

        # go to settings
        settings(page)

        # grab the info
        getSiteInfo(page)

        # take a screenshot just for fun
        print("Took a screenshot: screenshot.png")
        page.screenshot(path="screenshot.png")

        browser.close()