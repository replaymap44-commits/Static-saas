"""
Rockstar Social Club Bot

A Python bot using Playwright to retrieve information from the Rockstar Social Club website.
This provides a foundation for building more advanced scraping functionality.
"""

from playwright.sync_api import sync_playwright


def main():
    """
    Main function to launch browser, navigate to Rockstar Social Club,
    and verify connection by printing the page title.
    """
    with sync_playwright() as p:
        # Launch browser (set headless=False to see the browser window)
        browser = p.chromium.launch(headless=True)
        
        # Create a new browser context and page
        context = browser.new_context()
        page = context.new_page()
        
        try:
            # Navigate to Rockstar Social Club
            print("Navigating to Rockstar Social Club...")
            page.goto("https://socialclub.rockstargames.com/", timeout=60000)
            
            # Wait for the page to load
            page.wait_for_load_state("domcontentloaded")
            
            # Print the page title to verify connection
            title = page.title()
            print(f"Page Title: {title}")
            
            # Take a screenshot as proof of access
            screenshot_path = "screenshot.png"
            page.screenshot(path=screenshot_path)
            print(f"Screenshot saved to: {screenshot_path}")
            
        except Exception as e:
            print(f"An error occurred: {e}")
            raise
        
        finally:
            # Close the browser
            context.close()
            browser.close()
            print("Browser closed.")


if __name__ == "__main__":
    main()
