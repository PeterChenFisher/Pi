import datetime
# import dateutil.parser as dpaser
import requests
from bs4 import BeautifulSoup
from config import *
from tools import log, DDingWarn
from tools.reply_template import *
import os

logger = log.logger
local_articles_tree = {}


def get_soul_bread(page_list_urls, root_path):
    daily_bread_urls = read_page_list(page_list_urls=page_list_urls)
    if daily_bread_urls[key_success]:
        for title, url in daily_bread_urls[key_data].items():
            logger.info(f'获取文章:{title}')
            article_content = get_article_content(url)
            if article_content[key_success]:
                logger.info('成功获取文章，写入本地。')
                save_articles(article_content[key_data], root_path=root_path)


def read_page_list(page_list_urls: list, request_times=0):
    logger.info('开始读取灵修文章列表...')
    root_url = SpiritualFood.root_url
    daily_bread_urls = {}

    for url in page_list_urls:
        try:
            resp = requests.request(method='get', url=url, timeout=30)
        except Exception as e:
            request_times += 1
            logger.info(f"更新列表失败。更新次数：{request_times} err[{e}]")
            if request_times >= 10:
                logger.info(f'请求网站次数达到{request_times}次，放弃请求。')
                return template(message='请求网站次数达到{request_times}次，放弃请求。')
            return read_page_list(request_times=request_times, page_list_urls=page_list_urls)

        resp.encoding = 'utf-8'
        soup = BeautifulSoup(resp.text, 'html5lib')
        hot_list = soup.find('div', id='hot-list')
        ul = hot_list.ul
        for li in ul:
            if li == '\n\n' or li == '\n\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t':
                continue
            a = li.find('div', class_='url').a
            article_url = root_url + a['href']
            title = a.text
            daily_bread_urls[title] = article_url
        logger.info('读取列表成功。')
    logger.info(f'列表更新成功：')
    for title, url in daily_bread_urls.items():
        logger.info(f"{title}: {url}")
    return template(True, data=daily_bread_urls)


def save_articles(article_content, root_path):
    url = article_content['url']
    title = article_content['title']
    content = article_content['content']
    date_place = title.find('恩典365') if title.find('恩典365') != -1 else title.find('每日灵粮')
    article_date, title = title[:date_place], title[date_place:].replace('每日灵粮——', '').replace('恩典365', '')
    year, month, day = article_date[0:4], article_date[4:6], article_date[6:8]
    mk_dirs([os.path.join(root_path, year), os.path.join(root_path, year, month)])
    filename = year + '-' + month + '-' + day + '-' + title + '.txt'
    write_aim_path = os.path.join(root_path, year, month, filename)
    with open(write_aim_path, 'w+', encoding='utf-8') as fo:
        fo.write(url + '\n')
        fo.write(content)
    return


def get_article_content(url, retry_time=0):
    logger.info('尝试读取网页……')
    try:
        resp = requests.request(method='get', url=url)
    except Exception as e:
        retry_time += 1
        if retry_time >= 10:
            logger.info(f'读取次数达到{retry_time}，放弃读取。')
            return template(message=f'读取次数达到{retry_time}，放弃读取。')
        logger.info(f'读取网页失败{retry_time}次。报错：{e.__str__()}')
        return get_article_content(url, retry_time)
    logger.info('读取网页成功，对网页进行解析')
    resp.encoding = 'utf-8'

    soup = BeautifulSoup(resp.text, 'html5lib')
    try:
        title = soup.find('div', class_='title')
        title = title.h1.text
        title = title.replace(' ', '')
        article_content = soup.find('div', class_='texts')
        article_content = article_content.text
        article_content = cut_needless_text(original_text=article_content,
                                            cut_keywords=['图片版', '简谱：', '\n\xa0\n\t\t\t\t\n\t\t\t\t\t',
                                                          '以上视频由天声传播协会录制', '分享到：'],
                                            delete_keywords=['\n\n\n\n\n\n点击下载MP3文件\t\t\t\t\n', '\n\n\t\t\t\t',
                                                             '\n\n点击下载MP3文件\t\t\t\t'])
        article_content = article_content.replace('\n\n', '\n')
        scripture_place = article_content.find('\n')
        scripture = article_content[0:scripture_place]
        if '恩典365' in title:
            song_url = get_song_url(url=url, title=title)
            article_content += '\n音频链接：' + song_url[key_data]['song_url'] if song_url[key_success] else '找不到音频链接'
    except Exception as e:
        DDingWarn.request_ding(result=[f'网页结构已经发生变化。', f'解析中报错：\n {e}'])
        return template(message='网页结构已经发生变化。')
    logger.info('获取文章成功')
    return template(True, data={
        'url': url,
        'title': title,
        'content': article_content,
        'scripture': scripture
    })


