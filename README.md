# Rockstar Social Club Web Scraping Bot

A Python web scraping bot that uses Playwright to interact with the Rockstar Social Club website.

## Prerequisites

- Python 3.8 or higher

## Installation

1. Install the Python dependencies:

```bash
pip install -r requirements.txt
```

2. Install the Playwright browsers:

```bash
playwright install
```

## Usage

Run the bot with:

```bash
python bot.py
```

The bot will:
- Launch a Chromium browser (visible mode)
- Navigate to the Rockstar Social Club website
- Print the page title to verify access
- Capture a screenshot saved as `screenshot.png`

## Notes

- The browser runs in visible mode (`headless=False`) for debugging purposes
- To run in headless mode, modify `bot.py` and set `headless=True`
