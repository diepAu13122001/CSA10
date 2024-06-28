import pygame
class Paddle:
    def __init__(self, img_url) -> None:
        self.img = pygame.image.load(img_url)

    # set location
    def setX(self, x):
        self.x = x

    def setY(self, y):
        self.y = y

    # get location
    def getX(self):
        return self.x

    def getY(self):
        return self.y

    # set key press
    def setKeyUp(self, key_up):
        self.key_up = key_up

    def setKeyDown(self, key_down):
        self.key_down = key_down

    # get key press
    def getKeyUp(self):
        return self.key_up

    def getKeyDown(self):
        return self.key_down

    def move(self, key_press):
        # match - case
        match key_press:
            case self.key_up: 
                if self.y > 0:
                    self.y -= 5 # move up
            case self.key_down:
                if self.y <= 480:
                    self.y += 5 # move down
