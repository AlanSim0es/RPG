import pygame  # importa a biblioteca de jogos
from pygame.locals import *  # importa funções da pasta locals
from sys import exit  # função que usada pra fechar a janela
import random as rnd
import Classe_Heroi
import Classe_Goblin

pygame.init()  # inicia funções e variaveis do pygame
largura = 640
altura = 480
hp_heroi = 100
hp_inimigo = 100
dano_causado = 0
fonte = pygame.font.SysFont('arial', 25, True, False)  # função para exibir texto
caixa_opcoes = pygame.font.SysFont('arial', 25, True, False)  # função para exibir texto

tela = pygame.display.set_mode((largura, altura))  # define o tamanho da janela do jogo

pygame.display.set_caption('Socos e Pontapés')
relogio = pygame.time.Clock()  # define os frames do jogo

todas_as_sprites = pygame.sprite.Group()
heroi = Classe_Heroi.Heroi()
goblin = Classe_Goblin.Goblin()
todas_as_sprites.add(heroi, goblin)

while True:
    relogio.tick(30)  # define o frame rate
    tela.fill((0, 0, 0))  # cor de fundo
    titulo = f'Socos e pontapés'  # formula do texto que mostra o HP do heroi
    formatado_titulo = fonte.render(titulo, False, (232, 228, 5))
    inicar = f'Iniciar Aventura'  # formula do texto que mostra o HP do heroi
    formatado_iniciar_aventura = fonte.render(inicar, False, (255, 255, 255))
    mensagem_inicial = f'Aperte qualquer tecla para iniciar'
    formatado_mensagem_inicial = fonte.render(mensagem_inicial, False, (255, 255, 255))

    for event in pygame.event.get():
        if event.type == QUIT:  # fecha o game
            pygame.quit()
            exit()
        if event.type == KEYDOWN:
            if event.key != K_ESCAPE:
                while hp_heroi > 0 or hp_inimigo > 0:
                    relogio.tick(30)  # define o frame rate
                    tela.fill((0, 0, 0))  # cor de fundo
                    mostrar_hp_heroi = f'HP {(hp_heroi / 10):.0f}'  # formula do texto que mostra o HP do heroi
                    formatado_mostrar_hp_heroi = fonte.render(mostrar_hp_heroi, False, (255, 255, 255))  # formatação HP
                    mostrar_hp_inimigo = f'HP {(hp_inimigo / 10):.0f}'  # formula do texto que mostra o HP do inimigo
                    formatado_mostrar_hp_inimigo = fonte.render(mostrar_hp_inimigo, False, (255, 255, 255))
                    opcao_q = f'Q - 4 PODER \n 3 DANO \n -1 VIDA'
                    formatado_opcao_q = fonte.render(opcao_q, False, (255, 255, 255))
                    opcao_w = f'W - 1-6 PODER \n 1-6 DANO'
                    formatado_opcao_w = fonte.render(opcao_w, False, (255, 255, 255))
                    opcao_e = f'E - 1-3 PODER \n 0-10 DANO'
                    formatado_opcao_e = fonte.render(opcao_e, False, (255, 255, 255))
                    mostrador_dano = f'{dano_causado:.0f}'
                    formatado_mostrador_dano = fonte.render(mostrador_dano, False, (255, 0, 0))

                    for event in pygame.event.get():
                        if event.type == QUIT:  # fecha o game
                            pygame.quit()
                            exit()

                        todas_as_sprites.draw(tela)
                        if event.type == KEYDOWN:  # reconhece o pressionar da tecla
                            if event.key == K_q:  # usa a tecla q para o cabeçada
                                pow_soco_inimigo = rnd.randint(1, 6)
                                if pow_soco_inimigo > 4:
                                    dano_inimigo = rnd.randint(1, 6)
                                    hp_heroi -= dano_inimigo
                                    goblin.atacar()
                                else:
                                    hp_inimigo -= 30
                                dano_causado = (3)
                                hp_heroi -= 10
                                heroi.atacar()

                            elif event.key == K_w:
                                pow_soco_inimigo = rnd.randint(1, 6)
                                pow_soco = rnd.randint(1, 6)
                                if pow_soco_inimigo > pow_soco:
                                    dano_inimigo = rnd.randint(1, 6) * 10
                                    hp_heroi -= dano_inimigo
                                    dano_causado = (dano_inimigo / 10)
                                    goblin.atacar()

                                else:
                                    dano_heroi = 0
                                dano_heroi = rnd.randint(1, 6) * 10
                                hp_inimigo -= dano_heroi
                                dano_causado = (dano_heroi / 10)
                                heroi.atacar()

                            elif event.key == K_e:
                                pow_soco_inimigo = rnd.randint(1, 6)
                                pow_soco = rnd.randint(1, 3)
                                if pow_soco_inimigo > pow_soco:
                                    dano_causado = rnd.randint(1, 6) * 10
                                    hp_heroi -= dano_causado
                                    goblin.atacar()

                                else:
                                    dano_heroi = 0
                                dano_heroi = rnd.randint(0, 10) * 10
                                hp_inimigo -= dano_heroi
                                dano_causado = (dano_heroi / 10)
                                heroi.atacar()

                    # vida dos personagens, o comando draw.rect cria um retangulo com os parametros cor((R,G,B))
                    # e plano cartesiano rect (eixo x, eixo y (negativo), largura, altura)
                    pygame.draw.line(tela, (255, 255, 255), (0, 350), (largura, 350), 5)
                    pygame.draw.rect(tela, ((18, 181, 21)), (120, 100, hp_heroi, 20))
                    pygame.draw.rect(tela, ((0, 0, 252)), (420, 100, hp_inimigo, 20))  # linha da caixa de texto
                    tela.blit(formatado_mostrar_hp_heroi, (120, 70))
                    tela.blit(formatado_mostrar_hp_inimigo, (420, 70))
                    tela.blit(formatado_opcao_q, (50, 350))
                    tela.blit(formatado_opcao_w, (50, 380))
                    tela.blit(formatado_opcao_e, (50, 410))
                    tela.blit(formatado_mostrador_dano, ((largura / 2), (altura / 2)))
                    todas_as_sprites.draw(tela)
                    todas_as_sprites.update()
                    pygame.display.flip()

            hp_heroi = 100
            hp_inimigo = 100

    # vida dos personagens, o comando draw.rect cria um retangulo com os parametros cor((R,G,B))
    # e plano cartesiano rect (eixo x, eixo y (negativo), largura, altura)
    pygame.draw.rect(tela, ((37, 18, 161)), (180, 100, 300, 50))
    tela.blit(formatado_iniciar_aventura, (220, 100))
    tela.blit(formatado_titulo, (200, 50))
    tela.blit(formatado_mensagem_inicial, (100, 300))
    pygame.display.flip()


