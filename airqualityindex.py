import requests


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


def get_html_text(url):
    r = requests.get(url, timeout=30)
    print(r.status_code)
    return r.text


def main():
    city_pinyin = input("请输入城市拼音：")
    url = "http://pm25.in/" + city_pinyin
    url_text = get_html_text(url)
    print(url_text)
    aqi_div = '''<div class="span12 data">
        <div class="span1">
          <div class="value">
            '''
    index = url_text.find(aqi_div)
    begin_index = index + len(aqi_div)
    end_index = url_text.find("</div>", begin_index)
    aqi_val = url_text[begin_index: end_index]
    print("空气质量为：{}".format(aqi_val))


if __name__ == '__main__':
    main()
