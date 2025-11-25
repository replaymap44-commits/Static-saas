# Rockstar Social Club Bot

A Python bot using Playwright to retrieve information from the Rockstar Social Club website.

## Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

## Setup

### 1. Create a Virtual Environment

```bash
python -m venv venv
```

### 2. Activate the Virtual Environment

**On Linux/macOS:**
```bash
source venv/bin/activate
```

**On Windows:**
```bash
venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Install Playwright Browsers

```bash
playwright install
```

This will download the necessary browser binaries (Chromium, Firefox, WebKit).

## Usage

Run the bot with:

```bash
python bot.py
```

The bot will:
1. Launch a headless Chromium browser
2. Navigate to the Rockstar Social Club website
3. Print the page title to verify connection
4. Save a screenshot as `screenshot.png`
5. Close the browser

## Configuration

To run the browser in headed mode (visible window), modify `bot.py` and change:

```python
browser = p.chromium.launch(headless=True)
```

to:

```python
browser = p.chromium.launch(headless=False)
```

## Extending the Bot

This bot provides a foundation for scraping specific data from the Rockstar Social Club website. You can extend it by:

- Adding login functionality
- Scraping specific data from user profiles
- Navigating to different sections of the website
- Implementing data extraction and storage

## License

This project is for educational purposes only. Please respect the website's terms of service and robots.txt when using this bot.
