import time
import random
import pygame
import os

pygame.mixer.init()
pygame.init()


def random_play():
    musics_location = '../musics'
    musics = os.listdir(musics_location)
    music_locations = [os.path.join(musics_location, i) for i in musics if i.endswith(('.mp3', 'm4a'))]
    music_count = len(music_locations)
    ran_music = music_locations[random.randint(0, music_count)]
    print(ran_music)
    track = pygame.mixer.music.load(ran_music)
    pygame.mixer.music.play()
    time.sleep(1000)


if __name__ == '__main__':
    random_play()
