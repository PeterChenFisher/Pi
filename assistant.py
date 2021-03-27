from tools import log, DDingWarn, ip_update, music_play, reformat_music_type, ServerChanWarn, send_email, Text2Speech
from config import *
from Spiders.SoulBread import jdjzww_daily
from events import Bibles
import time

logger = log.logger_generator(logger_name='Assistant')
mk_dirs([excluded_file, tts_location, time_report_tts_location])
manual = '''
tips;
player; mix_player/normal_player/mix_player; times;
test;
record_temp;
fans_ctr;
'''

if os_platform == 'linux' or os_platform == 'Linux':
    from events import FansCTR


def test_condition():
    # DDingWarn.logger = log.logger_generator(logger_name='Test')
    # ServerChanWarn.logger = log.logger_generator(logger_name='Test')
    # ServerChanWarn.server_chan_post(server_chan_url=Dingding.server_chan_url_test, title='测试！', content='测试server酱测试版')
    # Bibles.send_calvinism_speech()
    import pyttsx3
    pyttsx3.spe
    return


def executor():
    global manual
    args = sys.argv
    logger.info('Receive args:' + ' - '.join(args))
    arg1 = args[1]
    if arg1 == 'tips':
        logger.info(manual)
    elif arg1 == 'player':
        music_play.logger = log.logger_generator(logger_name='MusicPlayer')
        DDingWarn.logger = log.logger_generator(logger_name='MusicPlayer')
        arg2 = args[2] if len(args) >= 3 else normal_music_mode
        times = int(args[3]) if len(args) >= 4 else 50
        music_play.random_play(method='commandline', times=times, mode=arg2)
    elif arg1 == 'record_temp':
        if os_platform == 'linux' or os_platform == 'Linux':
            FansCTR.record_temp()
    elif arg1 == 'fans_ctr':
        if os_platform == 'linux' or os_platform == 'Linux':
            FansCTR.fans_ctrl()
    elif arg1 == 'daily_scripture':
        test = True if len(args) >= 3 else False
        Bibles.send_today_scripture(test)
    elif arg1 == 'daily_anthem':
        Bibles.send_today_anthem()
    elif arg1 == 'daily_grace365':
        Bibles.send_today_grace365()
    elif arg1 == 'daily_stream':
        Bibles.send_today_stream_in_desert()
    elif arg1 == 'calvinism_speech':
        Bibles.send_calvinism_speech()
    elif arg1 == 'ip_monitor':
        ip_update.logger = log.logger_generator(logger_name='IPMonitor')
        DDingWarn.logger = log.logger_generator(logger_name='IPMonitor')
        ip_update.ip_addr_monitor()
    elif arg1 == '':
        pass


# 实现assistant的timer或scheduler，使用该scheduler对单独定时任务进行处理
if __name__ == '__main__':
    if len(sys.argv) == 1:
        test_condition()
    else:
        executor()
