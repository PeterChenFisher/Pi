import os
import sys

os_platform = sys.platform

pure_musics_location = None
local_music_location = None
cloud_music_location = None

raspi_temp_result_file = './raspi-temp-record.txt'


def mk_dirs(dirs):
    for dir in dirs:
        try:
            if not os.path.exists(dir):
                os.mkdir(dir)
        except:
            continue


def init_music_location():
    global pure_musics_location, local_music_location, cloud_music_location, os_platform

    if os_platform == 'linux' or os_platform == 'Linux':
        pure_musics_location = 'musics/PureMusics'
        local_music_location = 'musics'
        cloud_music_location = 'musics/musics.txt'
    elif os_platform == 'win32':
        pure_musics_location = 'musics\\PureMusics'
        local_music_location = 'musics'
        cloud_music_location = 'musics\musics.txt'


# 钉钉链接
class Dingding():
    # 晨祷灵修
    dingding_url = 'https://oapi.dingtalk.com/robot/send?access_token=a056448cc63311f9424ab99da711481f83fd800d08fbda49b36a4120929016bb'
    # 石头派
    stone_pi = 'https://oapi.dingtalk.com/robot/send?access_token=d1103bb860b1a984d0bc21b6cd6c4d885914f51b08de6881fd77d8ddb10511ca'


# 灵修文章连接
class SpiritualFood():
    root_url = 'http://www.jidujiao.com'
    url = 'http://www.jidujiao.com/wenkan/lingxiuriliang/'
    daily_food_url = 'http://www.jidujiao.com/wenkan/lingxiuriliang/meirilingliang/'


init_music_location()

excluded_file = 'excluded'
excluded_file = os.path.abspath(excluded_file)
log_path = os.path.join(excluded_file, 'log')
tts_location = os.path.join(excluded_file, 'tts')
time_report_tts_location = os.path.join(tts_location, 'time_report')

assistant_log_path = os.path.join(excluded_file, 'assistant-log')

heart_beat_text2 = '早点睡觉！晚安！'

normal_music = 'normal_player'
pure_music = 'pure_player'
mix_music = 'mix_player'

mk_dirs([excluded_file, tts_location, time_report_tts_location])
