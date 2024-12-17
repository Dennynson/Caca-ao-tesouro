import pygame
import cores
import modulo

def creditos():
    # Inicializa o Pygame
    pygame.init()

    # Define a fonte e as dimensões da tela
    fonte = pygame.font.SysFont("Times New Roman", 45)
    fonte2 = pygame.font.Font("onepiece.ttf", 50)
    fonte3 = pygame.font.Font("onepiece.ttf", 27)
    largura = 1000
    altura = 640
    tela = pygame.display.set_mode((largura, altura))

    voltar = fonte3.render("<<< Voltar", True, cores.branco)

    # Define o título da janela
    pygame.display.set_caption('Créditos')

    # Loop principal do jogo
    executando = True
    while executando:
        # Preenche a tela com preto
        tela.fill(cores.preto)

        # Adiciona o brasão da UFPB
        ufpb = pygame.image.load('imagens/ufpb.png')
        ufpb = pygame.transform.scale(ufpb, (180, 200))
        tela.blit(ufpb, (400, 30))

        # Adiciona os créditos
        univ = fonte.render("Universidade Federal da Paraíba", True, cores.branco)
        tela.blit(univ, (195, 245))
        ci = fonte.render("CI - Centro de Informática", True, cores.branco)
        tela.blit(ci, (250, 295))
        dev = fonte2.render("PROGRAMADORES:", True, cores.branco)
        tela.blit(dev,(340, 390) )
        n1 = fonte2.render("Dennynson Scheydt Medeiros Nascimento", True, cores.branco)
        tela.blit(n1,(170, 475) )
        n2 = fonte2.render("Matias Monteiro de Araújo", True, cores.branco)
        tela.blit(n2,(275, 525) )
        n3 = fonte2.render("Vinícius da Silva Cunha", True, cores.branco)
        tela.blit(n3,(300, 575) )
        #adiciona botão voltar
        botao_voltar = tela.blit(voltar, (50, 575))
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                executando = False
            if (evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1):
                pos_mouse = pygame.mouse.get_pos() #pega a posição do clique
                if(botao_voltar.collidepoint(pos_mouse)):
                    return modulo.menu()



        # Atualiza a tela
        pygame.display.update()

    # Encerra o Pygame
    pygame.quit()