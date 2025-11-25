"""
Web scraping bot using Playwright to navigate to Rockstar Social Club website.
"""

from playwright.sync_api import sync_playwright


def main():
    """Launch browser, navigate to Rockstar Social Club, and print page title."""
    with sync_playwright() as p:
        # Launch browser in headless mode
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        # Navigate to Rockstar Social Club
        page.goto("https://socialclub.rockstargames.com/")

        # Wait for the page to load
        page.wait_for_load_state("networkidle")

        # Print page title to verify connection
        print(f"Page Title: {page.title()}")

        # Close the browser
        browser.close()


if __name__ == "__main__":
    main()
