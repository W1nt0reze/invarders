import pygame
import random
import time
import os
import sys


def load_image(name, color_key=None):
    fullname = os.path.join('data', name)
    try:
        image = pygame.image.load(fullname).convert()
    except pygame.error as message:
        print('Cannot load image:', name)
        raise SystemExit(message)

    if color_key is not None:
        if color_key == -1:
            color_key = image.get_at((0, 0))
            image.set_colorkey(color_key)
        else:
            image = image.convert_alpha()
    return image


def terminate():
    pygame.quit()
    sys.exit()


def start_screen():
    intro_text = ["Лучшая игра всех времён",
                  "Управление стрелочками",
                  "     Стрелять на пробел",
                  "        Приятной игры"]
    fon = pygame.transform.scale(load_image('земля1.png').convert(), SCREEN_SIZE)
    screen.blit(fon, (0, 0))
    font = pygame.font.Font(None, 30)
    text_coord = 200
    surf = pygame.Surface((265, 140))
    surf.fill((0, 0, 0))
    surf.set_alpha(200)
    screen.blit(surf, (120, 195))
    for line in intro_text:
        string_rendered = font.render(line, 1, pygame.Color(200, 200, 200))
        intro_rect = string_rendered.get_rect()
        text_coord += 10
        intro_rect.top = text_coord
        intro_rect.x = 125
        text_coord += intro_rect.height
        screen.blit(string_rendered, intro_rect)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.KEYDOWN or \
                    event.type == pygame.MOUSEBUTTONDOWN:
                return
        pygame.display.flip()
        clock.tick(FPS)


# Настройки окна
WIDTH = 500
HEIGHT = 520
SCREEN_SIZE = WIDTH, HEIGHT
FPS = 60

# Настройка цвета
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Инициализация
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

# Время
lastTime = 0
currentTime = 0

# Персонаж
x = WIDTH // 2
y = HEIGHT // 2
hero = pygame.Rect(x, y, 60, 50)
heroImg = load_image('razorinv.png')
heroImg.set_colorkey((0, 0, 0))

# Hp
hp = 3
HP_list = []
HP_X = 25
HP_Y = HEIGHT - 10
a = 0

# Противники
enemies = []
enemycd = 5
enemyImage = load_image('invaderinv_1.png').convert()
enemyRect = enemyImage.get_rect()
we = enemyRect.width
he = enemyRect.height
points = 0
enemyImage.set_colorkey((0, 0, 0))

# Звезд
stars = []
starcd = 5
starImg = load_image('starinv.png')
starRect = starImg.get_rect()
ws = enemyRect.width
hs = enemyRect.height
starsSpeed = 1

# бонусы
speedtime = 10
hptime = 10
y1 = -50
y2 = -50
x1 = random.randint(0, 500)
x2 = random.randint(0, 500)
hpB = 10
speedB = 10
hpRect = pygame.Rect(x1, y1, 20, 20)
speedRect = pygame.Rect(x2, y2, 20, 20)

# Пули
wb = 2
hb = 5
bulletImg = load_image("bullet.png")
bullets = []
Shot = False

# Пули противника
bulletse = []
speed = 2

# Шрифты
hpT = pygame.font.SysFont('comic sans ms', 14)
pointsT = pygame.font.SysFont('comic sans ms', 19)
pointsT1 = pygame.font.SysFont('comic sans ms', 30)
gameover = pygame.font.SysFont('comic sans ms', 60)

# Текст
gameover_text = gameover.render('GAME OVER', 1, WHITE)
hp_text = hpT.render('HP: ', 1, WHITE)
waveT = pointsT.render('Волна', 1, WHITE)

# Переменные движения
play_left = ''
play_right = ''
play_up = ''
play_down = ''

# МЕНЮ
HImg = load_image('земля1.png')
font = pygame.font.SysFont('arial', 18)
# сложность
difficult = 0
HeroSpeed = 4
enemyR = 3000
EnemySpeed = 2
bulletsEcd = 300
enemyD = 2
wave = 0
tristo = 700
speedX = 1

