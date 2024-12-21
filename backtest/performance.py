# 完善绩效评估指标计算，增强可视化功能

import matplotlib.pyplot as plt
import numpy as np

def calculate_performance_metrics(portfolio_value):
    """
    计算常见绩效评估指标。
    :param portfolio_value: 账户净值序列。
    :return: 包含年化收益率、夏普比率、最大回撤等指标的字典。
    """
    returns = portfolio_value.pct_change().dropna()
    num_days = len(returns)
    years = num_days / 252  # 假设一年252个交易日

    # 年化收益率
    annualized_return = (portfolio_value[-1] / portfolio_value[0]) ** (1 / years) - 1

    # 夏普比率（简单示例，可优化风险计算等）
    risk_free_rate = 0.02  # 假设无风险利率
    sharpe_ratio = (annualized_return - risk_free_rate) / returns.std()

    # 最大回撤
    max_drawdown = 0
    peak = portfolio_value[0]
    for value in portfolio_value:
        peak = max(peak, value)
        drawdown = (peak - value) / peak
        max_drawdown = max(max_drawdown, drawdown)

    metrics = {
        'annualized_return': annualized_return,
        'sharpe_ratio': sharpe_ratio,
        'max_drawdown': max_drawdown
    }
    return metrics

def plot_performance(portfolio_value, title='Portfolio Equity Curve'):
    """
    绘制资金曲线，可配置标题等样式。
    :param portfolio_value: 账户净值序列。
    :param title: 图表标题。
    """
    plt.plot(portfolio_value)
    plt.title(title)
    plt.xlabel('Time')
    plt.ylabel('Portfolio Value')
    plt.show()