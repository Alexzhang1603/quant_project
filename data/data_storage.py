# 实现多种数据存储方式，管理存储路径

import pickle
import pandas as pd
import sqlite3

def store_data(data, storage_type, filename):
    """
    将数据存储到指定位置，支持文件或数据库存储。
    :param data: 要存储的股票数据（如DataFrame）。
    :param storage_type: 存储类型，如 'file' 或 'database'。
    :param filename: 存储文件名（若是文件存储）或数据库表名（若是数据库存储）等相关标识。
    """
    if storage_type == 'file':
        with open(filename, 'wb') as f:
            pickle.dump(data, f)
    elif storage_type == 'database':
        conn = sqlite3.connect('stock_data.db')  # 可配置数据库连接信息
        data.to_sql(filename, conn, if_exists='replace', index=False)
        conn.close()

def load_stored_data(storage_type, filename):
    """
    从指定位置加载存储的数据。
    :param storage_type: 存储类型，如 'file' 或 'database'。
    :param filename: 存储文件名（若是文件存储）或数据库表名（若是数据库存储）等相关标识。
    :return: 加载的数据。
    """
    if storage_type == 'file':
        with open(filename, 'rb') as f:
            return pickle.load(f)
    elif storage_type == 'database':
        conn = sqlite3.connect('stock_data.db')
        data = pd.read_sql(f"SELECT * FROM {filename}", conn)
        conn.close()
        return data