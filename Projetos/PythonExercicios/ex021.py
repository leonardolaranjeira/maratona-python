import pygame
print('Exercício 21')

# Faça um programa em python que abra e reproduza o áudio de um arquivo MP3.

pygame.mixer.init()
pygame.mixer.music.load('coisasestranhas.mp3')
pygame.mixer.music.play()
input()
pygame.event.wait()

# Desafio concluído!
