import pygame
from  classes.ball import Ball 
from  classes.paddle import Paddle 

class Player:
    def __init__(self, title, size_x, size_y) -> None:
        # create canvas
        pygame.init()
        pygame.display.set_caption(title)
        self.canvas = pygame.display.set_mode(size=(size_x, size_y))
        self.clock = pygame.time.Clock()

    def run(self):
        ball = Ball("Buoi3/assets/ball.png", 1.5, 3.5)
        paddle_1 = Paddle("Buoi3/assets/paddle.png")
        paddle_2 = Paddle("Buoi3/assets/paddle.png")

        # setup location
        ball.setX(285)
        ball.setY(300)
        paddle_1.setX(0)
        paddle_1.setY(250)
        paddle_2.setX(570)
        paddle_2.setY(250)

        # setup key press
        paddle_1.setKeyUp("W")
        paddle_1.setKeyDown("S")
        paddle_2.setKeyUp("Up")
        paddle_2.setKeyDown("Down")

        



