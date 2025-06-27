class Portfolio:
    def __init__(self, start_balance):
        self.balance = start_balance
        self.positions = {}

    def buy(self, symbol, quantity, price):
        cost = quantity * price
        if self.balance >= cost:
            pos = self.positions.setdefault(symbol, {'quantity': 0, 'avg_price': 0})
            total_qty = pos['quantity'] + quantity
            pos['avg_price'] = (
                pos['avg_price'] * pos['quantity'] + cost
            ) / total_qty
            pos['quantity'] = total_qty
            self.balance -= cost

    def sell(self, symbol, quantity, price):
        if symbol in self.positions and self.positions[symbol]['quantity'] >= quantity:
            self.positions[symbol]['quantity'] -= quantity
            self.balance += quantity * price
            if self.positions[symbol]['quantity'] == 0:
                del self.positions[symbol]

    def portfolio_value(self, price_lookup):
        value = self.balance
        for sym, pos in self.positions.items():
            value += pos['quantity'] * price_lookup.get(sym, 0)
        return value
