import requests
from bs4 import BeautifulSoup
import json
import os
from tools.reply_template import *

article_urls = {}
logger = None


def get_article_list(url):
    resp = requests.request(method='GET', url=url)
    resp.encoding = 'utf-8'
    soup = BeautifulSoup(resp.text, 'html5lib')
    main_body = soup.find('div', id='js_content')
    paragraphs = main_body.findAll('p')
    article_url = {}
    article_number = 0
    for paragraph in paragraphs:
        a = paragraph.find('a')
        if not a:
            continue
        article_number += 1
        article_url[str(article_number) + '-' + a.text] = a['href']
    with open('ArticleList.json', 'w+', encoding='utf-8') as fo:
        json.dump(article_url, fo, ensure_ascii=False, indent='  ')
    return article_url


def get_article_content(url, retry_time=0):
    try:
        resp = requests.request(method='GET', url=url)
    except Exception as e:
        logger.waring(f'获取文章失败{e}')
        if retry_time >= 3:
            return template(message=f'获取文章失败，已经达到{retry_time}次，停止获取')
        contents = get_article_content(url, retry_time=retry_time + 1)
        return contents
    resp.encoding = 'utf-8'
    soup = BeautifulSoup(resp.text, 'html5lib')
    paragraphs = soup.find('div', id='js_content')
    paragraphs = paragraphs.findAll('p')
    contents = []
    for paragraph in paragraphs:
        if '朗诵者' in paragraph.text or paragraph.text == '':
            continue
        if '王兆丰 译' in paragraph.text or '[荷兰]亚伯拉罕' in paragraph.text or '加尔文主义讲座' in paragraph.text:
            continue
        contents.append(paragraph.text)
    return template(success=True, data=contents)


def read_article_list(file_path):
    global article_urls
    with open(file_path, 'r+', encoding='utf-8') as fo:
        article_urls = json.load(fo)
    return article_urls


def get_next_article_title(SentArticleTitlePath):
    if not os.path.isfile(SentArticleTitlePath):
        titles = list(article_urls.keys())
        title = titles.pop(0)
        with open(SentArticleTitlePath, 'w', encoding='utf-8') as fo:
            for line in titles:
                fo.write(line)
                fo.write('\n')
    else:
        with open(SentArticleTitlePath, 'r', encoding='utf-8') as fo:
            titles = fo.readlines()
            if len(titles) == 0:
                return None

        with open(SentArticleTitlePath, 'w', encoding='utf-8') as fo:
            title = titles.pop(0)
            for line in titles:
                fo.write(line.strip())
                fo.write('\n')
    logger.info(f'获取到文章标题：{title.strip()}  (待发送文章列表已经更新)')
    return title.strip()


def write_down_article(contents, file_path, title):
    contents.pop(0)
    path = os.path.join(file_path, title)
    with open(path, 'w', encoding='utf-8') as fo:
        for content in contents:
            fo.write(content)
            fo.write('\n')
    logger.info(f'文章写入成功:{path}')


if __name__ == '__main__':
    main_url = 'https://mp.weixin.qq.com/s/TnlJe0vu3w9068VmXx3iFw'
    get_article_list(main_url)
