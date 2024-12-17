import pygame
import random
import cores
import modulo
from Menu import nomes
        
def tabuleiro(tela, num):
    if (num == 1): #desenha quadrados brancos no fundo mais escuro
        for x in range(160, 640, 160):
            pygame.draw.rect(tela, cores.branco, (x, 0, 2, 640), 0)
        for y in range(160, 640, 160):
            pygame.draw.rect(tela, cores.branco, (0, y, 640, 2), 0)
    else:
        for x in range(160, 640, 160):
            pygame.draw.rect(tela, cores.preto, (x, 0, 2, 640), 0)
        for y in range(160, 640, 160):
            pygame.draw.rect(tela, cores.preto, (0, y, 640, 2), 0)

def main():
    sair = modulo.menu()
    if(not sair): #verifica se usuário não apertou em sair
            jogador1, jogador2 = nomes.nomes() #recebe os nomes dos jogadores

            pygame.init()
            largura = 1000
            altura = 640
            fonte = pygame.font.SysFont("Comic Sams MS", 80)
            fonte2 = pygame.font.SysFont("Times New Roman", 27)

            tela = pygame.display.set_mode((largura, altura))
            pygame.display.set_caption("Caça ao One Piece!")

            # Define imagem de fundo e música
            num = random.randint(1, 3)
            if (num == 1):
                bg = pygame.image.load('imagens/mugiwaras.png').convert_alpha()
                bg = pygame.transform.scale(bg, (640, altura))
                pygame.mixer.music.load('audios/overtaken.mp3')
                pygame.mixer.music.play(-1)
            elif (num == 2):
                bg = pygame.image.load('imagens/wanoII.jpg').convert_alpha()
                bg = pygame.transform.scale(bg, (640, altura))
                pygame.mixer.music.load('audios/Wano.mp3')
                pygame.mixer.music.play(-1)
            elif (num == 3):
                bg = pygame.image.load('imagens/leme.jpeg').convert_alpha()
                bg = pygame.transform.scale(bg, (640, altura))
                pygame.mixer.music.load('audios/fiereattack.mp3')
                pygame.mixer.music.play(-1)

            # Cria tabuleiro virtual com zeros
            conteudo_bloco = [[None for i in range(4)] for j in range(4)]

            # Coloca os tesouros
            num_tesouros = 0
            while (num_tesouros < 6):
                i = random.randint(0, 3)
                j = random.randint(0, 3)

                if conteudo_bloco[i][j] is None: 
                    conteudo_bloco[i][j] = "X"
                    num_tesouros += 1
            
            #conta os tesouros em cada célula
            for i in range(4):
                for j in range(4):
                    tesouros = 0
                    if (conteudo_bloco[i][j] == "X"):
                        continue
                    if (i > 0 and conteudo_bloco[i - 1][j] == "X"):  # Célula acima
                        tesouros += 1
                    if (i < 3 and conteudo_bloco[i + 1][j] == "X"):  # Célula abaixo
                        tesouros += 1
                    if (j > 0 and conteudo_bloco[i][j - 1] == "X"):  # Célula à esquerda
                        tesouros += 1
                    if (j < 3 and conteudo_bloco[i][j + 1] == "X"):  # Célula à direita
                        tesouros += 1

                    conteudo_bloco[i][j] = str(tesouros)

            # Cria os buracos
            num_buracos = 0
            while (num_buracos < 3):
                i = random.randint(0, 3)
                j = random.randint(0, 3)

                if (conteudo_bloco[i][j] == "X" or conteudo_bloco[i][j] == "Y"):
                    continue
                
                conteudo_bloco[i][j] = "Y"
                num_buracos += 1
                

            # Cria uma matriz para controlar a visualização do conteúdo das células
            bloco_revelado = [[False for i in range(4)] for j in range(4)]

            run = True
            jogador_1 = True
            jogador_2 = False
            cont1 = 0
            cont2 = 0
            contblocos = 0

            # Loop principal do jogo
            while (run):
                for evento in pygame.event.get():
                    if (evento.type == pygame.QUIT):
                        run = False

                    # Desenhar o fundo e o tabuleiro
                    tela.blit(bg, (0, 0))
                    tabuleiro(tela, num)

                    if (evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1):
                        mouse_x, mouse_y = evento.pos
                        celula_x = mouse_x // 160
                        celula_y = mouse_y // 160

                        # Clicou fora do tabuleiro
                        if (celula_x > 3):
                            continue

                        # Entra no if se a célula foi clicada pela primeira vez
                        if (not bloco_revelado[celula_x][celula_y]):
                            bloco_revelado[celula_x][celula_y] = True
                            contblocos += 1
                            
                            if(jogador_1):
                                if(conteudo_bloco[celula_x][celula_y] == "X"):
                                    cont1 += 100
                                elif(conteudo_bloco[celula_x][celula_y] == "Y"):
                                    cont1 -= 50
                                    if(cont1 < 0):
                                        cont1 = 0
                                jogador_1 = False
                                jogador_2 = True
                            else:
                                if(conteudo_bloco[celula_x][celula_y] == "X"):
                                    cont2 += 100
                                elif(conteudo_bloco[celula_x][celula_y] == "Y"):
                                    cont2 -= 50
                                    if(cont2 < 0):
                                        cont2 = 0
                                jogador_1 = True
                                jogador_2 = False

                    
                    # Desenhar todas as células do tabuleiro 
                    for i in range(4):
                        for j in range(4):
                            if (bloco_revelado[i][j]):
                                if (conteudo_bloco[i][j] == "X"):
                                    tesouro = pygame.image.load('imagens/gomu.png').convert_alpha() #aceita fundo transparente
                                    tesouro = pygame.transform.scale(tesouro, (160 - 2, 160 - 2))
                                    tela.blit(tesouro, (160 * i + 1, 160 * j + 1))
                                elif (conteudo_bloco[i][j] == "Y"):
                                    buraco = pygame.image.load('imagens/buraco.png').convert_alpha()
                                    buraco = pygame.transform.scale(buraco, (160 - 2, 160 - 2))
                                    tela.blit(buraco, (160 * i + 1, 160 * j + 1))
                                else:
                                    if(num == 1):
                                        texto = fonte.render(str(conteudo_bloco[i][j]), True, cores.branco)
                                        tela.blit(texto, (160 * i + 0.4 * 160, 160 * j + 0.4 * 160))
                                    else:
                                        texto = fonte.render(str(conteudo_bloco[i][j]), True, cores.preto)
                                        tela.blit(texto, (160 * i + 0.4 * 160, 160 * j + 0.4 * 160))
                            #desenha pontuação dos jogadores
                            pygame.draw.rect(tela, cores.preto, (640, 0, 360, 640))
                            if (jogador_1):
                                pont1 = fonte2.render(f"{jogador1}: {cont1} pontos!", True, cores.azul_claro)
                            else:
                                pont1 = fonte2.render(f"{jogador1}: {cont1} pontos!", True, cores.branco)
                            if (jogador_2):
                                pont2 = fonte2.render(f"{jogador2}: {cont2} pontos!", True, cores.vermelho)
                            else:
                                pont2 = fonte2.render(f"{jogador2}: {cont2} pontos!", True, cores.branco)
                            tela.blit(pont1,(700, 200) )
                            tela.blit(pont2,(700, 400) )
                    pygame.display.update()
                    #exibe quem ganhou ao término do jogo
                    if (contblocos == 16):
                        pygame.time.delay(500)
                        pygame.draw.rect(tela, cores.preto, (0, 0, 1000, 640), 0)
                        if(cont1 > cont2):
                            resultado = pygame.image.load('imagens/Roger.jpg').convert_alpha()
                            resultado = pygame.transform.scale(resultado, (1000, 640))
                            tela.blit(resultado, (0,0))
                            pygame.draw.rect(tela, cores.preto, (0, 550, 1000, 35), 0)
                            ganhador = fonte2.render(f"One Piece encontrado! {jogador1} se tornou o Rei dos Piratas com {cont1} pontos!", False, cores.branco)
                            tela.blit(ganhador, (70, 550))
                        elif(cont2 > cont1):
                            resultado = pygame.image.load('imagens/Roger.jpg').convert_alpha()
                            resultado = pygame.transform.scale(resultado, (1000, 640))
                            tela.blit(resultado, (0,0))
                            pygame.draw.rect(tela, cores.preto, (0, 550, 1000, 35), 0)
                            ganhador = fonte2.render(f"One Piece encontrado! {jogador2} se tornou o Rei dos Piratas com {cont2} pontos!", False, cores.branco)                   
                            tela.blit(ganhador, (70, 550))
                        else:
                            resultado = pygame.image.load('imagens/Comemoration.jpg').convert_alpha()
                            resultado = pygame.transform.scale(resultado, (1000, 640))
                            tela.blit(resultado, (0,0))
                            pygame.draw.rect(tela, cores.preto, (0, 550, 1000, 35), 0)
                            ganhador = fonte2.render(f"Empate! O verdadeiro One Piece são os amigos que fizemos pelo caminho! Pontos: {cont1}", False, cores.branco)
                            tela.blit(ganhador, (15,550))

                        voltar = fonte2.render("<<< Voltar", True, cores.preto)
                        botao_voltar = tela.blit(voltar, (30, 600))
                        pygame.mixer.music.load('audios/weare.mp3')
                        pygame.mixer.music.play(-1,28.00)
                        pygame.display.update()
                        while True:
                                for evento in pygame.event.get():
                                    if evento.type == pygame.QUIT:
                                        pygame.quit() # Encerra o programa
                                    if evento.type == pygame.KEYDOWN:
                                        if evento.key == pygame.K_ESCAPE:  # Tecla de escape para sair
                                            pygame.quit()  # Encerra o programa
                                    if (evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1):
                                        pos_mouse = pygame.mouse.get_pos() #pega a posição do clique
                                        if(botao_voltar.collidepoint(pos_mouse)):
                                           pygame.mixer.music.stop()
                                           return main()           

                        
            pygame.quit()

if(__name__ == "__main__"):
    main()