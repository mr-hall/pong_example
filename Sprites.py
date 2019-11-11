from Constants import *
import random

class Ball():
    def __init__(self):
        super().__init__()
        self.x = random.randint(0,WIDTH)
        self.y = random.randint(0,HEIGHT)
        self.vx = random.randint(MIN_BALL_SPEED,MAX_BALL_SPEED)
        self.vy = random.randint(MIN_BALL_SPEED,MAX_BALL_SPEED)
        self.width = BALL_WIDTH
        self.colour = WHITE

    def update(self):
        self.x = self.x + self.vx
        if self.x < 0 or self.x + self.width > WIDTH:
            self.x = self.x - self.vx
            self.vx = - self.vx
        self.y = self.y + self.vy
        if self.y < 0 or self.y + self.width > HEIGHT:
            self.y = self.y - self.vy
            self.vy = - self.vy


