import json
from config import *
import config

pure_music_list_file = '../musics/PureMusics.json'

net_ease_music_mother_linear_chain = 'https://music.163.com/song/media/outer/url?id='


def reformat_cloud_musics():
    music_location = origin_cloud_music_file_location
    with open(music_location, 'r+', encoding='utf-8')as fo:
        lines = fo.readlines()
    cloud_musics = {}
    for line in lines:
        cloud_musics[line.split('--')[0]] = net_ease_music_mother_linear_chain + \
                                            line.split('--')[1].split('id=')[1].split('&')[0]

    with open(config.cloud_music_file_location, 'w+', encoding='utf-8') as fo:
        json.dump(cloud_musics, fo, indent='  ', ensure_ascii=False)


def reformat_pure_musics():
    with open(pure_music_list_file, 'r+', encoding='utf-8') as fo:
        # print(fo.readlines())
        pure_musics = json.load(fp=fo)
        print(pure_musics)
        for key, value in pure_musics.items():
            value = net_ease_music_mother_linear_chain + value.replace('/song?id=', '')
            pure_musics[key] = value

    print(pure_musics)
    with open('../musics/PureMusics.json', 'w+', encoding='utf-8') as fo:
        json.dump(pure_musics, fo, indent='  ', ensure_ascii=False)
    return

# reformat_pure_musics()
# reformat_cloud_musics()
