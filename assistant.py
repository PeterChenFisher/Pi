from tools import music_play
from events import events
import sys
from config import *

mk_dirs([excluded_file, tts_location, time_report_tts_location])


def test():
    music_play.random_play(method='commandline', times=1, mode=mix_music)
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
            music_play.random_play(method='commandline', times=1, mode=mix_music)
        elif arg == 'test':
            test()
