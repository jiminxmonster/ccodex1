# Simple Virtual Stock Game

This is a minimal Flask application simulating a virtual stock investment game.
It uses `yfinance` to fetch real market data. Users start with 10 million
KRW in virtual funds and can buy or sell stocks via a web interface.

## Requirements

- Python 3
- Flask
- yfinance

Install dependencies with:

```bash
pip install Flask yfinance
```

## Running

Execute the following command inside the `stock_game` directory:

```bash
python app.py
```

Then open `http://localhost:5000` in your browser.
