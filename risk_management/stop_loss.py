# 完善止损策略逻辑，日志记录与配置选择

def set_stop_loss(entry_price, stop_loss_type='fixed', stop_loss_param=0.1):
    """
    设置止损策略，支持不同类型止损。
    :param entry_price: 买入价格。
    :param stop_loss_type: 止损类型，如 'fixed'（固定比例）、'trailing'（移动止损）等。
    :param stop_loss_param: 止损参数，如固定比例值或移动止损相关参数。
    :return: 止损价格。
    """
    if stop_loss_type == 'fixed':
        stop_loss_price = entry_price * (1 - stop_loss_param)
    elif stop_loss_type == 'trailing':
        # 移动止损逻辑待完善
        stop_loss_price = entry_price
    else:
        print("不支持的止损类型")
        stop_loss_price = None
    print(f"设置止损价格为: {stop_loss_price}")
    return stop_loss_price