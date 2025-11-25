"""
Web scraping bot for Rockstar Social Club website.
Uses Playwright to automate browser interactions.
"""

from playwright.sync_api import sync_playwright


def main():
    """Initialize Playwright and navigate to Rockstar Social Club."""
    with sync_playwright() as p:
        # Launch browser with headless=False for visibility
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        # Navigate to Rockstar Social Club
        url = "https://socialclub.rockstargames.com/"
        print(f"Navigating to {url}...")
        page.goto(url)

        # Print the page title to verify access
        title = page.title()
        print(f"Page title: {title}")

        # Capture a screenshot
        screenshot_path = "screenshot.png"
        page.screenshot(path=screenshot_path)
        print(f"Screenshot saved to {screenshot_path}")

        # Close the browser
        browser.close()
        print("Browser closed. Scraping complete.")


if __name__ == "__main__":
    main()
