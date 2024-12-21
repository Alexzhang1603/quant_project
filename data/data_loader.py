# 加载股票数据，支持多数据源，含参数注释、错误处理等

import yfinance as yf
import requests

def load_data(ticker, start_date, end_date):
    """
    从指定数据源加载股票数据。
    :param ticker: 股票代码，如 'AAPL' 代表苹果公司股票。
    :param start_date: 数据开始日期，格式如 'YYYY-MM-DD'。
    :param end_date: 数据结束日期，格式如 'YYYY-MM-DD'。
    :return: 返回包含股票收盘价的数据（可按需扩展返回其他字段）。
    """
    try:
        data = yf.download(ticker, start=start_date, end=end_date)
        return data[['Close']]  # 可扩展获取更多数据列
    except requests.exceptions.RequestException as e:
        print(f"数据加载失败，原因: {e}")
        return None