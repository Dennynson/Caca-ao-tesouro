import pygame
import cores
import modulo

def manual():
    pygame.init()

    tela_manual = pygame.display.set_mode((1000, 640))
    tela_manual.fill(cores.branco)
    pygame.display.set_caption("Manual de Instruções")
    gomu = pygame.image.load("imagens/gomu.png").convert_alpha()
    gomu = pygame.transform.scale(gomu, (100, 100))
    buraco = pygame.image.load("imagens/buraco.png").convert_alpha()
    buraco = pygame.transform.scale(buraco, (100, 100))
    
    #carrega fontes personalizadas
    fonte = pygame.font.Font("onepiece.ttf", 100)
    fonte2 = pygame.font.SysFont("Times New Roman", 24)
    fonte3 = pygame.font.Font("onepiece.ttf", 50)
    fonte4 = pygame.font.Font("onepiece.ttf", 27)
    

    manual_logo = fonte.render("Manual", True, cores.preto)
    pontos = fonte3.render("+ 100 pontos cada", True, cores.preto)
    pontos_50 = fonte3.render("- 50 pontos cada", True, cores.preto)
    numeros = fonte2.render("--> Números (0 a 4) indicam a quantidade de Akumas no Mi ao redor!", True, cores.preto)
    jogador1 = fonte2.render("--> A vez do jogador 1 será indicada na cor azul!", True, cores.preto)
    jogador2 = fonte2.render("--> A vez do jogador 2 será indicada na cor vermelha!", True, cores.preto)
    vencedor = fonte2.render("--> O jogador que conseguir mais pontos ao final do jogo encontrará o One Piece e se", True, cores.preto)
    one_piece = fonte2.render("tornará o Rei dos Piratas!", True, cores.preto)
    voltar = fonte4.render("<<< Voltar", True, cores.preto)
    jogar = fonte4.render("Jogar >>>", True, cores.preto)
    
    
    rodando = True
    while rodando:
        tela_manual.blit(manual_logo, (400,50))
        tela_manual.blit(gomu, (150, 180))
        tela_manual.blit(pontos, (250, 200)) #texto de +100 pontos
        tela_manual.blit(buraco, (150, 270))
        tela_manual.blit(pontos_50, (250, 290)) #texto de -50 pontos
        tela_manual.blit(numeros, (150, 370))
        tela_manual.blit(jogador1,(150, 400) )
        tela_manual.blit(jogador2, (150, 430))
        tela_manual.blit(vencedor, (150, 460))
        tela_manual.blit(one_piece, (187, 490 ))
        botao_voltar = tela_manual.blit(voltar, (50, 600)) #botão de voltar ao menu
        botao_jogar = tela_manual.blit(jogar, (850, 600)) #botão de jogar

        for evento in pygame.event.get():
            if (evento.type == pygame.QUIT): #analisa condição de parada
                rodando = False
                pygame.quit()#fecha a janela
            if (evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1):
                pos_mouse = pygame.mouse.get_pos() #pega a posição do clique
                if(botao_voltar.collidepoint(pos_mouse)):
                    return modulo.menu()
                if(botao_jogar.collidepoint(pos_mouse)):
                    return pygame.quit()

        pygame.display.update()
        
    pygame.quit()


    