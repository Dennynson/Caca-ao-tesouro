import pygame
import cores

def nomes():
    pygame.init()
    
    tela_nomes = pygame.display.set_mode((1000, 640))
    tela_nomes.fill(cores.preto)
    pygame.display.set_caption("Caça ao One Piece!")
    #carrega fontes personalizadas
    fonte = pygame.font.Font("onepiece.ttf", 50)

    jogador1 = ""
    jogador2 = ""

    digitando = True
    jogador = 1

    while(digitando):
        #atualiza a tela após cada jogador digitar
        tela_nomes.fill(cores.preto)

        # Mensagem para o jogador 1 ou jogador 2
        if (jogador == 1):
            mensagem = "Jogador 1, digite seu nome: " + jogador1
        else:
            mensagem = "Jogador 2, digite seu nome: " + jogador2

        texto = fonte.render(mensagem, True, cores.branco)
        tela_nomes.blit(texto, (50, 250))

        # Capturar eventos
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                digitando = False
                pygame.quit()
             # Captura das teclas pressionadas
            if (evento.type == pygame.KEYDOWN):
                if (evento.key == pygame.K_BACKSPACE):
                    if (jogador == 1):
                        jogador1 = jogador1[:-1]
                    else:
                        jogador2 = jogador2[:-1]
                elif (evento.key == pygame.K_RETURN):
                    # Se o jogador 1 terminou, passa para o jogador 2
                    if (jogador == 1):
                        jogador = 2
                    else:
                        # Quando o jogador 2 terminar, finalizar o input
                        digitando = False
                else:
                    # Adiciona o caractere ao nome do jogador correspondente
                    if (jogador == 1):
                        jogador1 += evento.unicode
                    else:
                        jogador2 += evento.unicode
        pygame.display.update()

    return jogador1, jogador2
