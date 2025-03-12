class Turtles:
    x = 10
    y = 10
    s = 1

    def go_up(self):
        """Двигаться вверх"""
        self.y += self.s

    def go_down(self):
        """Двигаться вниз"""
        self.y -= self.s

    def go_left(self):
        """Двигаться влево"""
        self.x -= self.s

    def go_right(self):
        """Двигаться вправо"""
        self.x += self.s

    def evolve(self):
        """Увеличивает скорость"""
        self.s += 1

    def degrade(self):
        """Уменьшает скорость"""
        if self.s > 1:
            self.s -= 1
        else:
            print("Скорость может стать '0'!")

    def count_moves(self, x2, y2):
        """Возвращает минимальное количество ходов, за которое черепашка сможет добраться до позиции (x2, y2)"""
        # вычисляем расстояние до цели
        distance_x = abs(x2 - self.x)
        distance_y = abs(y2 - self.y)

        # находим минимальное количество ходов
        moves_x = (distance_x + self.s - 1) // self.s
        moves_y = (distance_y + self.s - 1) // self.s

        return moves_x + moves_y

turtle = Turtles()

print(f"Начальная позиция: ({turtle.x}, {turtle.y}), скорость: {turtle.s}")

# Двигаем черепашку
turtle.go_up()
turtle.go_right()
turtle.go_up()
turtle.go_right()

print(f"Текущая позиция: ({turtle.x}, {turtle.y}), скорость: {turtle.s}")

turtle.evolve()
print(f"Увеличили скорость: {turtle.s}")

moves = turtle.count_moves(10, 10)
print(f"Минимальное количество ходов до (10, 10): {moves}")