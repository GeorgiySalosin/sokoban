from pygame import *
from configparser import ConfigParser
def cfg_load():
    config_path = 'config.ini'
    config = ConfigParser()

    try:
        with open(config_path) as f:
            config.read_file(f)
    except FileNotFoundError:
        config['DATA'] = {
            "level": '1',
            "lvl_1_min_moves": '0',
            "lvl_1_last_moves": '0',
            "lvl_2_min_moves": '0',
            "lvl_2_last_moves": '0',
            "lvl_3_min_moves": '0',
            "lvl_3_last_moves": '0',
            "lvl_4_min_moves": '0',
            "lvl_4_last_moves": '0',
            "lvl_5_min_moves": '0',
            "lvl_5_last_moves": '0'
        }
        config['SETTINGS'] = {
            "bind_up": str(K_w),
            "bind_down": str(K_s),
            "bind_left": str(K_a),
            "bind_right": str(K_d)
        }
        with open(config_path, 'w') as f:
            config.write(f)
    return config
def cfg_save():
    config_path = 'config.ini'
    config = ConfigParser()
    config['DATA'] = {
        "level": f'{current_level}',
        "lvl_1_min_moves": f'{lvl_1_min_moves}',
        "lvl_1_last_moves": f'{lvl_1_last_moves}',
        "lvl_2_min_moves": f'{lvl_2_min_moves}',
        "lvl_2_last_moves": f'{lvl_2_last_moves}',
        "lvl_3_min_moves": f'{lvl_3_min_moves}',
        "lvl_3_last_moves": f'{lvl_3_last_moves}',
        "lvl_4_min_moves": f'{lvl_4_min_moves}',
        "lvl_4_last_moves": f'{lvl_4_last_moves}',
        "lvl_5_min_moves": f'{lvl_5_min_moves}',
        "lvl_5_last_moves": f'{lvl_5_last_moves}'
    }
    config['SETTINGS'] = {
        "bind_up": f'{bind_up}',
        "bind_down": f'{bind_down}',
        "bind_left": f'{bind_left}',
        "bind_right": f'{bind_right}'
    }
    with open(config_path, 'w') as f:
        config.write(f)
    with open(config_path, 'r') as f:
        config.read_file(f)
    return config
config = cfg_load()
current_level = int(config['DATA']["level"])
lvl_1_min_moves = int(config['DATA']["lvl_1_min_moves"])
lvl_1_last_moves = int(config['DATA']["lvl_1_last_moves"])
lvl_2_min_moves = int(config['DATA']["lvl_2_min_moves"])
lvl_2_last_moves = int(config['DATA']["lvl_2_last_moves"])
lvl_3_min_moves = int(config['DATA']["lvl_3_min_moves"])
lvl_3_last_moves = int(config['DATA']["lvl_3_last_moves"])
lvl_4_min_moves = int(config['DATA']["lvl_4_min_moves"])
lvl_4_last_moves = int(config['DATA']["lvl_4_last_moves"])
lvl_5_min_moves = int(config['DATA']["lvl_5_min_moves"])
lvl_5_last_moves = int(config['DATA']["lvl_5_last_moves"])

bind_up = int(config['SETTINGS']["bind_up"])
bind_down = int(config['SETTINGS']["bind_down"])
bind_left = int(config['SETTINGS']["bind_left"])
bind_right = int(config['SETTINGS']["bind_right"])