def cut_needless_text(original_text: str, delete_keywords: list = [], cut_keywords: list = []):
    if delete_keywords:
        for text in delete_keywords:
            original_text = original_text.replace(text, '')
    if cut_keywords:
        for text in cut_keywords:
            split_place = original_text.find(text)
            original_text = original_text[0:split_place]
    return original_text


def read_local_articles_tree(root_path):
    global local_articles_tree
    for year in os.listdir(root_path):
        local_articles_tree[year] = {}
        for month in os.listdir(os.path.join(root_path, year)):
            local_articles_tree[year].update({month: os.listdir(os.path.join(root_path, year, month))})
            # local_articles_tree.update({month: os.listdir(os.path.join(root_path, year, month))})


def get_song_url(url, title, request_time=0):
    logger.info('从网页读取音乐链接...')
    try:
        resp = requests.get(url)
    except Exception as e:
        request_time += 1
        logger.info(f'读取网页失败{request_time}次，错误：{e.__str__()}')
        if request_time >= 5:
            return template(message=f'读取网页失败达到{request_time}次，终止读取')
        return get_song_url(url, request_time)
    resp.encoding = 'utf-8'
    try:
        soup = BeautifulSoup(resp.text, 'html5lib')
        nrydown = soup.find('div', class_='nrydown')
        song_url = nrydown.a['href']
    except Exception as e:
        DDingWarn.request_ding(result=[f'网页结构已经发生变化，请尽快修改{e}'])
        return template(message=f'网页结构已经发生变化，获取内容失败{e}')
    return template(success=True, data={'song_url': song_url, 'title': title})


def get_very_day_anthem_url_lyrics(date=''):
    result = {}
    if not date:
        date = datetime.datetime.now().__str__()[0:10].replace('-', '')
    read_page_list_result = read_page_list(
        page_list_urls=[SpiritualFood.daily_song_url, SpiritualFood.daily_song_url_2])
    if read_page_list_result[key_success]:
        for title, url in read_page_list_result[key_data].items():
            if date in title:
                logger.info(f'找到日期对应链接：{title} - {url}')
                lyric_result = get_article_content(url)
                if lyric_result[key_success]:
                    result.update({'lyric': lyric_result[key_data]['content']})
                song_url_result = get_song_url(url, title)
                if song_url_result[key_success]:
                    result.update(song_url_result[key_data])
                return template(success=True, data=result)
    return template(message='从列表中找不到今日的赞美诗')


def get_very_day_article(page_url_lists: list, root_path: str, get_scripture_only: bool = False,
                         acquire_time: int = 0, date: str = '', article_url: str = None):
    if article_url:
        article_content = get_article_content(article_url)
        if article_content[key_success]:
            logger.info('成功获取文章，写入本地。')
            save_articles(article_content[key_data], root_path=root_path)
    if not date:
        now = datetime.datetime.now()
        today, month, year = str(now)[8:10], str(now)[5:7], str(now)[0:4]
    else:
        today, month, year = str(date)[8:10], str(date)[5:7], str(date)[0:4]
    mk_dirs([os.path.join(root_path, year), os.path.join(root_path, year, month)])
    logger.info('读取本地内容树')
    read_local_articles_tree(root_path=root_path)

    month_articles = local_articles_tree[year][month]
    article_dates = [i[8:10] for i in month_articles]
    if today in article_dates:
        file_name = local_articles_tree[year][month][article_dates.index(today)]
        title = file_name.replace('.txt', '')
        file_path = os.path.join(root_path, year, month, file_name)
        with open(file_path, 'r+', encoding='utf-8') as fo:
            article_url = fo.readline()
            scripture = fo.readline()
            article = fo.read()
        if get_scripture_only:
            return template(True, data=scripture)
            # 继续处理文件读取结果
        logger.info(f'从本地获取到今日灵修内容[{title}]，进行推送。')
    else:
        logger.info(f'本地未发现当天灵修内容，现在进行灵修内容的爬取。爬取次数：第{acquire_time}次。')
        # 获取灵修文章到本地
        get_soul_bread(page_list_urls=page_url_lists, root_path=root_path)
        logger.info('爬取结束~')
        acquire_time += 1
        if acquire_time >= 10:
            return template(message='尝试获取内容超过十次，放弃获取文章。')
        result = get_very_day_article(acquire_time=acquire_time, root_path=root_path, page_url_lists=page_url_lists)
        if not result[key_success]:
            return template(message=result[key_message])
        data = result[key_data]
        article, title, scripture, article_url = data['article'], data['title'], data['scripture'], data['url']
    return template(success=True, data={'title': title, 'article': article, 'scripture': scripture, 'url': article_url})
