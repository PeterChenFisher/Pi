import config
import time
from urllib import request
from .log import logger
import json


def request_ding(result, Warning=False, isAtAll=False, request_ding_time=0, ding_url=None):
    if type(result) != list:
        result = ['告警信息格式错误了！请发送一个错误信息列表过来~']
    # result.append('\n    来自石头派的问候！愿你平安！')
    content = ('\n'.join(result)) if result != '' else ''
    content += '\n\n    来自石头派的问候！愿你平安！'
    if content == '':
        logger.info('空信息。')
        return
    if not ding_url:
        ding_url = config.Dingding.stone_pi
    atMobiles = None
    if Warning:
        atMobiles = None
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
    except Exception as e:
        logger.warning(f'连接钉钉失败:第{request_ding_time}次。')
        time.sleep(60)
        request_ding_time += 1
        if request_ding_time == 3:
            logger.warning(f'连接钉钉失败{request_ding_time}次。停止重试。{e}')
            return
        request_ding(result, Warning, isAtAll, request_ding_time)
