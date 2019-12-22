from Tools.log import logger
from Tools.Text2Speech import text2speech
from Tools.music_play import play_a_song_via_pygame
from Tools.music_play import play_a_song_via_commandline
import time

def WholeTimeReporting():
    hour = time.localtime()[3]
    text = '现在是%d点整'%hour
    text_voice = text2speech(text,file_name='TimeReport_%d'%hour)
    play_a_song_via_pygame(text_voice)
    time.sleep(3)
    play_a_song_via_commandline(text_voice)
    print(text_voice)
    return

if __name__ == '__main__':
    WholeTimeReporting()