from tools.log import logger
from tools.Text2Speech import text2speech
from config import *
from tools.music_play import pi_mplayer
import time
import os
from tools.templates import *


def time_reporting():
    now = time.localtime()
    hour, minute = now[3], now[4]
    text = f'现在是{hour}点{minute}分'
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
            file_name = text_voice[key_message]
            pi_mplayer(music=file_name)
            logger.info('Successfully Reported the Time.')
            return
        else:
            logger.warning(f'Time Reporting Failed.{text_voice[key_message]}')
        return
