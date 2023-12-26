import random

from pygame import *
init()
clock = time.Clock()


def help():
    bg = image.load('Plaster01_D.jpg')
    size = [1080, 720]
    font_base = font.Font('Bernhard.otf', 60)
    screen = display.set_mode(size)
    display.set_caption('Сокобан.помощь')
    player = image.load('content/player.png')
    display.set_icon(player)
    help_text = ['      WELCOME!',
                 '',
                 'sokoban is such an easy game,',
                 'no tutorials are provided',
                 'every level is passable,',
                 'just strain your brain',
                 'and be happy with it',
                 '',
                 'Have a good game!']

    x = 25
    y = 140

    run = True
    while run:

        screen.blit(bg, (0,0))

        for i in range(len(help_text)):
            text = font_base.render(help_text[i], True, [200, 200, 200])
            screen.blit(text, [x, y+i*50])
        for e in event.get():
            if e.type == QUIT:
                run = False
            elif e.type == KEYDOWN:
                if e.key == K_SPACE:
                    run = False
        display.flip()
