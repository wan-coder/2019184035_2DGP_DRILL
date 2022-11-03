from pico2d import *
import game_world


class Ball:
    image = None

    def __init__(self, x = 800, y = 300, v = 1):
        if Ball.image == None:
            Ball.image = load_image('ball21x21.png')
        self.x, self.y, self.v = x, y, v

    def draw(self):
        self.image.draw(self.x, self.y)

    def update(self):
        self.x += self.v
        if self.x < 20 or self.x > 800-25:
            game_world.remove_object(self)
