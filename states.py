from Constants import *
import pygame
import Sprites


class Game():
    def __init__(self):
        # initalise sprites
        self.sprites = pygame.sprite.Group()
        self.left_paddle = Sprites.Paddle(LEFT_PADDLE_X, STARTING_PADDLE_Y)
        self.sprites.add(self.left_paddle)
        self.right_paddle = Sprites.Paddle(RIGHT_PADDLE_X, STARTING_PADDLE_Y)
        self.sprites.add(self.right_paddle)
        self.paddles = [self.left_paddle, self.right_paddle]
        self.ball = Sprites.Ball(STARTING_BALL_X, STARTING_BALL_Y, self.paddles)
        self.sprites.add(self.ball)
        self.running = True
        self.next_state = None

    def handle_events(self, events):#
        for event in events:
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    self.left_paddle.up()
                elif event.key == pygame.K_z:
                    self.left_paddle.down()
                elif event.key == pygame.K_UP:
                    self.right_paddle.up()
                elif event.key == pygame.K_DOWN:
                    self.right_paddle.down()
                elif event.key == pygame.K_q:
                    self.next_state = Menu()
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_a:
                    self.left_paddle.stopup()
                elif event.key == pygame.K_z:
                    self.left_paddle.stopdown()
                elif event.key == pygame.K_UP:
                    self.right_paddle.stopup()
                elif event.key == pygame.K_DOWN:
                    self.right_paddle.stopdown()


    def update(self):
        self.sprites.update()

    def draw(self, screen):
        screen.fill(RED)
        self.sprites.draw(screen)


class Menu():
    def __init__(self):
        self.running = True
        self.next_state = None

    def handle_events(self, events):
        for event in events:
            if event.type == pygame.QUIT:
                self.running = False

    def update(self):
        pass

    def draw(self, screen):
        screen.fill(BLUE)