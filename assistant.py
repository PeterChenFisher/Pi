from tools import music_play
from events import events
import sys
from config import *

mk_dirs([excluded_file, tts_location, time_report_tts_location])


def test():
    # music_play.random_play(musics_location='musics', times=3)
    from events import heart_beats
    heart_beats.time_reporting()
    return


if __name__ == '__main__':
    if len(sys.argv) < 2:
        test()
    else:
        arg = sys.argv[1]
        if arg == 'player':
            music_play.random_play(musics_location='musics', mode='commandline', times=50)
        elif arg == 'weather':
            events.weather_reporter()
        elif arg == 'test':
            test()

# TODO 实现带空格歌曲名字的mplayer播放
