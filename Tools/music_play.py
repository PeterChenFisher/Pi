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
            logger.warning('System Estimate Failed.Exit.')
            return 'System error'

    musics = os.listdir(musics_location)
    music_locations = [os.path.join(musics_location, i) for i in musics if i.endswith(('.mp3', 'm4a'))]
    music_chains = read_song_list_via_linear_chain(os.path.join(musics_location, 'musics.txt'))
    music_locations.extend(music_chains)
    logger.info('All Musics : %s')
    for music_location in music_locations:
        logger.info(str(music_location))

    if mode == 'pygame':
        player = play_a_song_via_pygame
    elif mode == 'commandline':
        player = play_a_song_via_commandline
    else:
        return 'Play Mode Error.'
    i = 0
    while i < times:
        ran_music = music_locations[random.randint(0, len(music_locations) - 1)]
        # logger.info('Music To Be Played: ' + ran_music)
        time.sleep(0.5)
        player(ran_music)
        i += 1


def read_song_list_via_linear_chain(music_list_file_location=None):
    music_id_list = []
    net_easy_music_mother_linear_chain = 'https://music.163.com/song/media/outer/url?id='

    if music_list_file_location is None:
        os_platform = sys.platform
        if os_platform == 'Linux':
            music_list_file_location = '../musics/musics.txt'
        elif os_platform == 'win32':
            music_list_file_location = '..\musics\musics.txt'
        else:
            logger.warning('Judge System Failed.Exit.')
            return 'System error'
    with open(music_list_file_location, 'r', encoding='utf-8') as music_list_file:
        lines = music_list_file.readlines()
        for line in lines:
            if line.startswith('#') or line == '/n':
                continue
            if line.startswith('http://music.163.com/'):
                music_id = line.split('id=')[1].split('&')[0]
                muisc_linear_chain = net_easy_music_mother_linear_chain + str(music_id) + '.mp3'
            elif line.startswith('OriginlChain'):
                muisc_linear_chain = line.split(':')[1]
            else:
                music_id = line
                muisc_linear_chain = net_easy_music_mother_linear_chain + str(music_id) + '.mp3'

            music_id_list.append(muisc_linear_chain)

    return music_id_list


def play_a_song_via_pygame(music):
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
    result = os.system(commandline)
    # logger.info('After Playing Music.')

    if result == 0:
        logger.info('Music Successfuly Played.')
        return True
    else:
        logger.warning('Failed to play the music.')
        return False


def waitKey():
    def wait_key():
        return

    threading.Thread(target=wait_key)
    return


def reform_music_file_names(musics_location='.\musics'):
    musics = os.listdir(musics_location)
    music_locations = [os.path.join(musics_location, i) for i in musics if i.endswith(('.mp3', 'm4a'))]
    for location in music_locations:
        os.rename(location, location.replace(' ', ''))
    return


if __name__ == '__main__':
    random_play(times=10)
    # read_song_list_via_linear_chain()
    # random_play(mode='commandline')
