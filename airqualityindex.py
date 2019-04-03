import requests
from bs4 import BeautifulSoup
import csv


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
        city_aqi.append(value)
    return city_aqi


def main():
    city_list = get_all_cities()
    header = ['City', 'AQI','PM2.5/1h', 'PM10/1h', 'CO/1h', 'NO2/1h', 'O3/1h', 'O3/8h', 'SO2/1h']
    with open('china_city_aqi.csv', 'w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(header)
        for i, city in enumerate(city_list):
            if (i + 1) % 10 == 0:
                print('已处理{}条记录（共{}条记录）'.format(i + 1, len(city_list)))
            city_name = city[0]
            city_aqi = get_city_aqi(city[1])
            row = [city_name] + city_aqi
            writer.writerow(row)


if __name__ == '__main__':
    main()
