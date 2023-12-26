from pygame import *
import settings
init()
def game():
    def get_frame(input_image, tile_res, frame, scale=1):
        image = Surface((tile_res, tile_res), SRCALPHA)
        atlas_res = int(input_image.get_width() / tile_res)
        image.blit(input_image, (0, 0),
                   ((tile_res * (frame % atlas_res)), (tile_res * (frame // atlas_res)), tile_res, tile_res))
        return image

    def anim_list(image, tile_res, length, scale=1):
        myList = []
        for i in range(0, length):
            myList.append(get_frame(image, tile_res, i, scale))
        return myList

    def read_file(file_name):
        coins_total = 0
        cells_total = 0
        f = open(file_name, 'r')
        s = f.readlines()
        for i in range(len(s)):
            s[i] = s[i].split()
        map_list = [0] * len(s)
        for i in range(len(map_list)):
            map_list[i] = [0] * len(s[i])
        for i in range(len(map_list)):
            for j in range(len(map_list[i])):
                map_list[i][j] = int(s[i][j])
                if map_list[i][j] == 3 or map_list[i][j] == 10:
                    coins_total += 1
                elif map_list[i][j] == 5 or map_list[i][j] == 9:
                    cells_total += 1
        f.close()
        print(map_list)
        print(coins_total, cells_total)
        return map_list, coins_total, cells_total

    def draw_map(map_list, gx, gy, dx, dy):
        screen.blit(bg, (0, 0))
        p_row, p_col = 0, 0
        for row in range(len(map_list)):
            for col in range(len(map_list[row])):
                x = gx + dx * col
                y = gy + dy * row
                match (int(map_list[row][col])):
                    case 0:
                        screen.blit(road, (x, y))
                    case 1:
                        screen.blit(wall, (x, y))
                    case 2:
                        screen.blit(box, (x, y))
                    case 3:
                        screen.blit(road, (x, y))
                        screen.blit(a_coin[coin_frame], (x, y))
                    case 4:
                        screen.blit(door, (x, y))
                    case 5:
                        screen.blit(road, (x, y))
                        screen.blit(star, (x, y))
                    case 7:
                        screen.blit(road, (x, y))
                        screen.blit(a_player[player_frame], (x, y))
                        p_col = col
                        p_row = row
                    case 8:
                        screen.blit(road, (x, y))
                        screen.blit(a_player[player_frame], (x, y))
                        p_col = col
                        p_row = row
                    case 9:
                        screen.blit(box_placed, (x, y))
                    case 10:
                        screen.blit(box, (x, y))
        return p_row, p_col

    def define_following(p_row, p_col, e):
        next_row, next_col = p_row, p_col
        box_next_row, box_next_col = p_row, p_col
        if e.key == settings.bind_up:
            next_row = p_row - 1
            box_next_row = p_row - 2
        elif e.key == settings.bind_down:
            next_row = p_row + 1
            box_next_row = p_row + 2
        elif e.key == settings.bind_left:
            next_col = p_col - 1
            box_next_col = p_col - 2
        elif e.key == settings.bind_right:
            next_col = p_col + 1
            box_next_col = p_col + 2
        return next_row, next_col, box_next_row, box_next_col

    def move_player(p_row, p_col, next_row, next_col, box_next_row, box_next_col, map_list, current_coins, is_win,
                    current_cells):
        if map_list[next_row][next_col] == 0:
            map_list[next_row][next_col] = 7
            if map_list[p_row][p_col] == 7:
                map_list[p_row][p_col] = 0
            elif map_list[p_row][p_col] == 8:
                map_list[p_row][p_col] = 5
        elif map_list[next_row][next_col] == 2:
            if map_list[box_next_row][box_next_col] == 0:
                map_list[box_next_row][box_next_col] = 2
                map_list[next_row][next_col] = 7
                if map_list[p_row][p_col] == 7:
                    map_list[p_row][p_col] = 0
                elif map_list[p_row][p_col] == 8:
                    map_list[p_row][p_col] = 5
            elif map_list[box_next_row][box_next_col] == 3:
                map_list[box_next_row][box_next_col] = 10
                map_list[next_row][next_col] = 7
                if map_list[p_row][p_col] == 7:
                    map_list[p_row][p_col] = 0
                elif map_list[p_row][p_col] == 8:
                    map_list[p_row][p_col] = 5
            elif map_list[box_next_row][box_next_col] == 5:
                notif.play()
                map_list[box_next_row][box_next_col] = 9
                map_list[next_row][next_col] = 7
                if map_list[p_row][p_col] == 7:
                    map_list[p_row][p_col] = 0
                elif map_list[p_row][p_col] == 8:
                    map_list[p_row][p_col] = 5
        elif map_list[next_row][next_col] == 3:
            notif.play()
            current_coins += 1
            map_list[next_row][next_col] = 7
            if map_list[p_row][p_col] == 7:
                map_list[p_row][p_col] = 0
            elif map_list[p_row][p_col] == 8:
                map_list[p_row][p_col] = 5
        elif map_list[next_row][next_col] == 4:
            if current_coins == coins_total and current_cells == boxes_total:
                is_win = True
        elif map_list[next_row][next_col] == 5:
            map_list[next_row][next_col] = 8
            if map_list[p_row][p_col] == 7:
                map_list[p_row][p_col] = 0
            elif map_list[p_row][p_col] == 8:
                map_list[p_row][p_col] = 5
        elif map_list[next_row][next_col] == 9:
            if map_list[box_next_row][box_next_col] == 0:
                map_list[box_next_row][box_next_col] = 2
                map_list[next_row][next_col] = 8
                if map_list[p_row][p_col] == 7:
                    map_list[p_row][p_col] = 0
                elif map_list[p_row][p_col] == 8:
                    map_list[p_row][p_col] = 5
            elif map_list[box_next_row][box_next_col] == 3:
                map_list[box_next_row][box_next_col] = 10
                if map_list[p_row][p_col] == 7:
                    map_list[p_row][p_col] = 0
                elif map_list[p_row][p_col] == 8:
                    map_list[p_row][p_col] = 5
            elif map_list[box_next_row][box_next_col] == 5:
                map_list[box_next_row][box_next_col] = 9
                map_list[next_row][next_col] = 8
                if map_list[p_row][p_col] == 7:
                    map_list[p_row][p_col] = 0
                elif map_list[p_row][p_col] == 8:
                    map_list[p_row][p_col] = 5
        elif map_list[next_row][next_col] == 10:
            if map_list[box_next_row][box_next_col] == 0:
                map_list[box_next_row][box_next_col] = 2
                if map_list[p_row][p_col] == 7:
                    map_list[p_row][p_col] = 0
                elif map_list[p_row][p_col] == 8:
                    map_list[p_row][p_col] = 5
            elif map_list[box_next_row][box_next_col] == 3:
                map_list[box_next_row][box_next_col] = 10
                if map_list[p_row][p_col] == 7:
                    map_list[p_row][p_col] = 0
                elif map_list[p_row][p_col] == 8:
                    map_list[p_row][p_col] = 5
            elif map_list[box_next_row][box_next_col] == 5:
                map_list[box_next_row][box_next_col] = 9
                if map_list[p_row][p_col] == 7:
                    map_list[p_row][p_col] = 0
                elif map_list[p_row][p_col] == 8:
                    map_list[p_row][p_col] = 5
            current_coins += 1
            map_list[next_row][next_col] = 7
        p_row = next_row
        p_col = next_col
        current_cells = 0
        for i in range(len(map_list)):
            for j in range(len(map_list[i])):
                if map_list[i][j] == 9:
                    current_cells += 1

        print(is_win)
        return p_col, p_row, next_row, next_col, box_next_row, box_next_col, map_list, current_coins, is_win, current_cells
    size = [1080, 720]
    screen = display.set_mode(size)
    display.set_caption('Sokoban')
    a_player = anim_list(transform.scale(image.load('content/avatar.png'),(96,96)), 32, 5)  # персонаж
    display.set_icon(a_player[1])
    bg = image.load(f'content/lvl{settings.current_level}/bg.jpg')
    road = image.load(f'content/lvl{settings.current_level}/ground.jpg')  # 0
    wall = image.load(f'content/lvl{settings.current_level}/wall.jpg')  # 1
    box = image.load('content/box1.png')  # 2
    a_coin = anim_list(image.load('content/coin_16.png'), 16, 11)  # 3
    door = image.load('content/door.png')  # 4
    star = image.load('content/cell.png')  # 5
    box_placed = image.load('content/box2.png')  # 9
    player_frame = 0
    coin_frame = 0
    font1 = font.Font('Bernhard.otf', 50)
    win = transform.scale(image.load('content/you_win.png'), size)
    notif = mixer.Sound('content/sfx/beep_notification.mp3')
    result = mixer.Sound('content/sfx/result_harmonic.mp3')
    next_player_row, next_player_col, k_nex_row, k_nex_col = 0,0,0,0
    gx, gy = 200, 200
    dx, dy = 32, 32
    ticks = time.get_ticks()
    run = True
    clock = time.Clock()
    current_boxes = 0
    current_coins = 0
    player_row, player_col = 0, 0
    map_list, coins_total, boxes_total = read_file(f'map{settings.current_level}.txt')
    is_win = False
    while run:
        if not is_win:
            for e in event.get():
                if e.type == QUIT:
                    run = False
                if e.type == KEYDOWN:
                    if e.key == K_ESCAPE:
                        run = False
                    next_player_row, next_player_col, k_nex_row, k_nex_col = define_following(player_row, player_col, e)
            player_row, player_col, next_player_row, next_player_col, box_next_row, box_next_col, map_list, current_coins, \
                    is_win, current_boxes = move_player(player_row, player_col, next_player_row, next_player_col,
                                                        k_nex_row, k_nex_col, map_list, current_coins, is_win,
                                                        current_boxes)
            player_row, player_col = draw_map(map_list, gx, gy, dx, dy)
            if coin_frame <= len(a_coin)-2:
                coin_frame += 1
            else:
                coin_frame = 0
            if player_frame <= len(a_player)-2:
                if ticks + 200 <= time.get_ticks():
                    player_frame +=1
                    ticks = time.get_ticks()
            else:
                player_frame = 0
            coins_text = font1.render('Score: ' + str(current_coins)+'/'+str(coins_total),True, [220, 220, 220])
            boxes_text = font1.render('Boxes: ' + str(current_boxes)+'/'+str(boxes_total),True, [220, 220, 220])
            screen.blit(coins_text, [100, 10])
            screen.blit(boxes_text, [100, 50])
        else:
            result.play()
            settings.current_level += 1
            print(settings.current_level)
            if settings.current_level <= 5:
                settings.config = settings.cfg_save()
                bg = image.load(f'content/lvl{settings.current_level}/bg.jpg')
                road = image.load(f'content/lvl{settings.current_level}/ground.jpg')  # 0
                wall = image.load(f'content/lvl{settings.current_level}/wall.jpg')  # 1
                map_list, coins_total, boxes_total = read_file(f'map{settings.current_level}.txt')
                current_coins = 0
                is_win = False
            else:
                screen.blit(win, [0, 0])

        display.flip()
        clock.tick(30)