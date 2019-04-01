import requests
from bs4 import BeautifulSoup


def get_html_text(url):
    r = requests.get(url, timeout=30)
    return r.text


def get_all_cities():
    url = "http://pm25.in/"
    soup = BeautifulSoup(get_html_text(url), 'lxml')
    city_div = soup.find_all('div', {'class': 'bottom'})[1]
    city_link_list = city_div.find_all('a')
    city_list = []
    for city_link in city_link_list:
        city_name = city_link.text
        city_pinyin = city_link['href'][1:]
        city_list.append((city_name, city_pinyin))
    return city_list


def get_city_aqi(city_pinyin):
    url = "http://pm25.in/" + city_pinyin
    soup = BeautifulSoup(get_html_text(url), 'lxml')
    div_list = soup.find_all('div', {'class': 'span1'})
    city_aqi = []
    for i in range(0, 8):
        div_content = div_list[i]
        caption = div_content.find('div', {'class': 'caption'}).text.strip()
        value = div_content.find('div', {'class': 'value'}).text.strip()
        city_aqi.append((caption, value))
    return city_aqi


def main():
    city_list = get_all_cities()
    for city in city_list:
        city_aqi = get_city_aqi(city[1])
        print("{}的空气质量为：{}".format(city[0], city_aqi))


if __name__ == '__main__':
    main()
