# 🌲 🟦 🚁 🟩 🔥 🏥 ❤️ 🗑️ 🏛️ ☁️ ⚡ 🏆
import os
import time
from pynput import keyboard
from clouds import Clouds
from helicopter import Helicopter
from map import Map
import json

TICK_SLEEP = 0.05
TREE_UPDATE = 50
CLOUDS_UPDATE = 100
FIRE_UPDATE = 75
MAP_W, MAP_H = 20, 10

field = Map(MAP_W, MAP_H)
clouds = Clouds(MAP_W, MAP_H)
helicopter = Helicopter(MAP_W, MAP_H)

MOVES = {'w': (-1, 0), 'd': (0, 1), 's': (1, 0), 'a': (0, -1)}
# f - сохранение, g - восстановление
def process_key(key):
    """Обработка нажатий клавиш"""
    global helicopter, tick, clouds, field

    try:
        if hasattr(key, 'char') and key.char is not None:
            key_lower = key.char.lower()
            # обработка движений вертолета
            if key_lower in MOVES:
                dx, dy = MOVES[key_lower]
                if helicopter:
                    helicopter.move(dx, dy)

            # сохранение игры
            if key_lower == 'f':
                data = {
                    "helicopter": helicopter.export_data(),
                    "clouds": clouds.export_data(),
                    "field": field.export_data(),
                    "tick": tick
                }
                with open("level.json", "w") as file:
                    json.dump(data, file)
            # загрузка игры
            elif key_lower == 'g':
                with open("level.json", "r") as file:
                    data = json.load(file)
                    helicopter.import_data(data["helicopter"])
                    tick = data["tick"] or 1
                    field.import_data(data["field"])
                    clouds.import_data(data["clouds"])
    except AttributeError:
        print("OOOPS")

# слушатель событий нажатия клавиш
listener = keyboard.Listener(
    on_press=None,
    on_release=process_key)
listener.start()

tick = 1

while True:
    os.system('cls' if os.name == 'nt' else 'clear') # cls
    field.process_helicopter(helicopter, clouds)
    helicopter.print_status()
    field.print_map(helicopter, clouds)
    print("TICK", tick)
    tick += 1
    time.sleep(TICK_SLEEP)
    if tick % TREE_UPDATE == 0:
        field.generate_tree()
    if tick % FIRE_UPDATE == 0:
        field.update_fires()
    if tick % CLOUDS_UPDATE == 0:
        clouds.update()