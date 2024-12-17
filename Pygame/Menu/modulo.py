import pygame
import cores
from Menu import Manual
from Menu import creditos

def menu():
    pygame.init()
    
    tela_menu = pygame.display.set_mode((1000, 640))
    tela_menu.fill(cores.preto)
    pygame.display.set_caption("Caça ao One Piece!")
    #carrega fontes personalizadas
    fonte = pygame.font.Font("onepiece.ttf", 100)
    fonte3 = pygame.font.Font("onepiece.ttf", 50)

    welcome = fonte.render("Caça ao One Piece", True, cores.branco)
    jogar = fonte3.render("Jogar", True, cores.branco)
    manual = fonte3.render("Manual", True, cores.branco)
    credito = fonte3.render("Créditos", True, cores.branco)
    sair = fonte3.render("Sair", True, cores.branco)
    

    rodando = True
    while rodando:
        tela_menu.blit(welcome, (200,75)) #desenha logo
        botao_jogar = tela_menu.blit(jogar, (450,300)) 
        botao_manual = tela_menu.blit(manual, (450,350))
        botao_creditos = tela_menu.blit(credito, (450,400))
        botao_sair = tela_menu.blit(sair, (450,450))
        pygame.display.update()
        
        for evento in pygame.event.get():
            if (evento.type == pygame.QUIT): #analisa condição de parada
                rodando = False
                pygame.quit()#fecha a janela
                return True
            #analisa qual botão o usuário escolheu
            if (evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1):
                pos_mouse = pygame.mouse.get_pos() #pega a posição do clique
                if(botao_jogar.collidepoint(pos_mouse)):
                    return pygame.quit()
                if(botao_manual.collidepoint(pos_mouse)):
                    return Manual.manual()
                if(botao_creditos.collidepoint(pos_mouse)):
                    return creditos.creditos()
                if(botao_sair.collidepoint(pos_mouse)):
                    return pygame.quit()
    pygame.quit()