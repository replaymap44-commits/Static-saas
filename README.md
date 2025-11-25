# Rockstar Social Club Web Scraping Bot

A simple web scraping bot using Python and Playwright to access the Rockstar Social Club website.

## Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

## Installation

1. Clone this repository:
   ```bash
   git clone <repository-url>
   cd Static-saas
   ```

2. Install Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Install Playwright browsers:
   ```bash
   playwright install
   ```

## Usage

Run the bot:
```bash
python bot.py
```

The bot will:
1. Launch a headless Chromium browser
2. Navigate to the Rockstar Social Club website
3. Print the page title to verify the connection
4. Take a screenshot and save it as `screenshot.png`

## Output

- Console output showing the page title
- `screenshot.png` - A screenshot of the Rockstar Social Club homepage
