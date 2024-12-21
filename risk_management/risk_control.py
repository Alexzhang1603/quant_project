# 细化整合风险控制功能，统一接口

def assess_risk(position_size, stop_loss_price, current_price, max_risk_percentage=0.05):
    """
    评估交易风险是否可控。
    :param position_size: 仓位大小。
    :param stop_loss_price: 止损价格。
    :param current_price: 当前价格。
    :param max_risk_percentage: 最大可承受风险比例。
    :return: True 表示风险可控，False 表示风险不可控。
    """
    potential_loss = (current_price - stop_loss_price) * position_size
    total_value = current_price * position_size
    risk_percentage = potential_loss / total_value
    return risk_percentage <= max_risk_percentage

def manage_risk(position_size, stop_loss_price, current_price):
    """
    整体风险控制逻辑，调用风险评估等功能。
    :param position_size: 仓位大小。
    :param stop_loss_price: 止损价格。
    :param current_price: 当前价格。
    :return: 根据风险情况调整后的仓位大小等信息（可扩展返回更多）。
    """
    if assess_risk(position_size, stop_loss_price, current_price):
        print("Risk is within acceptable limits.")
    else:
        print("Risk exceeds acceptable level. Adjusting position size accordingly.")