import pygame
pygame.init()

#colores
black = (0,0,0)
white = (255,255,255)
screen_size =(800,600)
player_width=15
player_height=90

screen = pygame.display.set_mode(screen_size)
clock = pygame.time.Clock()

# coords, speed p1
player1_x = 50
player1_y = 300 - 45
player1_speed = 0

# coords, speed p2
player2_x = 750 - player_width
player2_y = 300 - 45
player2_speed = 0

#coords pelota
ball_x = 400
ball_y = 300
ball_speed_x = 3
ball_speed_y = 3

game_over = False

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
    #zona logica

    screen.fill(black)
    #zona de dibujo
    player1 = pygame.draw.rect(screen, white, (player1_x, player1_y, player_width,player_height))
    player2 = pygame.draw.rect(screen, white, (player2_x, player2_y, player_width,player_height))
    pygame.draw.circle(screen, white, (ball_x, ball_y), 10)
    pygame.display.flip()
    clock.tick(60)
pygame.quit()