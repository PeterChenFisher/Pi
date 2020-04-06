import time
from tools import music_play, log, socket_post
from config import *
import threading

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
    socket_post.socket_post(HOST='192.168.1.100', PORT=65432)
    return


def executer():
    global manual
    args = sys.argv
    logger.info('Receive args:' + ' - '.join(args))
    arg1 = args[1]
    if arg1 == 'tips':
        logger.info(manual)
    elif arg1 == 'player':
        arg2 = args[2] if len(args) >= 3 else normal_music
        times = int(args[3]) if len(args) >= 4 else 50
        music_play.random_play(method='commandline', times=times, mode=arg2)
    elif arg1 == 'record_temp':
        if os_platform == 'linux' or os_platform == 'Linux':
            FansCTR.record_temp()
    elif arg1 == 'fans_ctr':
        if os_platform == 'linux' or os_platform == 'Linux':
            FansCTR.fans_ctrl()


if __name__ == '__main__':
    logger = log.logger_generator(log_path=assistant_log_path, logger_name='Assistant')
    if len(sys.argv) == 1:
        test_condition()
    else:
        executer()
