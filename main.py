import pygame
import config
import utils
from Sprites.Sprites import Player, Mob
from Sprites.MapSprite import Ground
import random

pygame.init()
pygame.font.init()

background = pygame.image.load("assets/background.jpeg")
background = pygame.transform.scale(background, (config.WIDTH, config.HEIGHT))

font = pygame.font.SysFont(pygame.font.get_default_font(), 20)

screen = pygame.display.set_mode(
    (config.WIDTH, config.HEIGHT)
)

player = pygame.sprite.Group()
player.add(Player())

__map = []

for i in range(config.CELL_ON_HEIGHT):
    __map.append(pygame.sprite.Group())
    for j in range(config.CELL_ON_WIDTH):
        group = __map[i]
        group.add(Ground())

utils.generate_walls(__map)

clock = pygame.time.Clock()
running = True

while running:
    clock.tick(config.FRAMERATE)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    player.update()

    # screen.fill(config.COLORS["Red"])
    screen.blit(background, (0, 0))
    # for row in __map:
    #     row.draw(screen)
    player.draw(screen)
    pygame.display.flip()

pygame.quit()
