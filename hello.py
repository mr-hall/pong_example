import pygame
import Sprites
import Constants
from Constants import *


#Initalise pygame and window
pygame.init()
screen = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()

#initalise sprites
balls = []
for i in range(20):
    balls.append(Sprites.Ball())

#Game loop
running = True
while running:
    #handle input
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            running = False

    #game logic
    for ball in balls:
        ball.update()

    #drawing
    screen.fill(RED)
    for ball in balls:
        pygame.draw.rect(screen, ball.colour,[ball.x, ball.y, ball.width, ball.width])
    pygame.display.flip()

    clock.tick(FPS)

#Quit
pygame.quit()