import time
import sys
import random
import os
# import cv2
import threading

music_list = []

if __name__ == '__main__':
    from log import logger
    from DDingWarn import request_ding
elif __name__ != '__main__':
    from .log import logger
    from .DDingWarn import request_ding


# pygame.mixer.init()
# pygame.init()


def random_play(musics_location=None, mode='commandline', times=1):
    global music_list

    if not musics_location:
        os_platform = sys.platform
        if os_platform == 'Linux':
            musics_location = '../musics'
        elif os_platform == 'win32':
            musics_location = '..\musics'
        else:
            logger.warning('System Estimate Failed.Exit.')
            return 'System error'

    if music_list == []:

        musics = os.listdir(musics_location)
        music_locations = [os.path.join(musics_location, i).replace(' ', '\ ') for i in musics if
                           i.endswith(('.mp3', 'm4a'))]
        music_chains = read_song_list_via_linear_chain(os.path.join(musics_location, 'musics.txt'))
        music_locations.extend(music_chains)
        logger.info('All Musics :')
        for music_location in music_locations:
            logger.info(str(music_location))
        music_list = music_locations

    if mode == 'pygame':
        # player = play_a_song_via_pygame
        mode = 'commandline'
        player = play_a_song_via_commandline
    elif mode == 'commandline':
        player = play_a_song_via_commandline
    else:
        return 'Play Mode Error.'
    i = 0
    while i < times:
        ran_music = music_list[random.randint(0, len(music_list) - 1)]
        # logger.info('Music To Be Played: ' + ran_music)
        time.sleep(0.5)
        if not player(ran_music):
            logger.warning('Music: ' + ran_music)
            continue
        i += 1


def read_song_list_via_linear_chain(music_list_file_location=None):
    music_id_list = []
    net_ease_music_mother_linear_chain = 'https://music.163.com/song/media/outer/url?id='

    if music_list_file_location is None:
        os_platform = sys.platform
        if os_platform == 'Linux' or os_platform == 'linux':
            music_list_file_location = '../musics/musics.txt'  # TODO 换成绝对路径
        elif os_platform == 'win32':
            music_list_file_location = '..\musics\musics.txt'
        else:
            logger.warning('Judge System Failed.Exit.')
            return 'System error'

    with open(music_list_file_location, 'r', encoding='utf-8') as music_list_file:
        lines = music_list_file.readlines()
        for line in lines:
            if line.startswith('#') or line == '\n':
                continue
            if line.startswith('http://music.163.com/'):
                music_id = line.split('id=')[1].split('&')[0]
                music_linear_chain = net_ease_music_mother_linear_chain + str(music_id) + '.mp3'
            elif line.startswith('OriginalChain'):
                music_linear_chain = line.split(':')[1]
            else:
                music_id = line
                music_linear_chain = net_ease_music_mother_linear_chain + str(music_id) + '.mp3'

            music_id_list.append(music_linear_chain)
    return music_id_list


# def play_a_song_via_pygame(music):
#     try:
#         pygame.mixer.music.load(music)
#         pygame.mixer.music.play()
#         while (pygame.mixer.music.get_busy()):
#             time.sleep(1)
#             # if cv2.waitKey(1) & 0xFF == ord('q'):
#             #     break
#         return True
#     except Exception as e:
#         request_ding(result=['Play Music Failed.Let us Do it Again. Msg:%s' % e])
#         return False


def play_a_song_via_commandline(music):
    commandline = 'mplayer ' + music
    logger.info('The CommandLine is: ' + commandline)
    result = os.system(commandline)
    # logger.info('After Playing Music.')

    if result == 0:
        logger.info('Music Successfuly Played.')
        return True
    else:
        request_ding(result=['Failed to play the music.The music is %s' % music])
        return False


def waitKey():
    def wait_key():
        import socket
        so = socket.socket()
        return

    import socket
    so = socket.socket()
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
