import os
import sys

os_platform = sys.platform


def mk_dirs(dirs):
    for dir in dirs:
        try:
            if not os.path.exists(dir):
                os.mkdir(dir)
        except:
            continue


# 钉钉链接
class Dingding():
    # 晨祷灵修
    dingding_url = 'https://oapi.dingtalk.com/robot/send?access_token=a056448cc63311f9424ab99da711481f83fd800d08fbda49b36a4120929016bb'
    # 石头派
    stone_pi = 'https://oapi.dingtalk.com/robot/send?access_token=d1103bb860b1a984d0bc21b6cd6c4d885914f51b08de6881fd77d8ddb10511ca'
    # Server酱微信推送-给卫娜
    server_chan_url_wn = 'https://sc.ftqq.com/SCU94437T1b2b37c7817871dd85a19596a60c0a0b5e9b036b67e40.send'
    # Server酱微信推送-给温琦
    server_chan_url_vinky = 'https://sc.ftqq.com/SCU98167T7e788378638ccf748cd85248e42f3b405ec0ca593f674.send'


# 灵修文章连接
class SpiritualFood():
    root_url = 'http://www.jidujiao.com'
    url = 'http://www.jidujiao.com/wenkan/lingxiuriliang/'
    daily_food_url = 'http://www.jidujiao.com/wenkan/lingxiuriliang/meirilingliang/'


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

assistant_log_path = os.path.join(excluded_file, 'assistant-log')

heart_beat_text2 = '早点睡觉！晚安！'

raspi_temp_result_file = './raspi-temp-record.txt'

BaiduYunTokenFileLocation = './BaiduYunToken.json'

ProjAutomationUpdateBashFile = './ProjAutomation-UpdateCode.sh'

mk_dirs([excluded_file, tts_location, time_report_tts_location, assistant_log_path])
# init_music_location()
