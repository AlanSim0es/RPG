import pygame
from pygame.locals import *

class Heroi(pygame.sprite.Sprite): #cria a classe sprite
    def __init__(self):
        pygame.sprite.Sprite.__init__(self) #inicia o objeto sprite
        self.sprites = []    #cria uma lista
        self.sprites.append(pygame.image.load('Sprites/attack1.png'))
        self.sprites.append(pygame.image.load('Sprites/attack2.png'))
        self.sprites.append(pygame.image.load('Sprites/attack3.png'))
        self.sprites.append(pygame.image.load('Sprites/attack4.png'))
        self.sprites.append(pygame.image.load('Sprites/attack5.png'))
        self.sprites.append(pygame.image.load('Sprites/attack6.png'))
        self.sprites.append(pygame.image.load('Sprites/attack7.png'))
        self.sprites.append(pygame.image.load('Sprites/attack8.png'))
        self.sprites.append(pygame.image.load('Sprites/attack9.png'))
        self.sprites.append(pygame.image.load('Sprites/attack10.png'))
        self.atual = 0 #estabelece a primeira imagem da lista como a padrão
        self.image = self.sprites[self.atual]
        self.image = pygame.transform.scale(self.image, (100 * 2, 100 * 2))
        self.rect= self.image.get_rect()
        self.rect.topleft = 50,200

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