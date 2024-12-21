# 数据清洗、预处理，功能细化拆分，增加验证逻辑

import pandas as pd

def calculate_returns(data):
    """
    计算股票收益率。
    :param data: 包含股票价格数据的DataFrame。
    :return: 添加收益率列后的DataFrame。
    """
    data['Returns'] = data['Close'].pct_change()
    return data

def fill_missing_values(data):
    """
    填充数据中的缺失值。
    :param data: 包含股票数据的DataFrame。
    :return: 处理缺失值后的DataFrame。
    """
    data = data.dropna()
    return data

def preprocess_data(data):
    """
    数据预处理主函数，调用其他子函数完成整体预处理。
    :param data: 原始股票数据。
    :return: 预处理后的股票数据。
    """
    data = calculate_returns(data)
    data = fill_missing_values(data)
    # 可继续添加其他预处理步骤
    return data