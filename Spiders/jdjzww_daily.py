import requests
from bs4 import BeautifulSoup

url = 'http://www.jidujiao.com/wenkan/lingxiuriliang/'
daily_food_url = 'http://www.jidujiao.com/wenkan/lingxiuriliang/meirilingliang/'

resp = requests.request(method='get', url=daily_food_url)
html = resp.text
soup = BeautifulSoup(html)
hot_list = soup.find('div', id='hot-list')
ul = hot_list.ul
# lis = ul.findall('li')
# print(lis[0])
print(ul.li)
print(type(ul))

# print(hot_list)
