from PPlay.window import *
from PPlay.sprite import *
from PPlay.gameimage import *
from PPlay.collision import *
from random import randint

var = 0
contador = 0

var2 = 0
contador2 = 0        
# Definindo a janela_jogo e entrada #
janela_jogo = Window(1280, 720)
janela_jogo.set_title("Ponguinho")
imagem_fundo = GameImage("C:/Users/pyyyt/Documents/Projetos PPlay/Pong/assets/fundo.jpg")
teclado = Window.get_keyboard()



# Definindo a bola #
ball = Sprite("C:/Users/pyyyt/Documents/Projetos PPlay/Pong/assets/bola64.png")
ball.x = janela_jogo.width/2 - ball.width/2
ball.y = janela_jogo.height/2 - ball.height/2
velocidadexdabola = 600
vely = 200



# Definindo paddle 1 #
pad1 = Sprite("C:/Users/pyyyt/Documents/Projetos PPlay/Pong/assets/cinderace.png")
pad1.x = 1180
pad1.y = janela_jogo.height/2 - pad1.height/2
velypad1 = 600


# Definindo paddle 2 #
pad2 = Sprite("C:/Users/pyyyt/Documents/Projetos PPlay/Pong/assets/pikachu.png")
pad2 = Sprite("Pong/assets/pikachu.png")
pad2.x = 30
pad2.y = janela_jogo.height/2 - pad2.height/2
velypad2 = 600



while True:


    # Moving the ball #
    ball.x+=velocidadexdabola*janela_jogo.delta_time()
    ball.y+=vely*janela_jogo.delta_time()


    # Movendo o pad1 #
    if(teclado.key_pressed("UP")):
            pad1.y+=velypad1*janela_jogo.delta_time()*(-1)
    if(teclado.key_pressed("DOWN")): 
            pad1.y+=velypad1*janela_jogo.delta_time()
    
    # Movendo o pad2 #
    if(teclado.key_pressed("w")):
            pad2.y+=velypad2*janela_jogo.delta_time()*(-1)    
    if(teclado.key_pressed("s")): 
            pad2.y+=velypad2*janela_jogo.delta_time()

    # Fazendo os pads reaparecerem em baixo quando vazarem por cima :

    if pad1.y <= -140:
        pad1.y = 720
        
    if pad2.y <= -140:
        pad2.y = 720
    
    # Fazendo os pads reaparecerem em cima quando vazarem por baixo :

    if pad1.y >= 860:
        pad1.y = 0
        
    if pad2.y >= 860:
        pad2.y = 0

    
    if ball.collided(pad1) or ball.collided(pad2):
            if (ball.x + ball.width >= pad1.x+ball.width) or (ball.x<=pad2.x):
                    
                    if velocidadexdabola>0:
                            b=0
                    else:
                            b=1
                    if (ball.x + ball.width >=pad1.x + ball.width):
                            a=1
                    else:
                            a=0
                    if a!=b:
                            velocidadexdabola*=(-1)
                    b=a
                    
    if (ball.y + ball.width >= 725) or (ball.y<=0):
            
            if vely>-15:
                    i=0
            else:
                    i=1
            if (ball.y + ball.width >=620):
                    o=1
            else:
                    o=0
            if o!=i:
                    vely*=(-1)
            i=o
    
    if (ball.x >= janela_jogo.width+1000) or (ball.x<=-1000):
            ball.x=janela_jogo.width/2 - ball.width/2
            ball.y=janela_jogo.height/2 - ball.height/2


    contador += randint(1, 10)
    if contador >= 1000 :
        var = randint(0,1)
        contador = 0
    if var == 0:
            pad2.y+=velypad2*janela_jogo.delta_time()*(-1)    
    if var == 1 : 
            pad2.y+=velypad2*janela_jogo.delta_time()
#     contador2 += randint(1, 10)
#     if contador2 >= 1000 :
#         var2 = randint(0,1)
#         contador2 = 0
#     if var2 == 0:
#             pad1.y+=velypad2*janela_jogo.delta_time()*(-1)    
#     if var2 == 1 : 
#             pad1.y+=velypad2*janela_jogo.delta_time()
    imagem_fundo.draw()

    ball.draw()
    pad1.draw()
    pad2.draw()

    if(teclado.key_pressed("ESC")): 
            janela_jogo.close()
    janela_jogo.update()