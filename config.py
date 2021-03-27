import os
import sys

os_platform = sys.platform

logger_ = None


def mk_dirs(dirs):
    for dir in dirs:
        try:
            if not os.path.exists(dir):
                os.mkdir(dir)
        except:
            continue


# 钉钉链接
class Dingding:
    # 晨祷灵修
    dingding_url = 'https://oapi.dingtalk.com/robot/send?access_token=a056448cc63311f9424ab99da711481f83fd800d08fbda49b36a4120929016bb'
    # 石头派
    pi_alert = 'https://oapi.dingtalk.com/robot/send?access_token=d1103bb860b1a984d0bc21b6cd6c4d885914f51b08de6881fd77d8ddb10511ca'
    # 早安
    morning_pi = 'https://oapi.dingtalk.com/robot/send?access_token=fa18af238598f1374d3c2450201d022d46dfa816180f839c8037ec7751833289'
    # Server酱微信推送-给卫娜
    server_chan_url_wn = 'https://sc.ftqq.com/SCU94437T1b2b37c7817871dd85a19596a60c0a0b5e9b036b67e40.send'
    # Server酱微信推送-给温琦
    server_chan_url_vinky = 'https://sc.ftqq.com/SCU98167T7e788378638ccf748cd85248e42f3b405ec0ca593f674.send'
    # Server酱测试版
    server_chan_url_test = 'https://sctapi.ftqq.com/SCT1927TFOtNoDxFtCOiIISeq7GrbE53.send'
    # 企业版微信机器人
    enterpriseWechet_link = 'https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=f26c4ab7-b1a1-4f70-9ade-f2ccf54986bb'


# 灵修文章连接
class SpiritualFood:
    root_url = 'http://www.jidujiao.com'
    url = 'http://www.jidujiao.com/wenkan/lingxiuriliang/'
    daily_food_url = 'http://www.jidujiao.com/wenkan/lingxiuriliang/meirilingliang/'
    daily_food_url_2 = 'http://www.jidujiao.com/wenkan/lingxiuriliang/meirilingliang/index_2.html'

    daily_song_url = 'http://www.jidujiao.com/wenkan/lingxiuriliang/zanmeishi/'
    daily_song_url_2 = 'http://www.jidujiao.com/wenkan/lingxiuriliang/zanmeishi/index_2.html'

    grace_365_url = 'http://www.jidujiao.com/wenkan/lingxiuriliang/endian365/'
    grace_365_url_2 = 'http://www.jidujiao.com/wenkan/lingxiuriliang/endian365/index_2.html'


class MailUsers:
    WeiNa = '2101776486@qq.com'
    OneNote = 'me@onenote.com'
    Peter163 = 'peter_chenxiaofeng@163.com'
    PeterGmail = 'peter.chenxiaofeng@gmail.com'


mail_wn = '2101776486@qq.com'
mail_onenote = 'me@onenote.com'
mail_peter_163 = 'peter_chenxiaofeng@163.com'
mail_peter_gmail = 'peter.chenxiaofeng@gmail.com'

if os_platform == 'linux' or os_platform == 'Linux':
    local_music_location = 'musics'
    cloud_music_file_location = 'musics/CloudMusics.json'
    pure_musics_file_location = './musics/PureMusics.json'
    origin_cloud_music_file_location = 'musics/CloudMusics.txt'
elif os_platform == 'win32':
    local_music_location = 'musics'
    cloud_music_file_location = 'musics\\CloudMusics.json'
    pure_musics_file_location = 'musics\\PureMusics.json'
    origin_cloud_music_file_location = 'musics\\CloudMusics.txt'

normal_music_mode = 'normal_player'
pure_musics_mode = 'pure_player'
mix_music_mode = 'mix_player'

excluded_file = 'excluded'
excluded_file = os.path.abspath(excluded_file)
default_log_path = os.path.join(excluded_file, 'log')
tts_location = os.path.join(excluded_file, 'tts')
time_report_tts_location = os.path.join(tts_location, 'time_report')

mk_dirs([excluded_file, tts_location, time_report_tts_location])

heart_beat_text2 = '早点睡觉！晚安！'

raspi_temp_result_file = os.path.join('ProjAutomation', 'raspi-temp-record.txt')

BaiduYunTokenFileLocation = os.path.join('ProjAutomation', './BaiduYunToken.json')

ProjAutomationUpdateBashFile = os.path.join('ProjAutomation', 'ProjAutomation-UpdateCode.sh')

# init_music_location()

articles_path = os.path.join(excluded_file, 'Articles')
soul_bread_path = os.path.join(articles_path, 'SoulBread')
grace365_path = os.path.join(articles_path, 'Grace365')
streams_in_desert_path = os.path.join(articles_path, 'StreamInDesert')
calvinism_speech_path = os.path.join(articles_path, 'CalvinismSpeech')
mk_dirs([articles_path, soul_bread_path, grace365_path, calvinism_speech_path])

calvinism_article_list_file_path = 'Spiders/LordBooks/CalvinismSpeech/ArticleList.json'
calvinism_next_article_path = os.path.join(articles_path, calvinism_speech_path, 'NextArticle.txt')
