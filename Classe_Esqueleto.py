import pygame
from pygame.locals import *

class Esqueleto(pygame.sprite.Sprite):  # cria a classe sprite
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)  # inicia o objeto sprite
        self.sprites = []  # cria uma lista
        self.sprites.append(pygame.image.load('Sprites/Esqueleto1.png'))
        self.sprites.append(pygame.image.load('Sprites/Esqueleto2.png'))
        self.sprites.append(pygame.image.load('Sprites/Esqueleto3.png'))
        self.sprites.append(pygame.image.load('Sprites/Esqueleto4.png'))
        self.sprites.append(pygame.image.load('Sprites/Esqueleto5.png'))
        self.sprites.append(pygame.image.load('Sprites/Esqueleto6.png'))
        self.sprites.append(pygame.image.load('Sprites/Esqueleto7.png'))
        self.sprites.append(pygame.image.load('Sprites/Esqueleto8.png'))

        self.atual = 0
        self.image = self.sprites[self.atual]
        self.image = pygame.transform.scale(self.image, (100 * 2, 100 * 2))
        self.rect = self.image.get_rect()
        self.rect.topleft = 370, 200
        self.animar = False


    def atacar(self):
        self.animar = True

    def update(self):
        if self.animar == True:
            self.atual = self.atual + 0.5
            if self.atual >= len(self.sprites):
                self.atual = 0
                self.animar = False
            self.image = self.sprites[int(self.atual)]
            self.image = pygame.transform.scale(self.image, (100 * 2, 100 * 2))