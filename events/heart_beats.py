from tools import log
from tools.Text2Speech import text2speech
from config import *
from tools.music_play import pi_mplayer
import time
import os
from tools.reply_template import *

logger = log.logger


def time_reporting(require_times=0, retry=False):
    now = time.localtime()
    hour, minute = now[3], now[4]
    text = f'{hour}点{minute}分'
    file_name = f'TimeReport_{hour}-{minute}.mp3'
    file_name = os.path.join(time_report_tts_location, file_name)
    if os.path.isfile(file_name):
        logger.info(f'本地报时文件名:{file_name}')
        pi_mplayer(music=file_name)
        logger.info('Successfully Reported the Time.')
        return
    else:
        logger.info(f'找不到本地报时文件{file_name}，请求百度')
        text_voice = text2speech(text, file_name=file_name)
        if text_voice[key_success]:
            file_name = text_voice[key_data]
            pi_mplayer(music=file_name)
            logger.info('Successfully Reported the Time.')
            return
        else:
            if not retry:
                return
            require_times += 1
            logger.warning(f'报时失败第{require_times}次')
            if require_times >= 5:
                logger.warning(f'报时失败达到5次.{text_voice[key_message]}')
                return
            time_reporting(require_times=require_times, retry=retry)
        return


# TODO 如果无法访问外网，红灯亮起/语音播报
# TODO 记录网络失常时间，把网络失常时间作为报表记录下来
def check_wifi():
    return
