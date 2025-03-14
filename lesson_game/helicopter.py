import os
from utils import randcell

# tank - запас воды
# mxtank - максимальный запас воды

class Helicopter:
    def __init__(self, w, h):
        rc = randcell(w, h)
        rx, ry = rc[0], rc[1]
        self.x, self.y = rx, ry
        self.w = w
        self.h = h
        self.tank = 0
        self.mxtank = 1
        self.score = 0
        self.lives = 20

    def move(self, dx, dy):
        nx, ny = dx + self.x, dy + self.y
        if 0 <= nx < self.h and 0 <= ny < self.w:
            self.x, self.y = nx, ny

    def print_status(self):
        print(f"💧{self.tank}/{self.mxtank} | "
              f"🏆{self.score} | "
              f"❤️{self.lives}")

    def game_over(self):
        global helico
        text = f"GAME OVER, YOUR SCORE IS {self.score}"
        os.system('cls' if os.name == 'nt' else 'clear')
        print("=" * (len(text) + 4))
        print("|" + " " * (len(text) + 2) + "|")
        print(f"| {text} |")
        print("|" + " " * (len(text) + 2) + "|")
        print("=" * (len(text) + 4))
        exit(0)

    def export_data(self):
        return {
            "score": self.score,
            "lives": self.lives,
            "x": self.x, "y": self.y,
            "tank": self.tank, "mxtank": self.mxtank,
        }

    def import_data(self, data):
        self.x = data["x"] or 0
        self.y = data["y"] or 0
        self.tank = data["tank"] or 0
        self.mxtank = data["mxtank"] or 1
        self.score = data["score"] or 0
        self.lives = data["lives"] or 3