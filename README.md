# Rockstar Social Club Web Scraper

A web scraping bot using Python and Playwright to interact with the Rockstar Social Club website.

## Prerequisites

- Python 3.8 or higher

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
1. Launch a visible browser window (headless mode disabled)
2. Navigate to the Rockstar Social Club website
3. Print the page title to the console
4. Save a screenshot as `screenshot.png`
5. Close the browser

## Files

- `requirements.txt` - Python package dependencies
- `bot.py` - Main scraping script
- `README.md` - This documentation file
