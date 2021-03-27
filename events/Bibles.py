from Spiders.SoulBread import jdjzww_daily
from tools import ServerChanWarn, DDingWarn, send_email, log
from tools.reply_template import *
from config import *
import datetime, re
from Spiders.LordBooks.CalvinismSpeech import get_contents

logger = log.logger_generator(logger_name='DailyScripture')
jdjzww_daily.logger = log.logger_generator(logger_name='DailyScripture')
DDingWarn.logger = log.logger_generator(logger_name='DailyScripture')
send_email.logger = log.logger_generator(logger_name='DailyScripture')
ServerChanWarn.logger = log.logger_generator(logger_name='DailyScripture')
get_contents.logger = log.logger_generator(logger_name='DailyScripture')


def send_today_scripture(test=False):
    logger.debug(f'开始获取今日灵修内容')
    soul_bread_result = jdjzww_daily.get_very_day_article(page_url_lists=[SpiritualFood.daily_food_url,
                                                                          SpiritualFood.daily_food_url_2],
                                                          root_path=soul_bread_path)
    # 当需要补提交某日经文时候，使用下面的语句，时间格式为 ‘yyyy-mm-dd’
    # soul_bread_result = get_very_day_article(date='2020-09-29')
    if not soul_bread_result[key_success]:
        DDingWarn.request_ding(result=['获取今日经文失败:', soul_bread_result[key_message]])
        return
    soul_bread = soul_bread_result[key_data]
    scripture = soul_bread['scripture'].replace('\n', '')

    if test:
        DDingWarn.request_ding(result=['测试！', str(scripture)], ding_url=Dingding.pi_alert)
        DDingWarn.request_ding(result=['测试！', scripture.replace('今日经文：', ''), '', soul_bread['article']],
                               ding_url=Dingding.pi_alert)
        return

    logger.debug('通过ServerChan 发送给朋友:')
    logger.debug('发送给卫娜')
    title, article = soul_bread['title'], soul_bread['article'].replace('\n', '\n\n')
    result1 = ServerChanWarn.server_chan_post(server_chan_url=Dingding.server_chan_url_wn,
                                              title=f"{title}",
                                              content=f"{scripture}\n\n{article}")
    if not result1[key_success]:
        DDingWarn.request_ding(result=[result1[key_message]])
    else:
        logger.info('发送给卫娜成功。')

    logger.debug('发送给温琦')
    result2 = ServerChanWarn.server_chan_post(server_chan_url=Dingding.server_chan_url_vinky, title='今日经文',
                                              content=str(scripture))
    if not result2[key_success]:
        DDingWarn.request_ding(result2[key_message])
    else:
        logger.info('发送给温琦成功。')

    # logger.info('通过钉钉发送给自己')
    # DDingWarn.request_ding(result=[scripture.replace('今日经文：', ''), '', soul_bread['article']],
    #                        ding_url=Dingding.morning_pi)

    logger.debug('将灵修内容通过邮箱发送OneNote和网易邮箱')
    send_result = send_email.send_mail(aim_list=[mail_onenote, mail_peter_163, mail_wn],
                                       subject=soul_bread['title'], content=scripture + '\n' + soul_bread['article'])
    if not send_result[key_success]:
        DDingWarn.request_ding(result=[send_result[key_message]])
    send_email.close_server()


# 发送今日赞美诗
def send_today_anthem():
    logger.debug('获取今日赞美诗')
    get_url_result = jdjzww_daily.get_very_day_anthem_url_lyrics()
    # print(get_url_result)
    if get_url_result[key_success]:
        logger.debug('获取成功，今日赞美诗发送卫娜：')
        data = get_url_result[key_data]
        # DDingWarn.request_ding(result=[data['song_url'], data['lyric']], ding_url=Dingding.morning_pi)
        song_url, lyric = data['song_url'], data['lyric'].replace('\n', '\n\n')
        result1 = ServerChanWarn.server_chan_post(server_chan_url=Dingding.server_chan_url_wn,
                                                  title=f"{data['title']}", content=f"{song_url}\n\n{lyric}")
        if not result1[key_success]:
            DDingWarn.request_ding(result=[result1[key_message]], ding_url=Dingding.pi_alert)
        else:
            logger.info('今日赞美诗发送给卫娜成功。')
        #  发送邮箱
        send_result = send_email.send_mail(
            aim_list=[mail_peter_163, mail_wn], subject=f"{data['title']}",
            content=f"{song_url}\n{lyric}")
        if not send_result[key_success]:
            DDingWarn.request_ding(result=[send_result[key_message]])
        send_email.close_server()
    else:
        DDingWarn.request_ding(result=['今日赞美诗获取失败，未发送给卫娜', get_url_result[key_message]], ding_url=Dingding.pi_alert)


