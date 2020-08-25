from tools.reply_template import *
from Spiders.jdjzww_daily import *
from tools import ServerChanWarn, DDingWarn

logger = log.logger


def send_today_scripture(test=False):
    logger.info(f'开始爬取每日经文...')
    update_url_list()
    scripture = get_very_day_scripture()
    logger.info('今日经文请求钉钉！')
    if test:
        logger.info('进入测试模式')
        DDingWarn.request_ding(result=[str(scripture)])
        return
    logger.info('发送给卫娜')
    result1 = ServerChanWarn.server_chan_post(server_chan_url=Dingding.server_chan_url_wn, title='今日经文',
                                              content=str(scripture))
    logger.info('发送给温琦')
    result2 = ServerChanWarn.server_chan_post(server_chan_url=Dingding.server_chan_url_vinky, title='今日经文',
                                              content=str(scripture))
    DDingWarn.request_ding(result=[str(scripture), f'卫娜:{result1[key_message]}', f'温琦:{result2[key_message]}'])
    logger.info(f'爬取每日经文结束。')
    return
