class Transport:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

Autobus = Transport("Renault Logan", 180, 12)

print(f"Название автомобиля: {Autobus.name}\n"
      f"Скорость: {Autobus.max_speed} км/ч\n"
      f"Пробег: {Autobus.mileage} км")