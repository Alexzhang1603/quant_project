# 均线策略，参数可配置，添加日志记录

import backtrader as bt

class MovingAverageStrategy(bt.Strategy):
    def __init__(self, short_window=50, long_window=200):
        """
        初始化均线策略，设置短、长期均线周期。
        :param short_window: 短期均线周期，默认50。
        :param long_window: 长期均线周期，默认200。
        """
        self.short_ma = bt.indicators.SimpleMovingAverage(self.data.close, period=self.short_window)
        self.long_ma = bt.indicators.SimpleMovingAverage(self.data.close, period=self.long_window)

    def next(self):
        if self.short_ma > self.long_ma:
            if not self.position:
                self.buy()  # 短期均线上穿长期均线，买入
                print(f"{self.data.datetime.date()} 买入，价格: {self.data.close[0]}")
        elif self.short_ma < self.long_ma:
            if self.position:
                self.sell()  # 短期均线下穿长期均线，卖出
                print(f"{self.data.datetime.date()} 卖出，价格: {self.data.close[0]}")