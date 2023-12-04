import pygame.key

from pygame.sprite import Sprite
from pygame import Surface, image, transform
import config
import random
import utils
import pygame

clock = pygame.time.Clock()
running = True


class Player(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        self.index = 0

        self.images = [
            image.load("assets/dino.2.png"),
            image.load("assets/dino.2.png")
        ]
        self.images = list(map(
            lambda x: transform.scale(x, (64, 64)),
            self.images
        ))

        self.image = self.images[self.index]
        self.rect = self.image.get_rect()
        self.rect.center = (config.WIDTH / 2, config.HEIGHT / 2)

        self.score = 0


        self.speed_x = 0
        self.speed_y = 0

        self.is_jump = False

    def update(self):
        self.speed_x = 0
        self.speed_y += 1
        self.update_image_move(0)

        key = pygame.key.get_pressed()
        # if key[pygame.K_w]:
        #  self.speed_y = -5
        # if key[pygame.K_s]:
        # self.speed_y = 5
        if key[pygame.K_a]:
            self.speed_x = -5
            self.update_image_move(-1)
        if key[pygame.K_d]:
            self.speed_x = 5
            self.update_image_move(1)
        if key[pygame.K_SPACE] and self.is_jump == False:
            self.speed_y = -10
            self.is_jump = True

        self.rect.x += self.speed_x
        if self.rect.x > config.WIDTH - self.rect.width or self.rect.x < 0:
            self.rect.x -= self.speed_x
            # self.speed_x *= 0.95

        self.rect.y += self.speed_y
        if self.rect.y > config.HEIGHT - self.rect.height or self.rect.y < 0:
            self.rect.y -= self.speed_y
            self.is_jump = False
            # self.speed_y *= 0.95

    def update_image(self, index):
        if self.index != index:
            self.index = index
            self.image = self.images[self.index]

    def update_image_move(self, move: int):
        angle = 45 * move
        # image = transform.rotate(self.images[self.index], angle)
        image = self.images[self.index]
        if move < 0:
            image = transform.flip(image, 1, 0)
        self.image = image

    def reverse_speed_x(self):
        self.speed_x = -self.speed_x

    def reverse_speed_y(self):
        self.speed_y = -self.speed_y

    #def get_knockback(self):
    #    self.rect.x += -self.speed_x
    #    self.rect.y += -self.speed_y


class Coin(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        self.index = 0
        self.images = [
            image.load("assets/money.2.png"),
            image.load("assets/money.2.png")
        ]
        self.images = list(map(
            lambda x: transform.scale(x, (30, 30)),
            self.images
        ))
        self.image = self.images[self.index]
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(400, 500)
        self.rect.y = random.randint(450, 500)
        self.rect.center = (self.rect.x, self.rect.y)
        #self.rect.center = (config.WIDTH / 5, config.HEIGHT / 3)


    def update(self):
        def update(self):
            self.rect.x += self.speed_x
            if self.rect.x > config.WIDTH - self.rect.width or self.rect.x < 0:
                self.rect.x -= self.speed_x
                # self.speed_x *= 0.95

            self.rect.y += self.speed_y
            if self.rect.y > config.HEIGHT - self.rect.height or self.rect.y < 0:
                self.rect.y -= self.speed_y

    # def compute_move(self, player: Player):
    #    x_m, y_m = self.rect.center
    #    x_p, y_p = player.rect.center

    #    vector_up = utils.get_lenght(x_p, y_p, x_m, y_m - self.speed_y)
    #    vector_down = utils.get_lenght(x_p, y_p, x_m, y_m + self.speed_y)
    #    vector_right = utils.get_lenght(x_p, y_p, x_m + self.speed_x, y_m)
    #    vector_left = utils.get_lenght(x_p, y_p, x_m - self.speed_x, y_m)

    #    min_vector = min(vector_up, vector_down, vector_left, vector_right)
    #    if vector_up == min_vector:
    #        self.rect.y += -self.speed_y
    #    if vector_down == min_vector:
    #        self.rect.y += self.speed_y
    #    if vector_left == min_vector:
    #        self.rect.x += -self.speed_x
    #    if vector_right == min_vector:
    #        self.rect.x += self.speed_x

    def reverse_speed_x(self):
        self.speed_x = -self.speed_x

    def reverse_speed_y(self):
        self.speed_y = -self.speed_y
