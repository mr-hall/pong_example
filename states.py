from Constants import *
import pygame
import Sprites

class States():
    def __init__(self):
        super().__init__()
        self.running = True
        self.next_state = None
    def handle_event(self, event):
        pass

    def update(self):
        pass

    def draw(self, screen):
        pass


class Game(States):
    def __init__(self):
        super().__init__()
        # initalise sprites
        self.sprites = pygame.sprite.Group()
        self.left_paddle = Sprites.Paddle(LEFT_PADDLE_X, STARTING_PADDLE_Y)
        self.sprites.add(self.left_paddle)
        self.right_paddle = Sprites.Paddle(RIGHT_PADDLE_X, STARTING_PADDLE_Y)
        self.sprites.add(self.right_paddle)
        self.paddles = [self.left_paddle, self.right_paddle]
        self.ball = Sprites.Ball(STARTING_BALL_X, STARTING_BALL_Y, self.paddles)
        self.sprites.add(self.ball)
        self.next_state = None

    def handle_event(self, event):#
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


class Menu(States):
    def __init__(self):
        super().__init__()


    def handle_event(self, event):
        if event.type == pygame.QUIT:
            self.running = False

    def update(self):
        pass

    def draw(self, screen):
        screen.fill(BLUE)

class TitleScreen(States):
    def __init__(self):
        super().__init__()
        self.background = pygame.image.load("images/background.png").convert()
        self.timer = 0

    def handle_event(self, event):
        if event.type == pygame.QUIT:
            self.running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            self.next_state = Game()

    def update(self):
        self.timer += 1
        if self.timer > 500:
            self.next_state = Game()

    def draw(self, screen):
        screen.fill(GREEN)
        screen.blit(self.background, (0,0))
