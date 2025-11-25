# Rockstar Social Club Web Scraper

A Python-based web scraping bot using Playwright to navigate to the Rockstar Social Club website.

## Prerequisites

- Python 3.8 or higher

## Installation

1. Install the required Python packages:

   ```bash
   pip install -r requirements.txt
   ```

2. Install Playwright browsers:

   ```bash
   playwright install
   ```

## Usage

Run the bot with:

```bash
python bot.py
```

The bot will:
- Launch a headless Chromium browser
- Navigate to the Rockstar Social Club website
- Wait for the page to load
- Print the page title to verify connection
- Close the browser
