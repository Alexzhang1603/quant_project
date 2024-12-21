# 策略基类，完善文档字符串，可添加钩子方法

import backtrader as bt

class BaseStrategy(bt.Strategy):
    """
    所有策略的基类，定义了通用的接口和可扩展的钩子方法。
    子类继承时需重写 next 方法来实现具体交易逻辑。
    可利用此类已有的属性和方法辅助策略实现，如 self.data 可获取交易数据等。
    """
    def __init__(self):
        pass

    def next(self):
        raise NotImplementedError("需要实现策略的 next 方法")

    def on_start(self):
        """
        交易开始时的钩子方法，子类可按需重写。
        """
        pass

    def on_end(self):
        """
        交易结束时的钩子方法，子类可按需重写。
        """
        pass