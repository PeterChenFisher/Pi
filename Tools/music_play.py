import time
import sys
import random
import pygame
import os
# import cv2
import threading

if __name__ == '__main__':
    from log import logger
elif __name__ != '__main__':
    from .log import logger

pygame.mixer.init()
pygame.init()


def random_play(musics_location=None, mode='commandline', times=1):
    if not musics_location:
        os_platform = sys.platform
        if os_platform == 'Linux':
            musics_location = '../musics'
        elif os_platform == 'win32':
            musics_location = '..\musics'
        else:
            logger.warning('Judge System Failed.Exit.')
            return
    musics = os.listdir(musics_location)
    logger.info('Musics:%s' % str(musics))
    music_locations = [os.path.join(musics_location, i) for i in musics if i.endswith(('.mp3', 'm4a'))]
    ran_music = music_locations[random.randint(0, len(music_locations) - 1)]
    logger.info('Music To Be Played: ' + ran_music)
    if mode == 'pygame':
        for i in range(0, times):
            if not play_a_song(ran_music):
                random_play(musics_location, mode=mode)
    elif mode == 'commandline':
        for i in range(0, times):
            if not play_a_song_via_commandline(ran_music):
                random_play(musics_location, mode=mode)


def play_a_song(music):
    try:
        pygame.mixer.music.load(music)
        pygame.mixer.music.play()
        while (pygame.mixer.music.get_busy()):
            time.sleep(1)
            # if cv2.waitKey(1) & 0xFF == ord('q'):
            #     break
        return True
    except Exception as e:
        logger.warning('Play Music Failed.Let us Do it Again. Msg:%s' % e)
        return False


def play_a_song_via_commandline(music):
    commandline = 'mplayer ' + music
    logger.info('The CommandLine is: ' + commandline)
    os.system(commandline)
    return True


def waitKey():
    def wait_key():
        return

    threading.Thread(target=wait_key)
    return


if __name__ == '__main__':
    random_play(times=10)
    # random_play(mode='commandline')
