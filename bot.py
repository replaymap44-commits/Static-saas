"""
Web scraping bot for Rockstar Social Club website using Playwright.
"""

from playwright.sync_api import sync_playwright, TimeoutError as PlaywrightTimeoutError


def main():
    """Initialize Playwright, navigate to Rockstar Social Club, and capture page info."""
    with sync_playwright() as p:
        # Launch browser (headless=False for visibility)
        browser = p.chromium.launch(headless=False)
        try:
            page = browser.new_page()

            # Navigate to Rockstar Social Club
            url = "https://socialclub.rockstargames.com/"
            print(f"Navigating to {url}...")
            try:
                page.goto(url, timeout=30000)  # 30 second timeout
            except PlaywrightTimeoutError:
                print(f"Error: Timed out while navigating to {url}")
                return

            # Print the page title to verify access
            title = page.title()
            print(f"Page title: {title}")

            # Capture a screenshot
            screenshot_path = "screenshot.png"
            page.screenshot(path=screenshot_path)
            print(f"Screenshot saved to {screenshot_path}")
        finally:
            # Ensure browser cleanup even if an error occurs
            browser.close()


if __name__ == "__main__":
    main()
