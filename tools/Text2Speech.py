import os
import json
import requests
import config
from tools import log
from tools import DDingWarn
from tools.reply_template import *

auth = None
logger = log.logger


# 获取调用百度api的token，auth为返回的结果
def get_token():
    global auth

    APIKey = 'bpLlUme0C61GisOY9Ce2QYzu'
    SecretKey = 'btQoThXKmmVXGH2hHmBe64goEFQ0kihy'
    AppId = '16991715'
    url = 'https://openapi.baidu.com/oauth/2.0/token'
    params = {'grant_type': "client_credentials",
              'client_id': APIKey,
              'client_secret': SecretKey}
    a = requests.get(url, params=params)
    auth = eval(a.text)
    with open(config.BaiduYunTokenFileLocation, 'w+', encoding='utf-8') as fo:
        json.dump(auth, fo, indent='  ', ensure_ascii=False)

    return template(success=True, data=auth)


def read_token():
    global auth
    if not auth:
        with open(config.BaiduYunTokenFileLocation, 'r+', encoding='utf-8') as fo:
            auth = json.load(fp=fo)
        # auth = eval(auth)
    return


# 注意aue=4或者6是语音识别要求的格式，但是音频内容不是语音识别要求的自然人发音，所以识别效果会受影响。
def text2speech(text, file_location=config.tts_location, file_name=None):
    global auth

    read_token()
    print(auth)
    tok = auth['access_token']
    cuid = 'abc'  # 用户唯一标识
    ctp = '1'  # 客户端类型选择
    lan = 'zh'  # 中文。固定值
    spd = 2  # 语速
    pit = 6  # 音调
    vol = 10  # 音量
    per = 106  # 度小宇=1，度小美=0，度逍遥=3，度丫丫=4，度博文=106，度小童=110，度小萌=111，度米朵=103，度小娇=5
    aue = 3  # 3为mp3格式(默认)； 4为pcm-16k；5为pcm-8k；6为wav（内容同pcm-16k）;
    if not os.path.exists(file_location):
        os.mkdir(file_location)
    speech_url = 'http://tsn.baidu.com/text2audio'
    logger.info(f'The Text Is:{text}')
    try:
        res = requests.post(url=speech_url, params={'tex': text, 'tok': tok, 'cuid': cuid, 'lan': lan, 'ctp': ctp,
                                                    'spd': spd, 'pit': pit, 'vol': vol, 'per': per, 'aue': aue})
    except Exception as e:
        DDingWarn.request_ding(result=[f'请求百度失败！请检查网络连接~  {e}'])
        return template(message=f'请求百度失败！请检查网络连接~  {e}')
    if res.content[2:12] == b'err_detail':
        DDingWarn.request_ding(['请求百度成功，但秘钥错误！现在尝试获取新秘钥！'])
        get_token()
        return template(message='请求百度成功，但秘钥错误！已经尝试获取新秘钥！等待下一次请求结果！')

    if file_name is None:
        file_name = text[:5]
        file_name = os.path.abspath(os.path.join(file_location, file_name) + '.mp3')
    with open(file_name, 'wb') as fo:
        fo.write(res.content)
    return template(success=True, data=file_name)
