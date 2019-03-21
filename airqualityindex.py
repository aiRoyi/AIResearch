def cal_linear(iaqi_lo, iaqi_hi, bp_lo, bp_hi, cp):
    """
    范围缩放
    """
    iaqi = (iaqi_hi - iaqi_lo) * (cp - bp_lo) / (bp_hi - bp_lo) + iaqi_lo
    return iaqi


def cal_pm_iaqi(pm_val):
    if 0 <= pm_val <36:
        iaqi = cal_linear(0, 50, 0, 35, pm_val)
    if 36 <= pm_val < 76:
        iaqi = cal_linear(50, 100, 35, 75, pm_val)
    if 76 <= pm_val < 116:
        iaqi = cal_linear(100, 150, 75, 115, pm_val)
    else:
        pass
    return iaqi


def cal_co_iaqi(co_val):
    if 0 <= co_val < 3:
        iaqi = cal_linear(0, 50, 0, 2, co_val)
    if 3 <= co_val < 5:
        iaqi = cal_linear(50, 100, 2, 4, co_val)
    else:
        pass
    return iaqi


def cal_aqi(param_list):
    pm_val = param_list[0]
    co_val = param_list[1]
    pm_iaqi = cal_pm_iaqi(pm_val)
    co_iaqi = cal_co_iaqi(co_val)
    iaqi_list = []
    iaqi_list.append(pm_iaqi)
    iaqi_list.append(co_iaqi)
    return max(iaqi_list)


def main():
    print("输入以下信息， 用空格分隔")
    input_str = input('(1)PM2.5 (2)CO:')
    str_list = input_str.split(' ')
    pm_val = float(str_list[0])
    co_val = float(str_list[1])
    param_list = []
    param_list.append(pm_val)
    param_list.append(co_val)
    aqi = cal_aqi(param_list)
    print('空气质量指数为:{}'.format(aqi))


if __name__ == '__main__':
    main()
