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

font = pygame.font.SysFont(pygame.font.get_default_font(), 37)

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
bosses = pygame.sprite.Group()

n_bosses = 0
n_gotten_coins = 0
n_mobs = 4
n_coins = 10

for i in range(n_bosses):
    bosses.add(Sprites.Sprites.Boss())

for i in range(n_coins):
    coins.add(Coin())

for i in range(n_mobs):
    mobs.add(Sprites.Sprites.Mob())


player_entity = Player()
player.add(player_entity)
running = True

while running:
    clock.tick(config.FRAMERATE)
    if player_entity.health <= 0:
        running = False
        print("U r lose LOL")
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    for mob in mobs:
        mob.compute_move(player_entity)

    for Boss in bosses:
        Boss.compute_move(player_entity)

    player.update()
    coins.update()
    mobs.update()
    bosses.update()

    if len(coins) < n_coins:
        coins.add((Coin()))
    if len(mobs) < n_mobs:
        mobs.add((Sprites.Sprites.Mob()))

    if player_entity.time == 1 and player_entity.health > 5:
        bosses.add((Sprites.Sprites.Boss()))
        n_bosses += 1
    if player_entity.time == 1200: #1200 - 20 секунд
        bosses.add((Sprites.Sprites.Boss()))
        n_bosses += 1
    hits = pygame.sprite.groupcollide(player, bosses, False, True)
    if hits:
        player_entity.health -= 3
        player_entity.resist += 10
        print("if u still alive u r god or fk cheater")

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

    if n_gotten_coins == 100:
        player_entity.score -= 100
        n_gotten_coins -= 100
        player_entity.health += 1
        print("converted 100 coins into 1 health")

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
    screen.blit(text, (10, 20))
    text = font.render(f"Resist:{(int(player_entity.resist))}", False, (0, 0, 255))
    screen.blit(text, (20, 40))
    text = font.render(f"Life time:{player_entity.time//60}", False, (0, 255, 0))
    screen.blit(text, (30, 60))
    player.draw(screen)
    mobs.draw(screen)
    coins.draw(screen)
    bosses.draw(screen)

    pygame.display.flip()
print("Hello World!")
pygame.quit()



