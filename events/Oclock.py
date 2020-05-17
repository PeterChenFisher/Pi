from . import heart_beats
import time
from tools import music_play


def time_report_morning_oclock():
    music_time = 10
    for i in range(0, music_time):
        music_play.random_play()
        now = time.localtime()
        # hour, minute = now[3], now[4]
        heart_beats.time_reporting()

    return
