"""
Web scraping bot for Rockstar Social Club website.
Uses Playwright to automate browser interactions.
"""

from playwright.sync_api import sync_playwright, Error as PlaywrightError


def main():
    """
    Main function to scrape the Rockstar Social Club website.
    Launches a browser, navigates to the site, and captures a screenshot.
    """
    url = "https://socialclub.rockstargames.com/"

    with sync_playwright() as p:
        # Launch browser in visible mode (headless=False)
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        try:
            print(f"Navigating to {url}...")
            page.goto(url)

            # Wait for the page to load
            page.wait_for_load_state("networkidle")

            # Print the page title to verify access
            title = page.title()
            print(f"Page title: {title}")

        except PlaywrightError as e:
            print(f"Error navigating to {url}: {e}")
            browser.close()
            return

        try:
            # Capture a screenshot
            screenshot_path = "screenshot.png"
            page.screenshot(path=screenshot_path)
            print(f"Screenshot saved to {screenshot_path}")
        except PlaywrightError as e:
            print(f"Error capturing screenshot: {e}")

        browser.close()


if __name__ == "__main__":
    main()
