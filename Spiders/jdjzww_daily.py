import datetime
import requests
from bs4 import BeautifulSoup
from config import *
from tools.log import logger

daily_food_urls = {}


def get_scripture(url):
    resp = requests.request(method='get', url=url)
    resp.encoding = 'utf-8'
    # soup = BeautifulSoup(resp.text, 'html5lib')
    soup = BeautifulSoup(resp.text)
    scripture = soup.find('div', class_='texts').p.next
    return scripture


def update_url_list(request_times=0):
    global daily_food_urls
    root_url = SpiritualFood.root_url
    main_url = SpiritualFood.daily_food_url

    try:
        logger.info('读取网页...')
        resp = requests.request(method='get', url=main_url, timeout=30)
    except Exception as e:
        request_times += 1
        logger.info(f"更新列表失败。更新次数：{request_times} err[{e}]")
        if request_times >= 10:
            logger.info(f'请求网站次数达到{request_times}次，放弃请求。')
            return
        update_url_list(request_times)
        return
    logger.info('读取网页成功！')
    resp.encoding = 'utf-8'
    # soup = BeautifulSoup(resp.text, 'html5lib')
    soup = BeautifulSoup(resp.text)
    hot_list = soup.find('div', id='hot-list')
    ul = hot_list.ul
    for li in ul:
        if li == '\n\n' or li == '\n\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t':
            continue
        a = li.find('div', class_='url').a
        url = root_url + a['href']
        title = a.text
        daily_food_urls[title] = url
    logger.info(f'列表更新成功：{daily_food_urls}')
    return


def get_very_day_scripture():
    global daily_food_urls
    scripture = ''
    now = datetime.datetime.now()
    date = str(now)[:10]
    logger.info(f'今天日期：{date}')
    for title, url in daily_food_urls.items():
        if title[:10] == date:
            scripture = get_scripture(url=url)
            scripture = scripture.replace('今日经文：', '')
            break
    if scripture == '':
        logger.info('没有爬到当日经文')
        return '没有爬到当日经文'
    else:
        logger.info(f'今天的经文是：{scripture}')
    return scripture