jjj = []
hhh = []
gamemode = 1
pygame.display.set_caption("Invaders")
start_screen()
bonusS = False
bonusH = False
GO = False
running = True
while running:
    if gamemode == 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if 170 < event.pos[0] < 160 + 170 and 150 < event.pos[1] < 150 + 50:
                    if event.button == 1:
                        gamemode = 0
                if 170 < event.pos[0] < 160 + 170 and 250 < event.pos[1] < 250 + 50:
                    if event.button == 1:
                        if hp != 1:
                            hp -= 1
                    if event.button == 3:
                        if hp < 15:
                            hp += 1

                if 170 < event.pos[0] < 160 + 170 and 350 < event.pos[1] < 350 + 50:
                    if event.button == 1:
                        if speedX != 1:
                            speedX -= 1
                    if event.button == 3:
                        if speedX < 5:
                            speedX += 1
                if 170 < event.pos[0] < 160 + 170 and 450 < event.pos[1] < 450 + 50:
                    if event.button == 1:
                        running = False

        screen.fill(BLACK)
        screen.blit(HImg, (0, 0))

        text = font.render('Кол-во HP:' + str(hp), 1, (0, 255, 0))
        text1 = font.render('Играть', 1, (0, 255, 0))
        text2 = font.render('Волны: x' + str(speedX), 1, (0, 255, 0))
        text3 = gameover.render('Invaders', 1, (0, 255, 0))
        text4 = font.render('Выход', 1, (0, 255, 0))

        pygame.draw.rect(screen, (0, 0, 0), (170, 150, 160, 50))
        pygame.draw.rect(screen, (0, 0, 0), (170, 250, 160, 50))
        pygame.draw.rect(screen, (0, 0, 0), (170, 350, 160, 50))
        pygame.draw.rect(screen, (0, 0, 0), (170, 450, 160, 50))
        screen.blit(text, (190, 250))
        screen.blit(text1, (200, 150))
        screen.blit(text2, (200, 350))
        screen.blit(text3, (2, 15))
        screen.blit(text4, (220, 450))

    if gamemode == 0:
        if a == 0:
            for i in range(hp):
                HP_list.append(pygame.Rect(HP_X, HP_Y, 30, 10))
                HP_X += 32
            a = 1
        screen.fill(BLACK)
        for i in pygame.event.get():
            if i.type == pygame.QUIT:
                running = False
            if i.type == pygame.KEYDOWN:
                if i.key == pygame.K_LEFT:
                    play_left = 1
                if i.key == pygame.K_RIGHT:
                    play_right = 1
                if i.key == pygame.K_UP:
                    play_up = 1
                if i.key == pygame.K_DOWN:
                    play_down = 1
                if i.key == pygame.K_SPACE:
                    Shot = True
            if i.type == pygame.KEYUP:
                if i.key == pygame.K_LEFT:
                    play_left = ''
                if i.key == pygame.K_RIGHT:
                    play_right = ''
                if i.key == pygame.K_UP:
                    play_up = ''
                if i.key == pygame.K_DOWN:
                    play_down = ''

        # Передвижение персонажа
        if play_left == 1 and hero.left > 0:
            hero.left -= HeroSpeed
        if play_right == 1 and hero.right < WIDTH:
            hero.left += HeroSpeed
        if play_up == 1 and hero.top > 0:
            hero.top -= HeroSpeed + 1
        if play_down == 1 and hero.bottom < HEIGHT:
            hero.top += HeroSpeed

        # СТОЛКНОВЕНИЕ
        # Противник с героем
        for enemy in enemies:
            if hero.colliderect(enemy):
                del enemies[index_enemy]
                if hp > 0:
                    del HP_list[hp - 1]
                    hp -= 1
                    points += 1

        # Противник с пулей
        for i in range(len(enemies)):
            for j in range(len(bullets)):
                if enemies[i].colliderect(bullets[j]):
                    jjj.append(i)
                    hhh.append(j)
                    points += 1
        for i in jjj:
            del enemies[i]
        jjj = []
        for i in hhh:
            del bullets[i]
        hhh = []

        # Отрисовка счета
        points_text = pointsT.render('Очки: ' + str(points), 1, WHITE)
        screen.blit(points_text, (10, 10))

        # Отрисовка волн
        waveT = pointsT.render('Волна: ' + str(wave), 1, WHITE)
        screen.blit(waveT, (400, 10))

        # ПУЛИ
        # Создание пуль игрока

        if Shot:
            bulRect = pygame.Rect(hero.left + 33, hero.top + 5, wb, hb)
            bullets.append(bulRect)
            Shot = False

        # Отрисовка пуль
        for bullet in bullets:
            screen.blit(bulletImg, (bullet.left, bullet.top))
            bullet.top -= 5

        # Удаление пуль
        index_bul = 0
        for b in bullets:
            if b.bottom < -5:
                bullets.pop(index_bul)
            index_bul += 1

        # Создание пуль врага
        bulletsEcd -= 5
        if bulletsEcd == 0:
            pass

        # ЗВЕЗДЫ
        starcd -= 1
        if starcd < 0:
            x_star = random.randint(0, WIDTH - ws)
            star = pygame.Rect(x_star, -hs, ws, hs)
            stars.append(star)
            starcd = random.randint(20, 40)

        for star in stars:
            screen.blit(starImg, (star.left, star.top))
            starsSpeed = random.randint(1, 5)
            star.top += starsSpeed
            if star.top > HEIGHT:
                stars.remove(star)

                # ЗАХВАТЧИКИ
        currentTime = pygame.time.get_ticks()
        # Создание противников
        if currentTime - lastTime > enemycd:
            x_enemy = random.randint(we, WIDTH - we)
            enemies.append(pygame.Rect(x_enemy, -he, we, he))
            lastTime = currentTime
            if (points * difficult) != enemyR - 50 or (points * difficult) > enemyR - 50:
                enemycd = random.randint(10, enemyR - (points * difficult))
            else:
                enemycd = 110

        # Отрисовка противников
        for enemy in enemies:
            screen.blit(enemyImage, (enemy.left, enemy.top))

            enemy.top += enemyD

        for enemy in enemies:
            follow = random.randint(1, 3)
            if follow == 1 and enemy.left > 0:
                enemy.left -= EnemySpeed
            if follow == 2 and enemy.right < WIDTH:
                enemy.right += EnemySpeed
            if follow == 3 and enemy.top > 0:
                enemy.top += EnemySpeed

        index_enemy = 0
        # Удаление противников
        for enemy in enemies:
            if enemy.top > HEIGHT:
                del HP_list[hp - 1]
                hp -= 1
                del enemies[index_enemy]

        # Отрисовка персонажа
        screen.blit(heroImg, (hero.left, hero.top))

        # отрисовка hp
        screen.blit(hp_text, (0, HP_Y - 5))
        for hpp in HP_list:
            pygame.draw.rect(screen, RED, hpp)

        speedB -= 1
        if speedB == 0:
            bonusS = True

        tristo -= 1 * speedX
        if tristo == 0:
            wave += 1
            if difficult != 40:
                difficult += 2
            if HeroSpeed != 2:
                HeroSpeed -= 1
            if EnemySpeed != 10:
                EnemySpeed += 1
            if enemyD == 10:
                enemyD += 1
            tristo = 700

        if bonusS:
            pygame.draw.rect(screen, (255, 255, 0), speedRect)
            speedRect.top += 2
            if speedRect.top > 500:
                speedRect.top = -50
                speedB = speedtime
                bonusS = False

        if hero.colliderect(speedRect):
            speedRect.top = -50
            speedB = speedtime
            HeroSpeed += 0.2
            bonusS = False

        if hp <= 0:
            GO = True
        if GO:
            screen.fill(BLACK)
            screen.blit(gameover_text, (50, 200))
            points_text1 = pointsT1.render('Ваши очки: ' + str(points), 1, WHITE)
            screen.blit(points_text1, (150, 300))
            pygame.display.update()
            time.sleep(2)
            gamemode = 1
            hp = 3
            points = 0
            a = 0

            GO = False
            hero.left = WIDTH // 2
            hero.top = HEIGHT // 2
            play_left = ''
            play_right = ''
            play_up = ''
            play_down = ''
            enemies = []
            HP_X = 25
            HP_Y = HEIGHT - 10

    pygame.display.update()
    clock.tick(FPS)

pygame.quit()
