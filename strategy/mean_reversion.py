# 均值回归策略，参数可配置，添加日志记录

import backtrader as bt

class MeanReversionStrategy(bt.Strategy):
    def __init__(self, short_window=20, zscore_threshold=1.5):
        """
        初始化均值回归策略，设置相关参数。
        :param short_window: 短期均线周期，默认20。
        :param zscore_threshold: Z-score阈值，默认1.5。
        """
        self.short_window = short_window
        self.zscore_threshold = zscore_threshold
        self.short_ma = bt.indicators.SimpleMovingAverage(self.data.close, period=self.short_window)
        self.std_dev = bt.indicators.StandardDeviation(self.data.close, period=self.short_window)
        self.zscore = (self.data.close - self.short_ma) / self.std_dev

    def next(self):
        if self.zscore[0] > self.zscore_threshold:
            if self.position:
                self.sell()  # 卖出信号
                print(f"{self.data.datetime.date()} 卖出，Z-score: {self.zscore[0]}")
        elif self.zscore[0] < -self.zscore_threshold:
            if not self.position:
                self.buy()  # 买入信号
                print(f"{self.data.datetime.date()} 买入，Z-score: {self.zscore[0]}")