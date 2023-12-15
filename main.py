import pygame
import Sprites.Sprites
import config
import utils
from Sprites.Sprites import Player, Coin
from Sprites.MapSprite import Ground
import random

pygame.init()
pygame.font.init()

background = pygame.image.load("assets/map.png")
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
coins = pygame.sprite.Group()

n_gotten_coins = 0
n_mobs = 4
n_coins = 5
for i in range(n_coins):
    coins.add(Coin())

for i in range(n_mobs):
    mobs.add(Sprites.Sprites.Mob())


player_entity = Player()
player.add(player_entity)
running = True

while running:
    clock.tick(config.FRAMERATE)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if player_entity.health <= 0:
            running = False
    for mob in mobs:
        mob.compute_move(player_entity)

    player.update()
    coins.update()
    mobs.update()





    #if len(mobs) < n_mobs:
    #    mobs.add(Coin())
    if len(coins) < n_coins:
        coins.add((Coin()))
    if len(mobs) < n_mobs:
        mobs.add((Sprites.Sprites.Mob()))

    hits = pygame.sprite.groupcollide(player, coins, False, True)
    if hits:
        player_entity.score += 1
        coins.add((Coin()))
        n_gotten_coins += 1
    if n_gotten_coins == 10:
        print("Our congratulations Your 10 coins")

    if n_gotten_coins == 50:
        print("Wow u r good, if u got 100, u will get present!")

    if n_gotten_coins == 100:
        print("Mine congratulations, u r pro! U got 100 coins omg, so here your present")
        print("............／＞　 フ..........")
        print("　　　　    | 　_　 _|"        )
        print("    　　　／`ミ _x 彡")
        print("　　 　  /　　　 　 |")
        print("  　　  /　 ヽ　　 ﾉ")
        print("   ／￣|　　 |　|　|")
        print("   | (￣ヽ＿_ヽ_)_)")
        print("   ＼二つ")
    hits = pygame.sprite.groupcollide(player, mobs, False, True)
    if hits and player_entity.resist <= 0:
        player_entity.health -= 1
        player_entity.resist += 3  #3 seconds
        print("U lost 1 hp, looser LOL")

        if len(mobs) < n_mobs:
            mobs.add((Sprites.Sprites.Mob()))

    # screen.fill(config.COLORS["Red"])
    screen.blit(background, (0, 0))

    # for row in __map:
    #     row.draw(screen)

    text = font.render(f"Score:{player_entity.score}", False, (255, 255, 0))
    screen.blit(text, (0, 0))
    text = font.render(f"Health:{player_entity.health}", False, (255, 0, 0))
    screen.blit(text, (10, 10))
    text = font.render(f"Resist:{player_entity.resist}", False, (0, 0, 255))
    screen.blit(text, (20, 20))
    text = font.render(f"Life time:{player_entity.time}", False, (0, 255, 0))
    screen.blit(text, (30, 30))
    player.draw(screen)
    mobs.draw(screen)
    coins.draw(screen)

    pygame.display.flip()
print("Hello World!")
pygame.quit()



