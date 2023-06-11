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

#bucle principal
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    #color de fondo
    window.fill(WHITE)
    ### ZONA DE DIBUJO

    """pygame.draw.line(window, GREEN,[0,100], [200,300], 5)
    pygame.draw.rect(window, BLACK,(100,100, 80,80))
    pygame.draw.circle(window, BLACK, (200,200), 30)"""

    for x in range(100,700,100):
        pygame.draw.rect(window, BLACK,(x,230, 50, 50))
        pygame.draw.line(window, GREEN,(x,0),(x,100),5)

    ### ZONA DE DIBUJO
    # actualizar pantalla
    pygame.display.flip()