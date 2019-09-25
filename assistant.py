from Tools import music_play
from events import schedules
import sys


def test():
    music_play.random_play(musics_location='musics', times=3)
    return


if __name__ == '__main__':
    if len(sys.argv) < 2:
        test()
    else:
        arg = sys.argv[1]
        print(arg)
        print(type(arg))
        if arg == 'player':
            music_play.random_play(musics_location='musics', mode='commandline', times=50)
        elif arg == 'weather':
            schedules.weather_reporter()
        elif arg == 'test':
            test()
