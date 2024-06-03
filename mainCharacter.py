import pygame
from useful import *
from threading import Timer


class MainCharacter(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)

        self.clock = pygame.time.Clock()

        self.image = pygame.image.load("asset/img/sprite/walk/right/8.png")
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.jump_speed = 1.2  # vitesse initiale du saut
        self.jump_height = 90  # hauteur maximale du saut
        self.is_jumping = False  # indique si le personnage est en train de sauter
        # agrandir l'image car elle fait 20/20
        self.i = 0

        self.imageWidth = 90
        self.imageHeight = 90
        self.indexImg = 1

        self.oldDirection = None
        self.indexWalk = 0

    def jump(self):
        self.is_jumping = True
        print("jump" + str(self.i))
        self.i += 1
        for i in range(0, self.jump_height):
            self.goUp()
        for i in range(0, self.jump_height):
            self.goDown()
        self.is_jumping = False

    def goUp(self):
        self.rect.y -= 1

    def goDown(self):
        self.rect.y += 1

    def advance(self, speed, speedImg, key):
        if key == "left":
            if self.oldDirection == "right" and not self.is_jumping:
                self.image = pygame.image.load(
                    "asset/img/sprite/walk/right/" + str(self.indexImg) + ".png")
            elif (self.oldDirection == "left" and not self.is_jumping):
                self.image = pygame.image.load(
                    "asset/img/sprite/walk/left/" + str(self.indexImg) + ".png")
                self.rect.x -= speed
                self.oldDirection = "left"
        elif key == "right":
            if self.oldDirection == "left" and not self.is_jumping:
                self.image = pygame.image.load(
                    "asset/img/sprite/walk/left/" + str(self.indexImg) + ".png")
            elif (self.oldDirection == "right" and not self.is_jumping):
                self.image = pygame.image.load(
                    "asset/img/sprite/walk/right/" + str(self.indexImg) + ".png")
            self.rect.x += speed
            self.oldDirection = "right"
        if (self.indexWalk == speedImg - 1):
            self.indexImg = (self.indexImg + 1) % 8
        self.indexWalk = (self.indexWalk + 1) % 5

    def walk(self, key):
        self.advance(3.5, 5, key)

    def run(self, key):
        self.advance(6, 1, key)

    def update(self):
        keys = pygame.key.get_pressed()
        key = None

        if keys[pygame.K_LEFT] or keys[pygame.K_RIGHT]:
            if keys[pygame.K_LEFT]:
                self.oldDirection = "left"
                key = "left"
            elif keys[pygame.K_RIGHT]:
                self.oldDirection = "right"
                key = "right"

            if keys[pygame.K_RSHIFT]:
                self.run(key)
            else:
                self.walk(key)
        else:
            if self.oldDirection == "left":
                self.image = pygame.image.load(
                    "asset/img/sprite/walk/left/8.png")
            else:
                self.image = pygame.image.load(
                    "asset/img/sprite/walk/right/8.png")

        if keys[pygame.K_SPACE] and not self.is_jumping:
            self.jump()

        self.image = pygame.transform.scale(
            self.image, (self.imageWidth, self.imageHeight))
