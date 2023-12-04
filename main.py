import pygame
import config
import utils
from Sprites.Sprites import Player, Coin
from Sprites.MapSprite import Ground
import random

pygame.init()
pygame.font.init()

background = pygame.image.load("assets/T0o4T.png")
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

mobs = pygame.sprite.Group()

n_mobs = 5
for i in range(n_mobs):
    mobs.add(Coin())


player_entity = Player()
player.add(player_entity)

running = True

while running:
    clock.tick(config.FRAMERATE)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    player.update()
    mobs.update()





    #if len(mobs) < n_mobs:
    #    mobs.add(Coin())

    hits = pygame.sprite.groupcollide(player, mobs, False, True)
    if hits:
        player_entity.score += 1


    # screen.fill(config.COLORS["Red"])
    screen.blit(background, (0, 0))
    # for row in __map:
    #     row.draw(screen)

    text = font.render(f"Score:{player_entity.score}", False, (255, 255, 255))
    screen.blit(text, (0, 0))
    player.draw(screen)
    mobs.draw(screen)
    pygame.display.flip()
print("Hello World!")
pygame.quit()

