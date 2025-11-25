# Rockstar Social Club Web Scraping Bot

A web scraping bot using Python and Playwright to interact with the Rockstar Social Club website.

## Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

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

The bot will:
1. Launch a Chromium browser (visible, not headless)
2. Navigate to the Rockstar Social Club website
3. Print the page title to verify access
4. Capture a screenshot and save it as `screenshot.png`
5. Close the browser

## Output

- Console output showing the page title
- `screenshot.png` - Screenshot of the Rockstar Social Club homepage
