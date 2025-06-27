from flask import Flask, render_template, redirect, url_for, request
import yfinance as yf
from models import Portfolio

app = Flask(__name__)
portfolio = Portfolio(start_balance=10_000_000)  # 10 million KRW

@app.route('/')
def index():
    return render_template('index.html', portfolio=portfolio)

@app.route('/trade', methods=['GET', 'POST'])
def trade():
    if request.method == 'POST':
        symbol = request.form['symbol']
        action = request.form['action']
        quantity = int(request.form['quantity'])

        data = yf.Ticker(symbol).history(period='1d')
        last_price = data['Close'].iloc[-1]

        if action == 'buy':
            portfolio.buy(symbol, quantity, last_price)
        elif action == 'sell':
            portfolio.sell(symbol, quantity, last_price)
        return redirect(url_for('index'))
    return render_template('trade.html')

@app.route('/stats')
def stats():
    return render_template('stats.html', portfolio=portfolio)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
