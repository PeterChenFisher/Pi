from tools import log
from tools.reply_template import *
from Spiders.jdjzww_daily import *
from tools import ServerChanWarn, DDingWarn

logger = log.logger


def send_today_scripture():
    logger.info(f'开始爬取每日经文...')
    update_url_list()
    scripture = get_very_day_scripture()
    logger.info('今日经文请求钉钉！')
    # result1 = ServerChanWarn.server_chan_post(server_chan_url=Dingding.server_chan_url_wn, title='今日经文',
    #                                           content=str(scripture))
    # result2 = ServerChanWarn.server_chan_post(server_chan_url=Dingding.server_chan_url_vinky, title='今日经文',
    #                                           content=str(scripture))
    # DDingWarn.request_ding(result=[str(scripture), f'Vinky:{result1[key_message]} \nWN:{result2[key_message]}'])
    DDingWarn.request_ding(result=[str(scripture)])
    logger.info(f'爬取每日经文结束。')
    return
