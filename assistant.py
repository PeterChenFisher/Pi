from Tools import music_play
from events import schedules
import sys


def test():
    # music_play.reform_music_file_names(musics_location='musics')
    music_play.random_play(musics_location='musics')
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
