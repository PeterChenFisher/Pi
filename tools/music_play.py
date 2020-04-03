import time
import random
from .log import logger
from .DDingWarn import request_ding
from .ip_update import check_network_status
from config import *

local_music_list = []
pure_music_list = []
cloud_music_list = []

reload_sig = True


def read_pure_music(musics_location=None):
    global pure_music_list

    if not musics_location:
        musics_location = pure_musics_location

    if not pure_music_list:
        musics = os.listdir(musics_location)
        pure_music_list = [os.path.join(musics_location, i).replace(' ', '\ ') for i in musics if
                           i.endswith(('.mp3', 'm4a'))]
        logger.info('纯音乐列表 :')
        for music_location in pure_music_list:
            logger.info(str(music_location))
    return


def read_musics(musics_location=None):
    global local_music_list

    if not musics_location:
        os_platform = sys.platform
        if os_platform == 'linux' or os_platform == 'Linux':
            musics_location = 'musics'
        elif os_platform == 'win32':
            musics_location = 'musics'
        else:
            logger.warning('System Estimate Failed.Exit.')
            return 'System error'

    if not local_music_list:
        musics = os.listdir(musics_location)
        music_locations = [os.path.join(musics_location, i).replace(' ', '\ ') for i in musics if
                           i.endswith(('.mp3', 'm4a'))]
        logger.info('本地音乐：')
        for music_location in music_locations:
            logger.info(f' {music_location}')
        local_music_list = music_locations

    return


def read_cloud_music(music_list_file_location=None):
    global cloud_music_list

    net_ease_music_mother_linear_chain = 'https://music.163.com/song/media/outer/url?id='

    if music_list_file_location is None:
        music_list_file_location = cloud_music_location

    with open(music_list_file_location, 'r', encoding='utf-8') as music_list_file:
        lines = music_list_file.readlines()
        for line in lines:
            if '#' in line or line == '\n':
                continue
            if line.startswith('http://music.163.com/'):
                music_id = line.split('id=')[1].split('&')[0]
                music_linear_chain = net_ease_music_mother_linear_chain + str(music_id) + '.mp3'
            elif line.startswith('OriginalChain'):
                music_linear_chain = line.split(':')[1]
            else:
                music_id = line
                music_linear_chain = net_ease_music_mother_linear_chain + str(music_id) + '.mp3'

            cloud_music_list.append(music_linear_chain)
    logger.info('云音乐链接：')
    for music_link in cloud_music_list:
        logger.info(f' {music_link}')
    return cloud_music_list


def random_play(musics_location=None, method='commandline', times=1, mode=normal_music):
    # TODO 处理变量 musics_location
    global local_music_list, pure_music_list, cloud_music_list, reload_sig

    if not local_music_list or not pure_music_list or not cloud_music_list or reload_sig:
        read_musics()
        read_pure_music()
        read_cloud_music()
        reload_sig = False

    if mode == normal_music:
        musics = local_music_list + cloud_music_list if check_network_status() else local_music_list
    elif mode == pure_music:
        musics = pure_music_list
    elif mode == mix_music:
        musics = (pure_music_list + local_music_list + cloud_music_list) if check_network_status() else (
                pure_music_list + local_music_list)
    else:
        request_ding(result=['播放模式设置错误', '请检查代码，重新设置播放模式'])
        return
    for i in range(0, times):
        ran_music = musics[random.randint(0, len(musics) - 1)]
        time.sleep(0.5)
        pi_mplayer(ran_music)
    logger.info(f'随机音乐播放器播放结束')


def reload_sig_state_switch():
    global reload_sig
    reload_sig = True


def pi_mplayer(music):
    commandline = 'mplayer ' + str(music)
    logger.info('命令行：' + commandline)
    stt = time.time()
    result = os.system(commandline)
    time_interval = time.time() - stt
    if time_interval < 60:
        request_ding(result=['音乐播放时常不正常'])

    if result == 0:
        logger.info('音乐播放成功.')
        return True
    else:
        request_ding(result=[f'音乐播放失败！这首歌是： {music}'])
        return False

# import os
# import cv2
# import pygame

# pygame.mixer.init()
# pygame.init()


# def pygame_player(music):
#     try:
#         pygame.mixer.music.load(music)
#         pygame.mixer.music.play()
#         while (pygame.mixer.music.get_busy()):
#             time.sleep(1)
#         return True
#     except Exception as e:
#         request_ding(result=[f'Py Game 播放音乐失败，歌曲：{music} 错误信息：{e}'])
#         return False

# def py_game_player(file):
#     pygame.mixer.init()
#     print("播报天气")
#     pygame.mixer.music.load(file)
#     pygame.mixer.music.play(loops=1, start=0.0)
#     print("播放音乐")
#     while True:
#         if pygame.mixer.music.get_busy() == 0:
#             # Linux 配置定时任务要设置绝对路径
#             mp3 = "/home/pi/alarmClock/" + str(random.randint(1, 6)) + ".mp3"
#             # mp3 = str(random.randint(1, 6)) + ".mp3"
#             pygame.mixer.music.load(mp3)
#             pygame.mixer.music.play(loops=1, start=0.0)
#             break
#     while True:
#         if pygame.mixer.music.get_busy() == 0:
#             print("播报完毕，起床啦")
#             break
