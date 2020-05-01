# import json
# from config import *
#
# pure_music_list_file = Muscis.pure_musics_file_location
import json

pure_music_list_file = '../musics/PureMusics.json'

net_ease_music_mother_linear_chain = 'https://music.163.com/song/media/outer/url?id='


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


def reformat_cloud_musics():
    with open('../musics/CloudMusics.txt', 'r+', encoding='utf-8')as fo:
        title = fo.readline()
        lines = fo.readlines()
        # length = int(len(lines) / 2)
        # # music_couple = [[lines.pop(0), lines.pop(0)] for i in range(0, length)]
        music_couple = [[lines.pop(0), lines.pop(0)] for i in range(0, int(len(lines) / 2))]
        cloud_musics = {}
        for couple in music_couple:
            id = couple[1].split('id=')[1].split('&')[0]
            cloud_musics[couple[0].replace('# ', '')] = net_ease_music_mother_linear_chain + id
    with open('../musics/CloudMuiscs.json', 'w+', encoding='utf-8') as fo:
        json.dump(cloud_musics, fo, indent='  ', ensure_ascii=False)
    print(music_couple)
    print(cloud_musics)


# reformat_pure_musics()
reformat_cloud_musics()
