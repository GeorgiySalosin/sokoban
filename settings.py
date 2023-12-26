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
            "level": '1'
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
        "level": f'{current_level}'
    }
    config['SETTINGS'] = {
        "bind_up": f'{bind_up}',
        "bind_down": f'{bind_down}',
        "bind_left": f'{bind_left}',
        "bind_right": f'{bind_right}'
    }
    with open(config_path, 'w') as f:
        config.write(f)
    return config
config = cfg_load()
current_level = int(config['DATA']["level"])
bind_up = int(config['SETTINGS']["bind_up"])
bind_down = int(config['SETTINGS']["bind_down"])
bind_left = int(config['SETTINGS']["bind_left"])
bind_right = int(config['SETTINGS']["bind_right"])
