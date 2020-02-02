import os

excluded_file = 'excluded'
excluded_file = os.path.abspath(excluded_file)
log_path = os.path.join(excluded_file, 'log')
tts_location = os.path.join(excluded_file, 'tts')
time_report_tts_location = os.path.join(tts_location, 'time_report')

heart_beat_text2 = '早点睡觉！晚安！'

normal_music = 'NormalMusic'
pure_music = 'PureMusic'
mix_music = 'MinMusic'


# 钉钉链接
class Dingding():
    # 晨祷灵修
    dingding_url = 'https://oapi.dingtalk.com/robot/send?access_token=a056448cc63311f9424ab99da711481f83fd800d08fbda49b36a4120929016bb'
    # 石头派
    stone_pi = 'https://oapi.dingtalk.com/robot/send?access_token=d1103bb860b1a984d0bc21b6cd6c4d885914f51b08de6881fd77d8ddb10511ca'


class SpiritualFood():
    root_url = 'http://www.jidujiao.com'
    url = 'http://www.jidujiao.com/wenkan/lingxiuriliang/'
    daily_food_url = 'http://www.jidujiao.com/wenkan/lingxiuriliang/meirilingliang/'


def mk_dirs(dirs):
    for dir in dirs:
        try:
            if not os.path.exists(dir):
                os.mkdir(dir)
        except:
            continue

# mk_dirs([excluded_file, tts_location, time_report_tts_location])
