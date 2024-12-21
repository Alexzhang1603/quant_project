# 集成多仓位管理策略，参数校验

def kelly_position_size(win_prob, win_loss_ratio):
    """
    计算凯利公式仓位，进行参数合法性校验。
    :param win_prob: 获胜概率，取值范围应在0到1之间。
    :param win_loss_ratio: 盈亏比。
    :return: 凯利公式计算出的仓位比例，若参数不合法返回None。
    """
    if not (0 <= win_prob <= 1):
        print("获胜概率参数不合法")
        return None
    return win_prob - (1 - win_prob) / win_loss_ratio

def equal_weight_position_size(num_assets):
    """
    等比资金分配仓位管理策略。
    :param num_assets: 投资资产数量。
    :return: 每资产分配的仓位比例。
    """
    return 1 / num_assets

def get_position_size(strategy, params):
    """
    根据指定策略和参数选择仓位管理策略并计算仓位。
    :param strategy: 仓位管理策略名称，如 'kelly' 或 'equal_weight'。
    :param params: 对应策略所需参数的字典。
    :return: 计算出的仓位比例。
    """
    if strategy == 'kelly':
        return kelly_position_size(params['win_prob'], params['win_loss_ratio'])
    elif strategy == 'equal_weight':
        return equal_weight_position_size(params['num_assets'])