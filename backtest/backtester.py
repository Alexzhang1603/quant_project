# 优化回测参数传递，返回关键数据

import backtrader as bt

def run_backtest(strategy_config, data):
    """
    运行回测，传入策略配置和交易数据。
    :param strategy_config: 包含策略类及相关参数的配置字典。
    :param data: 股票交易数据。
    :return: 返回包含回测关键数据（如账户净值、交易记录等）的字典。
    """
    cerebro = bt.Cerebro()
    strategy_class = strategy_config['class']
    strategy_params = strategy_config.get('params', {})
    cerebro.addstrategy(strategy_class, **strategy_params)
    cerebro.adddata(data)

    cerebro.broker.set_cash(10000)
    cerebro.broker.set_commission(commission=0.001)

    results = {}
    results['initial_cash'] = cerebro.broker.getvalue()
    cerebro.run()
    results['final_cash'] = cerebro.broker.getvalue()
    results['trading_days'] = len(data)
    # 可继续添加更多关键数据收集逻辑
    return results