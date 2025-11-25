"""
Web scraping bot using Playwright to connect to Rockstar Social Club.
"""

import asyncio
import os
from playwright.async_api import async_playwright


async def main():
    """Main function to launch browser and scrape Rockstar Social Club."""
    # Check for headless mode via environment variable (default: False for dev)
    headless = os.getenv("HEADLESS", "false").lower() == "true"

    async with async_playwright() as p:
        # Launch Chromium browser
        browser = await p.chromium.launch(headless=headless)
        page = await browser.new_page()

        try:
            # Navigate to Rockstar Social Club
            print("Navigating to Rockstar Social Club...")
            await page.goto("https://socialclub.rockstargames.com/")

            # Wait for the page to load
            await page.wait_for_load_state("networkidle")

            # Print the page title to verify success
            title = await page.title()
            print(f"Page Title: {title}")

            # Take a screenshot for verification
            await page.screenshot(path="screenshot.png")
            print("Screenshot saved as screenshot.png")

        except Exception as e:
            print(f"Error during navigation: {e}")
        finally:
            # Close the browser
            await browser.close()
            print("Browser closed successfully.")


if __name__ == "__main__":
    asyncio.run(main())
