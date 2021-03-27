import requests
import time
from tools import log
from tools.reply_template import *

logger = log.logger


def server_chan_post(server_chan_url, title: str = '空标题', content: str = '空内容'):
    # server_chan_url = 'https://sc.ftqq.com/SCU94437T1b2b37c7817871dd85a19596a60c0a0b5e9b036b67e40.send'
    data = {
        'text': title,
        'desp': content
    }
    logger.info(f'推送到Server酱微信告警的内容为：{data}')
    try:
        resp = requests.get(url=server_chan_url, params=data)
    except:
        logger.warning(f'推送到Server酱失败。请检查网络连接。')
        return template(message='推送到Server酱失败。请检查网络连接。')
    resp.encoding = 'utf-8'
    # logger.info(f'推送到Server酱结果：{resp.text}')
    # result = eval(resp.text)
    # if result['errmsg'] == 'success':
    if resp.status_code == 200:
        return template(success=True, data=f'{resp.text}')
    else:
        logger.warning(f'发送到Server酱成功但返回了错误信息：{resp.text}')
        if '414 Request-URI Too Large' in resp.text:
            content = content.split('\n\n')
            length = len(content)
            split_palce = int((length + 1) / 2) if length % 2 == 1 else int(length / 2)
            content1, content2 = content[0:split_palce], content[split_palce: ]
            result1 = server_chan_post(server_chan_url=server_chan_url, title=title, content='\n\n'.join(content1))
            time.sleep(1)
            result2 = server_chan_post(server_chan_url=server_chan_url, title=title, content='\n\n'.join(content2))
            if result1[key_success] is True and result2[key_success] is True:
                return template(success=True)
            else:
                return template(message=f'数据发送不正常：{result1[key_message]},{result2[key_message]}')
        return template(message=f'{resp.text}')
