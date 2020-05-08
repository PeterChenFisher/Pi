from tools.log import logger
from tools.Text2Speech import text2speech
from config import *
from tools.music_play import pi_mplayer
import time
import os
from tools.reply_template import *


def time_reporting():
    now = time.localtime()
    hour, minute = now[3], now[4]
    text = f'{hour}点{minute}'
    file_name = f'TimeReport_{hour}-{minute}.mp3'
    file_name = os.path.join(time_report_tts_location, file_name)
    if os.path.isfile(file_name):
        logger.info(f'Music File Name:{file_name}')
        pi_mplayer(music=file_name)
        logger.info('Successfully Reported the Time.')
        return
    else:
        text_voice = text2speech(text, file_name=file_name)
        if text_voice[key_success]:
            file_name = text_voice[key_data]
            pi_mplayer(music=file_name)
            logger.info('Successfully Reported the Time.')
            return
        else:
            logger.warning(f'Time Reporting Failed.{text_voice[key_message]}')
        return


# TODO 如果无法访问外网，红灯亮起/语音播报
# TODO 记录网络失常时间，把网络失常时间作为报表记录下来
def check_wifi():
    return
