import time
import json
import random
from . import log
from .DDingWarn import request_ding
from .ip_update import check_network_status
from config import *

local_musics = {}
pure_musics = {}
cloud_musics = {}

reload_sig = True
logger = log.logger


def read_pure_music(musics_location=None):
    global pure_musics

    if not musics_location:
        musics_location = pure_musics_file_location

    with open(musics_location, 'r+', encoding='utf-8') as fo:
        pure_musics = json.load(fp=fo)
    logger.info('纯音乐列表：')
    for key, value in pure_musics.items():
        logger.info(f'    {key}:{value}')


def read_cloud_music(musics_location=None):
    global cloud_musics

    if not musics_location:
        musics_location = cloud_music_file_location

    with open(musics_location, 'r+', encoding='utf-8') as fo:
        cloud_musics = json.load(fp=fo)
    logger.info('云音乐链接：')
    for music, music_link in cloud_musics.items():
        logger.info(f'    {music}:{music_link}')
    return cloud_musics


def read_local_musics(musics_location=None):
    global local_musics

    if not musics_location:
        musics_location = local_music_location
    musics = os.listdir(musics_location)
    local_musics = {i: os.path.join(musics_location, i).replace(' ', '\ ').replace('(', '\(').replace(')', '\)') for
                    i in musics if i.endswith(('.mp3', 'm4a', 'flac'))}
    logger.info('本地音乐：')
    for music, music_location in local_musics.items():
        logger.info(f'    {music}:{music_location}')


def random_play(musics_location=None, method='commandline', times=1, mode=normal_music_mode):
    # TODO 处理变量 musics_location
    global local_musics, pure_musics, cloud_musics, reload_sig
    musics = {}

    if not local_musics or not pure_musics or not cloud_musics or reload_sig:
        read_local_musics()
        read_pure_music()
        read_cloud_music()
        reload_sig = False

    if mode == normal_music_mode:
        musics.update(local_musics)
        if check_network_status(): musics.update(cloud_musics)
        # musics = local_musics + cloud_musics if check_network_status() else local_musics
    elif mode == pure_musics_mode:
        musics = pure_musics
    elif mode == mix_music_mode:
        musics.update(local_musics)
        if check_network_status():
            musics.update(pure_musics)
            musics.update(cloud_musics)
        # musics = (pure_musics + local_musics + cloud_musics) if check_network_status() else (
        #         pure_musics + local_musics)
    else:
        request_ding(result=['播放模式设置错误', '请检查代码，重新设置播放模式'])
        return
    for i in range(0, times):
        music_names = list(musics.keys())
        ran_music = music_names[random.randint(0, len(musics) - 1)]
        logger.info(f'获取到的随机音乐：{ran_music}')
        time.sleep(0.5)
        pi_mplayer(musics[ran_music])
    logger.info(f'随机音乐播放器播放结束')


def reload_sig_state_switch():
    global reload_sig
    reload_sig = True


def pi_mplayer(music):
    commandline = 'mplayer ' + str(music)
    logger.info('命令行：' + commandline)
    stt = time.time()
    result = os.system(commandline)
    edt = time.time()
    play_time = edt - stt
    if play_time <= 2:
        request_ding(result=['音乐播放时长异常：', music])

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
