import pygame

class Goblin(pygame.sprite.Sprite):  # cria a classe sprite
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)  # inicia o objeto sprite
        self.sprites = []  # cria uma lista
        self.sprites.append(pygame.image.load('Sprites/Goblin1.png'))
        self.sprites.append(pygame.image.load('Sprites/Goblin2.png'))
        self.sprites.append(pygame.image.load('Sprites/Goblin3.png'))
        self.sprites.append(pygame.image.load('Sprites/Goblin4.png'))
        self.sprites.append(pygame.image.load('Sprites/Goblin5.png'))
        self.sprites.append(pygame.image.load('Sprites/Goblin6.png'))
        self.sprites.append(pygame.image.load('Sprites/Goblin7.png'))
        self.sprites.append(pygame.image.load('Sprites/Goblin8.png'))
        self.atual = 0  # estabelece a primeira imagem da lista como a padrão
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