# 发送今日恩典365
def send_today_grace365(test=False):
    logger.debug('获取今日恩典365')

    grace365_result = jdjzww_daily.get_very_day_article(
        page_url_lists=[SpiritualFood.grace_365_url, SpiritualFood.grace_365_url_2], root_path=grace365_path)
    # 当需要补提交某日经文时候，使用下面的语句，时间格式为 ‘yyyy-mm-dd’
    # grace365_result = get_very_day_article(date='2020-09-29')
    if not grace365_result[key_success]:
        DDingWarn.request_ding(result=['获取今日恩典365内容失败:', grace365_result[key_message]])
        return
    grace365 = grace365_result[key_data]

    if test:
        DDingWarn.request_ding(result=['测试！', grace365['article']], ding_url=Dingding.pi_alert)
        return

    # logger.info('通过钉钉发送群聊')
    # DDingWarn.request_ding(result=[grace365['article']], ding_url=Dingding.morning_pi)

    logger.debug('将恩典365内容通过邮箱发送OneNote和网易邮箱')
    send_result = send_email.send_mail(aim_list=[mail_onenote, mail_peter_163, mail_wn],
                                       subject=grace365['title'], content=grace365['article'])
    if not send_result[key_success]:
        DDingWarn.request_ding(result=[send_result[key_message]])
    send_email.close_server()


# 发送当天荒漠甘泉
def send_today_stream_in_desert(date: list = []):
    if not date:
        now = datetime.datetime.now()
        today, month = now.day, now.month
        logger.debug(f'{month}月{today}日荒漠甘泉推送')
    else:
        today, month = date[0], date[1]
    aim_path = os.path.join(streams_in_desert_path, f'{month}月{today}日.md')
    with open(aim_path, 'r+', encoding='utf-8') as fo:
        article_content = fo.read()
    logger.debug('发送给卫娜')
    result = ServerChanWarn.server_chan_post(server_chan_url=Dingding.server_chan_url_wn, content=article_content,
                                             title=f'''荒漠甘泉{month}月{today}日''')
    if not result[key_success]:
        DDingWarn.request_ding(result=[result[key_message]])
    logger.debug('将灵修内容通过邮箱发送OneNote和网易邮箱')
    article_content.strip('# |[|]')
    # re.sub('\(http\:\/\/*\)', '', article_content)
    send_result = send_email.send_mail(aim_list=[mail_onenote, mail_peter_163, mail_wn],
                                       subject=f'''荒漠甘泉{month}月{today}日''', content=article_content)
    if not send_result[key_success]:
        DDingWarn.request_ding(result=[send_result[key_message]])
    send_email.close_server()


def send_calvinism_speech():
    logger.debug('开始获取加尔文主义讲座文章并推送')
    logger.debug('读取文章-链接列表')
    article_list = get_contents.read_article_list(file_path=calvinism_article_list_file_path)
    title = get_contents.get_next_article_title(SentArticleTitlePath=calvinism_next_article_path)
    logger.debug(f'当次发送文章标题：{title}')
    if not title:
        DDingWarn.request_ding(result='没有文章了')
        return
    contents = get_contents.get_article_content(url=article_list[title])
    if not contents[key_success]:
        DDingWarn.request_ding(result=f'今日推送失败：{contents[key_message]}')
        return
    contents = contents[key_data]
    get_contents.write_down_article(contents=contents, file_path=calvinism_speech_path, title=title)
    send_result = send_email.send_mail(aim_list=[mail_peter_163, mail_wn, mail_onenote],
                                       subject=f'''加尔文主义讲座-{title}''', content='\n'.join(contents))
    if not send_result[key_success]:
        DDingWarn.request_ding(result=[send_result[key_message]])
    send_email.close_server()
