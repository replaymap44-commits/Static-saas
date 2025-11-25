"""
Web scraping bot using Playwright to access Rockstar Social Club website.
"""

from playwright.sync_api import sync_playwright


def main():
    """Main function to run the web scraping bot."""
    with sync_playwright() as p:
        # Launch Chromium browser
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        # Navigate to Rockstar Social Club
        url = "https://socialclub.rockstargames.com/"
        print(f"Navigating to {url}")
        page.goto(url)

        # Print the page title to verify connection
        title = page.title()
        print(f"Page title: {title}")

        # Take a screenshot as proof of access
        screenshot_path = "screenshot.png"
        page.screenshot(path=screenshot_path)
        print(f"Screenshot saved to {screenshot_path}")

        # Close the browser
        browser.close()
        print("Browser closed successfully.")


if __name__ == "__main__":
    main()
