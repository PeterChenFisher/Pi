from Spiders import weather_extractor
from Tools import Text2Speech, music_play
import time


def music_player():
    return


def weather_reporter():
    weather_message = weather_extractor.get_weather()['data']
    date = time.strftime('%Y-%m-%d', time.localtime(time.time()))
    weather_speech_file = Text2Speech.text2speech(text=weather_message, file_name=date)
    music_play.play_a_song(weather_speech_file)
    return


if __name__ == '__main__':
    weather_reporter()
