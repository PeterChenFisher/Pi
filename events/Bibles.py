from tools import log
from tools.reply_template import *
from Spiders.jdjzww_daily import *
from tools import ServerChanWarn, DDingWarn

logger = log.logger


def daily_scripture():
    logger.info(f'开始爬取每日经文...')
    update_url_list()
    scripture = get_very_day_scripture()
    logger.info('今日经文请求钉钉！')
    result = ServerChanWarn.server_chan_post(title='今日经文', content=str(scripture))
    DDingWarn.request_ding(result=[str(scripture), f'{result[key_message]}'])
    logger.info(f'爬取每日经文结束。')
    return


if __name__ == '__main__':
    daily_scripture()
