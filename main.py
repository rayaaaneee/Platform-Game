from time import sleep
import pygame
import sys
from pygame.locals import *
from pygame import *
from sys import exit
from random import randint
from mainCharacter import MainCharacter

pygame.init()
# met le screen en plein ecran windowed
screen_width, screen_height = pygame.display.Info(
).current_w, pygame.display.Info().current_h - 60

# Création de la fenêtre
screen = pygame.display.set_mode((screen_width, screen_height))

clock = pygame.time.Clock()

sprites = pygame.sprite.Group()


def __main__():
    character = MainCharacter(50, 600)
    # Mettre un background au jeu

    background = pygame.image.load(
        "asset/img/background/background1.jpg")
    floor = pygame.image.load("asset/img/world/floor2.png")
    floor = pygame.transform.scale(floor, (screen_width,
                                           floor.get_height()))
    background = background.convert()

    screen.blit(background, (0, 0))

    # Placer floor en bas de l'écran et le redimensionner pour qu'il prenne toute la largeur de l'écran sans modifier sa hauteur
    screen.blit(floor, (0, screen_height - floor.get_height()))

    sprites.add(character)

    while True:

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        # Supprimer les sprites pour les remettre a jour
        '''sprites.clear(screen, background) '''

        #  On supprime la position du personnage pour le remettre a jour
        sprites.update()

        # On supprime tous les sprites pour les remettre a jour
        sprites.draw(screen)

        # On met a jour l'écran
        pygame.display.update()


if __name__ == "__main__":
    __main__()
