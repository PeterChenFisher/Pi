from tools import log, DDingWarn, ip_update, music_play, Text2Speech, reformat_music_type
from config import *
from Spiders import jdjzww_daily
from events import Bibles

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
    ip_update.ip_addr_monitor()
    return


def executer():
    global manual
    args = sys.argv
    logger.info('Receive args:' + ' - '.join(args))
    arg1 = args[1]
    if arg1 == 'tips':
        logger.info(manual)
    elif arg1 == 'player':

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
        Bibles.logger = log.logger_generator(logger_name='DailyScripture')
        jdjzww_daily.logger = log.logger_generator(logger_name='DailyScripture')
        DDingWarn.logger = log.logger_generator(logger_name='DailyScripture')
        Bibles.send_today_scripture()
    elif arg1 == 'reformat_music':
        reformat_music_type.reformat_cloud_musics()
    elif arg1 == 'ip_monitor':
        ip_update.logger = log.logger_generator(logger_name='IPMonitor')
        DDingWarn.logger = log.logger_generator(logger_name='IPMonitor')
        ip_update.ip_addr_monitor()


# 实现assistant的timer或scheduler，使用该scheduler对单独定时任务进行处理
if __name__ == '__main__':
    if len(sys.argv) == 1:
        test_condition()
    else:
        executer()
