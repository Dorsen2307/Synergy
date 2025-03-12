class Transport:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

autobus = Transport("Renault Logan", 180, 12)

print(f"Название автомобиля: {autobus.name}\n"
      f"Скорость: {autobus.max_speed} км/ч\n"
      f"Пробег: {autobus.mileage} км")