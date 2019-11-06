import os

excluded_file = 'excluded'
log_path = os.path.join(excluded_file, 'log')
tts_location = os.path.join(excluded_file, 'tts')

heart_beat_text1 = 'Your RaspberryPi Project Is Still Alive, The Oclock Will Sing You Up Tomorrow! Good Nigth!'
heart_beat_text2 = '你的树莓派正在正常运行，明天你的音乐闹钟将继续响起！晚安！'
dingding_url = 'https://oapi.dingtalk.com/robot/send?access_token=a056448cc63311f9424ab99da711481f83fd800d08fbda49b36a4120929016bb'

def mk_dirs(dirs):
    for dir in dirs:
        try:
            if not os.path.exists(dir):
                os.mkdir(dir)
        except:
            continue


mk_dirs([excluded_file, tts_location])
