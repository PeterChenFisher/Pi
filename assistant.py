from tools import music_play
from events import events
import sys
from config import *

mk_dirs([excluded_file, tts_location, time_report_tts_location])


def test():
    from events.events import daily_scripture
    from apscheduler.schedulers.blocking import BlockingScheduler
    from apscheduler.schedulers.background import BackgroundScheduler
    bs = BlockingScheduler()
    bgs = BackgroundScheduler()
    bgs.add_job(func=daily_scripture, trigger='cron', max_instances=10, month='*', day='*', hour='14', minute='25')
    bs.add_job(func=daily_scripture, trigger='cron', max_instances=10, month='*', day='*', hour='13', minute='54')
    bgs.start()
    bs.start()
    # daily_scripture()
    return


if __name__ == '__main__':
    if len(sys.argv) < 2:
        test()
    else:
        arg = sys.argv[1]
        if arg == 'player':
            music_play.random_play(method='commandline', times=50)
        elif arg == 'pure_player':
            music_play.random_play(method='commandline', times=50, mode=pure_music)
        elif arg == 'mix_player':
            music_play.random_play(method='commandline', times=50, mode=mix_music)
        elif arg == 'test':
            test()
