import pygame
import Sprites
import Constants
from Constants import *


#Initalise pygame and window
pygame.init()
screen = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()

#initalise sprites
sprites = []

left_paddle = Sprites.Paddle(LEFT_PADDLE_X, STARTING_PADDLE_Y)
sprites.append(left_paddle)
right_paddle = Sprites.Paddle(RIGHT_PADDLE_X, STARTING_PADDLE_Y)
sprites.append(right_paddle)
paddles = [left_paddle, right_paddle]
ball = Sprites.Ball(STARTING_BALL_X, STARTING_BALL_Y, paddles)
sprites.append(ball)
#Game loop
running = True
while running:
    #handle input
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                left_paddle.up()
            elif event.key == pygame.K_z:
                left_paddle.down()
            elif event.key == pygame.K_UP:
                right_paddle.up()
            elif event.key == pygame.K_DOWN:
                right_paddle.down()
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                left_paddle.stopup()
            elif event.key == pygame.K_z:
                left_paddle.stopdown()
            elif event.key == pygame.K_UP:
                right_paddle.stopup()
            elif event.key == pygame.K_DOWN:
                right_paddle.stopdown()
    #game logic
    for sprite in sprites:
        sprite.update()

    #drawing
    screen.fill(RED)
    for sprite in sprites:
        sprite.draw(screen)

    pygame.display.flip()

    clock.tick(FPS)

#Quit
pygame.quit()