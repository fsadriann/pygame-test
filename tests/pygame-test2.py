# importar la libreria pygame
import pygame, sys
pygame.init()

#definir colores
BLACK = (0,0,0)
WHITE = (255,255,255)
GREEN = (0,255,0)
RED = (255,0,0)
BLUE = (0,0,255)

# definimos el tamaño de la ventana
size = (800, 500)

# crear ventana
window = pygame.display.set_mode(size)
# controlar fps
clock = pygame.time.Clock() 

#coordenadas del cuadrado
cord_x =400
cord_y =200

# velocidad del cuadrado
speed_x = 3
speed_y = 3

#bucle principal
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    if (cord_x > 720 or cord_x < 0):
        speed_x *= -1
    if (cord_y > 420 or cord_y < 0):
        speed_y *= -1

    cord_x += speed_x
    cord_y += speed_y
    #color de fondo
    window.fill(WHITE)
    ### ZONA DE DIBUJO

    pygame.draw.rect(window, RED, (cord_x,cord_y, 80, 80))

    ### ZONA DE DIBUJO
    # actualizar pantalla
    pygame.display.flip()
    clock.tick(60)