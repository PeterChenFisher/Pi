from Tools import music_play
from events import schedules
import sys

if __name__ == '__main__':
    arg = sys.argv[1]
    print(arg)
    print(type(arg))
    if arg == 'player':
        music_play.random_play(musics_location='musics', mode='commandline', times=50)
    elif arg == 'weather':
        schedules.weather_reporter()
