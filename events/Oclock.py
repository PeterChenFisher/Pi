from . import heart_beats
import time
from tools import music_play


def time_report_morning_clock():
    music_time = 10
    for i in range(0, music_time):
        music_play.random_play()
        heart_beats.time_reporting()
    return
