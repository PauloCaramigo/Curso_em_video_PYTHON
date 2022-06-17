# ENUNCIADO
# Faça um programa em Python que abra e reproduza o áudio de um arquivo

import playsound
import pygame

# playsound.playsound('Musica.mp3')


# Tbm pode ser feito pelo pygame
# Novo modelo para inicial um audio pelo pygame

pygame.mixer.init()
pygame.init()
pygame.mixer.music.load('musica.mp3')
pygame.mixer_music.play()
pygame.event.wait()
