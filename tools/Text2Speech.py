import os
import requests
import config
from tools.log import logger
from tools import DDingWarn
from tools.templates import *


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
    return template(success=True, data=a.text)


auth = {"access_token": "24.62d1d2224ff3fb5b0c0baa67c2c55cea.2592000.1580728561.282335-16991715",
        "session_key": "9mzdDcTnQRdWxWpYK56V4SVnVW7ZJ4MA2rjAE6ouKuWiFH\/8g4er2JSjwHRgOOmZmkXjLmRGvpxfttJLt6Eje4U6tFjd5w==",
        "scope": "brain_qrcode brain_ocr_business_card vis-ocr_\u673a\u52a8\u8f66\u68c0\u9a8c\u5408\u683c\u8bc1\u8bc6\u522b vis-ocr_\u4fdd\u5355\u8bc6\u522b vis-ocr_\u884c\u7a0b\u5355\u8bc6\u522b brain_ocr_vehicle_certificate brain_ocr_air_ticket brain_ocr_insurance_doc audio_tts_post public vis-ocr_ocr brain_ocr_scope brain_ocr_general brain_ocr_general_basic vis-ocr_business_license brain_ocr_webimage brain_all_scope brain_ocr_idcard brain_ocr_driving_license brain_ocr_vehicle_license vis-ocr_plate_number brain_solution brain_ocr_plate_number brain_ocr_accurate brain_ocr_accurate_basic brain_ocr_receipt brain_ocr_business_license brain_solution_iocr brain_ocr_handwriting brain_ocr_passport brain_ocr_vat_invoice brain_numbers brain_ocr_train_ticket brain_ocr_taxi_receipt vis-ocr_household_register vis-ocr_vis-classify_birth_certificate vis-ocr_\u53f0\u6e7e\u901a\u884c\u8bc1 vis-ocr_\u6e2f\u6fb3\u901a\u884c\u8bc1 vis-ocr_\u8f66\u8f86vin\u7801\u8bc6\u522b vis-ocr_\u5b9a\u989d\u53d1\u7968\u8bc6\u522b brain_ocr_vin brain_ocr_quota_invoice brain_ocr_birth_certificate brain_ocr_household_register brain_ocr_HK_Macau_pass brain_ocr_taiwan_pass wise_adapt lebo_resource_base lightservice_public hetu_basic lightcms_map_poi kaidian_kaidian ApsMisTest_Test\u6743\u9650 vis-classify_flower lpq_\u5f00\u653e cop_helloScope ApsMis_fangdi_permission smartapp_snsapi_base iop_autocar oauth_tp_app smartapp_smart_game_openapi oauth_sessionkey smartapp_swanid_verify smartapp_opensource_openapi smartapp_opensource_recapi fake_face_detect_\u5f00\u653eScope vis-ocr_\u865a\u62df\u4eba\u7269\u52a9\u7406 idl-video_\u865a\u62df\u4eba\u7269\u52a9\u7406",
        "refresh_token": "25.1dc29be56cd9d775bf193f36a51df8d9.315360000.1893496561.282335-16991715",
        "session_secret": "9064113eb690c88466067c0174a333e1", "expires_in": 2592000}


# 注意aue=4或者6是语音识别要求的格式，但是音频内容不是语音识别要求的自然人发音，所以识别效果会受影响。


def text2speech(text, file_location=config.tts_location, file_name=None):
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
    logger.info('The Text Is:' + text)
    try:
        res = requests.post(url=speech_url, params={'tex': text, 'tok': tok, 'cuid': cuid, 'lan': lan, 'ctp': ctp,
                                                    'spd': spd, 'pit': pit, 'vol': vol, 'per': per, 'aue': aue})
    except Exception as e:
        DDingWarn.request_ding(result=[f'Request Baidu Speech Failed.{e}'])
        return template(message=f'Request Baidu Speech Failed.{e}')
    if res.content[2:12] == b'err_detail':
        DDingWarn.request_ding('Request Baidu Successfully but Token Error.')
        return template(message='Request Baidu Successfully but Token Error.')

    if file_name is None:
        file_name = text[:5]
        file_name = os.path.abspath(os.path.join(file_location, file_name) + '.mp3')
    with open(file_name, 'wb') as fo:
        fo.write(res.content)
    return template(success=True, data=file_name)


if __name__ == '__main__':
    # get_token()
    text = '测试！测试！'
    file = text2speech(text, file_location='.')
