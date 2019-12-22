import config
import time
from urllib import request
from .log import logger
import json


def request_ding(result, Warning=False, isAtAll=False, request_ding_time=0, ding_url=None):
    content = ('\n\n'.join(result)) if result != '' else ''
    if content == '':
        logger.info('Empty message.')
        return
    if not ding_url:
        ding_url = config.Dingding.stone_pi
    atMobiles = None
    if Warning:
        atMobiles = 18819254603
    logger.warning('warning-message: \n' + content)
    data = {
        "msgtype": "text",
        "text": {
            "content": content
        },
        "at": {
            "atMobiles": [
                atMobiles
            ],
            "isAtAll": isAtAll
        }
    }
    # 设置编码格式
    json_data = json.dumps(data).encode(encoding='utf-8')
    header_encoding = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko',
        "Content-Type": "application/json"}
    try:
        req = request.Request(url=ding_url, data=json_data,
                              headers=header_encoding)
        res = request.urlopen(req)
        res = res.read()
        logger.info(res)
    except Exception:
        logger.warning('Connection to Dingding failed,lets try it next time')
        time.sleep(60)
        request_ding_time += 1
        if request_ding_time == 3:
            logger.warning('Request Dingding a lot times but all failed.')
            return
        request_ding(result, Warning, isAtAll, request_ding_time)
