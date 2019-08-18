import time
import random
import pygame
import os
from Tools.log import logger

pygame.mixer.init()
pygame.init()


def random_play(musics_location=None):
    if not musics_location:
        musics_location = '../musics'
    musics = os.listdir(musics_location)
    logger.info('Musics:%s' % str(musics))
    music_locations = [os.path.join(musics_location, i) for i in musics if i.endswith(('.mp3', 'm4a'))]
    music_count = len(music_locations)
    ran_music = music_locations[random.randint(0, music_count - 1)]
    logger.info('Music To Be Played: ' + ran_music)
    try:
        track = pygame.mixer.music.load(ran_music)
        pygame.mixer.music.play()
    except Exception as e:
        logger.warning('Play Music Failed.Let us Do it Again. Msg:%s' % e)
        random_play(musics_location)
        return
    time.sleep(480)


if __name__ == '__main__':
    random_play()
