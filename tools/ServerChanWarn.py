import requests
from config import *
from tools import log, reply_template

logger = log.logger


def server_chan_post(server_chan_url, title='空标题', content='空内容'):
    # server_chan_url = 'https://sc.ftqq.com/SCU94437T1b2b37c7817871dd85a19596a60c0a0b5e9b036b67e40.send'
    data = {
        'text': title,
        'desp': content
    }
    logger.info(f'推送到Server酱微信告警的内容为：{data}')
    try:
        resp = requests.get(url=server_chan_url, params=data)
    except:
        logger.info(f'推送到Server酱失败。请检查网络连接。')
        return reply_template.template(message='推送到Server酱失败。请检查网络连接。')
    resp.encoding = 'utf-8'
    logger.info(f'推送到Server酱结果：{resp.text}')
    return reply_template.template(success=True, data=f'{resp.text}', message=f'{resp.text}')
