from tools import music_play
from events import events
import sys


def test():
    music_play.random_play(musics_location='musics', times=3)
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