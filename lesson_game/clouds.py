# 0 - ничего нет
# 1 - обычное облако
# 2 - грозовое облако
from utils import randbool


class Clouds:
    def __init__(self, w, h):
        self.w = w
        self.h = h
        self.cells = [[0 for i in range(w)] for j in range(h)]

    def update(self, r = 1, rmx = 20, g = 1, mxg = 10):
        """Обновление облаков"""
        for i in range(self.h):
            for j in range(self.w):
                if randbool(r, rmx):
                    self.cells[i][j] = 1
                    if randbool(g, mxg):
                        self.cells[i][j] = 2
                else:
                    self.cells[i][j] = 0

    def export_data(self):
        """Экспорт данных облаков"""
        return {
            "cells": self.cells,
        }

    def import_data(self, data):
        """Импорт данных облаков"""
        self.cells = data["cells"] or [[0 for i in range(self.w)] for j in range(self.h)]