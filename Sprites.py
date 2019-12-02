from Constants import *
import random
import pygame



class Ball(pygame.sprite.Sprite):
    def __init__(self, x, y, paddles):
        super().__init__()

        self.vx = random.randint(MIN_BALL_SPEED,MAX_BALL_SPEED)
        self.vy = random.randint(MIN_BALL_SPEED,MAX_BALL_SPEED)
        self.paddles = paddles
        self.image = pygame.Surface([BALL_WIDTH, BALL_WIDTH])
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


    def hit_paddle(self):
        for paddle in self.paddles:
            if paddle.rect.colliderect(self.rect):
                return True
        return False


    def update(self):
        self.rect.x = self.rect.x + self.vx
        if self.rect.x < 0 or self.rect.x + self.rect.width > WIDTH or self.hit_paddle():
            self.rect.x = self.rect.x - self.vx
            self.vx = - self.vx
        self.rect.y = self.rect.y + self.vy
        if self.rect.y < 0 or self.rect.y + self.rect.width > HEIGHT or self.hit_paddle():
            self.rect.y = self.rect.y - self.vy
            self.vy = - self.vy


class Paddle(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.speed = 0
        self.direction = []
        self.image = pygame.Surface([BALL_WIDTH, BALL_WIDTH * 5])
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

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
        self.rect.y = self.rect.y + self.speed


