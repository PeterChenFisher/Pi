import os
import requests
import config
from Tools.log import logger

# 以下注释代码作用为获取调用百度api的token，auth为返回的结果
# APIKey = 'bpLlUme0C61GisOY9Ce2QYzu'
# SecretKey = 'btQoThXKmmVXGH2hHmBe64goEFQ0kihy'
# AppId = '16991715'

# url = 'https://openapi.baidu.com/oauth/2.0/token'
# params = {'grant_type': "client_credentials",
#           'client_id': APIKey,
#           'client_secret': SecretKey}
# a = requests.get(url, params=params)
# print(a.status_code)
# print(a.text)

auth = {"access_token": "24.0437edc59dacc4cccae26c54fc44544e.2592000.1568106769.282335-16991715",
        "session_key": "9mzdCyyxaZVHKM+gq9vM6K90zpNFPyf9\/1hSNVMzkexZimWGUXjafwJUMGwVLdwr1XKboxePidlCZ2lj3Fuqpyx7v5a3pQ==",
        "scope": "audio_tts_post public vis-ocr_ocr brain_ocr_scope brain_ocr_general brain_ocr_general_basic vis-ocr_business_license brain_ocr_webimage brain_all_scope brain_ocr_idcard brain_ocr_driving_license brain_ocr_vehicle_license vis-ocr_plate_number brain_solution brain_ocr_plate_number brain_ocr_accurate brain_ocr_accurate_basic brain_ocr_receipt brain_ocr_business_license brain_solution_iocr brain_ocr_handwriting brain_ocr_passport brain_ocr_vat_invoice brain_numbers brain_ocr_train_ticket brain_ocr_taxi_receipt vis-ocr_household_register vis-ocr_vis-classify_birth_certificate vis-ocr_\u53f0\u6e7e\u901a\u884c\u8bc1 vis-ocr_\u6e2f\u6fb3\u901a\u884c\u8bc1 vis-ocr_\u8f66\u8f86vin\u7801\u8bc6\u522b vis-ocr_\u5b9a\u989d\u53d1\u7968\u8bc6\u522b brain_ocr_vin brain_ocr_quota_invoice brain_ocr_birth_certificate brain_ocr_household_register brain_ocr_HK_Macau_pass brain_ocr_taiwan_pass wise_adapt lebo_resource_base lightservice_public hetu_basic lightcms_map_poi kaidian_kaidian ApsMisTest_Test\u6743\u9650 vis-classify_flower lpq_\u5f00\u653e cop_helloScope ApsMis_fangdi_permission smartapp_snsapi_base iop_autocar oauth_tp_app smartapp_smart_game_openapi oauth_sessionkey smartapp_swanid_verify smartapp_opensource_openapi smartapp_opensource_recapi fake_face_detect_\u5f00\u653eScope",
        "refresh_token": "25.b2ad9dcfd1d0fa0e1503fd2b3b2bd22c.315360000.1880874769.282335-16991715",
        "session_secret": "4fbc379263070fd72110d6625e15eef9", "expires_in": 2592000}

tok = auth['access_token']
cuid = 'abc'  # 用户唯一标识
ctp = '1'  # 客户端类型选择
lan = 'zh'  # 中文。固定值
spd = 2  # 语速
pit = 6  # 音调
vol = 10  # 音量
per = 106  # 度小宇=1，度小美=0，度逍遥=3，度丫丫=4，度博文=106，度小童=110，度小萌=111，度米朵=103，度小娇=5
aue = 3  # 3为mp3格式(默认)； 4为pcm-16k；5为pcm-8k；6为wav（内容同pcm-16k）;


# 注意aue=4或者6是语音识别要求的格式，但是音频内容不是语音识别要求的自然人发音，所以识别效果会受影响。


def text2speech(text, file_location=config.tts_location, file_name=None):
    if not os.path.exists(file_location):
        os.mkdir(file_location)
    speech_url = 'http://tsn.baidu.com/text2audio'
    logger.info('The Text Is:' + text)
    res = requests.post(url=speech_url, params={'tex': text, 'tok': tok, 'cuid': cuid, 'lan': lan, 'ctp': ctp,
                                                'spd': spd, 'pit': pit, 'vol': vol, 'per': per, 'aue': aue})
    if file_name is None:
        file_name = text[:5]
    file = os.path.join(file_location, file_name) + '.mp3'
    with open(file, 'wb') as fo:
        fo.write(res.content)
    return file


if __name__ == '__main__':
    text = '我是一点都不想你。'
    text2speech(text, file_location='.')
