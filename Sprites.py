from Constants import *
import random
import pygame


class Sprite():
    def __init__(self, x, y, width, height, colour):
        super().__init__()
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.colour = colour

    def update(self):
        pass

    def draw(self, screen):
        pygame.draw.rect(screen, self.colour, [self.x, self.y, self.width, self.height])

class Ball(Sprite):
    def __init__(self, x, y, paddles):
        super().__init__(x,y, BALL_WIDTH, BALL_WIDTH, WHITE)
        self.vx = random.randint(MIN_BALL_SPEED,MAX_BALL_SPEED)
        self.vy = random.randint(MIN_BALL_SPEED,MAX_BALL_SPEED)
        self.paddles = paddles


    def hit_paddle(self):
        for paddle in self.paddles:
            return False

    def update(self):
        self.x = self.x + self.vx
        if self.x < 0 or self.x + self.width > WIDTH or hit_paddle:
            self.x = self.x - self.vx
            self.vx = - self.vx
        self.y = self.y + self.vy
        if self.y < 0 or self.y + self.width > HEIGHT or hit_paddle:
            self.y = self.y - self.vy
            self.vy = - self.vy


class Paddle(Sprite):
    def __init__(self, x, y):
        super().__init__(x,y, BALL_WIDTH, BALL_WIDTH * 5, WHITE)
        self.speed = 0
        self.direction = []

    def up(self):
        self.direction.append(UP)

    def down(self):
        self.direction.append(DOWN)

    def stopup(self):
        self.direction.remove(UP)

    def stopdown(self):
        self.direction.remove(DOWN)

    def update(self):
        try:
            if self.direction[len(self.direction)-1] == UP:
                self.speed = -PADDLE_SPEED
            elif self.direction[len(self.direction)-1] == DOWN:
                self.speed = +PADDLE_SPEED
        except IndexError:
            self.speed = 0
        self.y = self.y + self.speed


