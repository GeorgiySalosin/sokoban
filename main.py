from pygame import *
from random import randint

import settings

init()
from sokoban import game
from help import help
size = [1080, 720]
beep_system = mixer.Sound("content/sfx/beep_system.mp3")
swish = mixer.Sound("content/sfx/step_swish.mp3")
screen = display.set_mode(size)
display.set_caption('Игра')
player = transform.scale(image.load('content/avatar_icon.png'), [64, 64])
cursor = transform.scale(image.load('content/ui/cursor.png'), [32, 32])
display.set_icon(player)
font_base = font.Font('Bernhard.otf', 70)
font_scaled = font.Font('Bernhard.otf', 100)
bg = image.load('BG.png')
run = True
x = 130
y = 120
menu_items = ['PLAY', 'HELP', 'EXIT']
menu_buttons_rect = []
mouse.set_visible(False)
clock = time.Clock()
R = randint(100,255)
G = randint(100,255)
B = randint(100,255)
dr = 1
dg = 2
db = 3

def colorgrade(R, G, B, dr, dg, db):
    R += dr
    G += dg
    B += db
    if R < 100:
        dr = -dr
    elif R > 255:
        R = 255
        dr = -dr
    if G < 100:
        dg = -dg
    elif G > 255:
        G = 255
        dg = -dg
    if B < 100:
        db = -db
    elif B > 255:
        B = 255
        db = -db
    return R, G, B, dr, dg, db

while run:
    pos = mouse.get_pos()
    screen.blit(bg, (0,0))
    for i in range(len(menu_items)):
        text_base = font_base.render(menu_items[i], True, [200, 200, 200])
        text_scaled = font_scaled.render(menu_items[i], True, [R, G, B])
        button_rect = Rect(x, y + i*150, 150, 80)
        menu_buttons_rect.append(button_rect)
        menu_items_rect = text_base.get_rect(center=button_rect.center)
        if not menu_buttons_rect[i].collidepoint(pos):
            screen.blit(text_base, button_rect)
        else:
            screen.blit(text_scaled, button_rect)

    for e in event.get():
        if e.type == QUIT:
            run = False
        elif e.type == KEYDOWN:
            if e.key == K_ESCAPE:
                run = False
        if e.type == MOUSEBUTTONDOWN:
            if e.button == 1:
                for i in range(len(menu_buttons_rect)):
                    if menu_buttons_rect[i].collidepoint(pos):
                        if i == 0:
                            swish.play()
                            game()
                        elif i == 1:
                            swish.play()
                            help()
                        elif i == 2:
                            run = False
    if mouse.get_focused():
        pos = mouse.get_pos()
        screen.blit(cursor, cursor.get_rect(center=pos))
    R,G,B,dr,dg,db = colorgrade(R,G,B,dr,dg,db)
    display.flip()
    clock.tick(30)
quit()
