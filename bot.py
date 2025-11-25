from playwright.sync_api import sync_playwright


def main():
    with sync_playwright() as p:
        # Launch browser in headless mode
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        # Navigate to Rockstar Social Club
        page.goto("https://socialclub.rockstargames.com/")

        # Wait for the page to fully load (including dynamic content)
        page.wait_for_load_state("networkidle")

        # Print the page title to verify connection
        print(f"Page title: {page.title()}")

        # Close the browser
        browser.close()


if __name__ == "__main__":
    main()
