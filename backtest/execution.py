# 模拟真实交易逻辑，适配外部接口

class MockBroker:
    def __init__(self, cash=10000):
        self.cash = cash
        self.positions = {}
        self.commission_rate = 0.001  # 交易手续费率

    def execute_order(self, order_type, amount, price):
        """
        模拟订单执行，考虑手续费等情况。
        :param order_type: 订单类型，如 'buy' 或 'sell'。
        :param amount: 交易数量。
        :param price: 交易价格。
        """
        if order_type == 'buy':
            cost = amount * price * (1 + self.commission_rate)
            if cost <= self.cash:
                self.cash -= cost
                self.positions['stock'] = self.positions.get('stock', 0) + amount
            else:
                print("资金不足，无法买入")
        elif order_type == 'sell':
            revenue = amount * price * (1 - self.commission_rate)
            self.cash += revenue
            self.positions['stock'] = max(0, self.positions.get('stock', 0) - amount)