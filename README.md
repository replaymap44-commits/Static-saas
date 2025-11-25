# Rockstar Social Club Web Scraping Bot

A Python-based web scraping bot using Playwright to retrieve information from the Rockstar Social Club website.

## Prerequisites

- Python 3.7 or higher
- pip (Python package installer)

## Installation

1. Install Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Install Playwright browsers:
   ```bash
   playwright install
   ```

## Usage

Run the bot:
```bash
python bot.py
```

### Headless Mode

By default, the browser runs in visible mode. To run in headless mode (e.g., for production or CI environments), set the `HEADLESS` environment variable:

```bash
HEADLESS=true python bot.py
```

The bot will:
1. Launch a Chromium browser
2. Navigate to the Rockstar Social Club website
3. Wait for the page to load
4. Print the page title to verify success
5. Take a screenshot saved as `screenshot.png`
6. Close the browser

## Output

- Console output showing the page title
- `screenshot.png` - A screenshot of the loaded page for verification
