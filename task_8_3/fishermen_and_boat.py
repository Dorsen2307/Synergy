def min_boat(weights, weight_limit):
    """Возвращает минимальное количество лодок, необходимых для перевозки рыбаков."""
    weights.sort() # сортируем список

    easy_fishermen = 0 # самый легкий рыбак
    heavy_fishermen = len(weights) - 1 # самый тяжелый рыбак
    count_boats = 0 # счетчик лодок

    while easy_fishermen <= heavy_fishermen:
        if weights[easy_fishermen] + weights[heavy_fishermen] <= weight_limit:
            easy_fishermen += 1 # убираем самого легкого

        heavy_fishermen -= 1 # убираем самого тяжелого
        count_boats += 1 # увеличиваем счетчик лодок

    return count_boats

def get_positive_integer(prompt, min_value, max_value):
    """Запрашивает у пользователя ввод положительного целого числа в заданном диапазоне."""
    while True:
        value = int(input(prompt))
        if min_value <= value <= max_value:
            return value
        else:
            print(f"Значение должно быть между {min_value} и {max_value}.\n")

weight_in_boat = get_positive_integer("Введите вес, который может выдержать лодка: ", 1, 10**6)
number_fishermen = get_positive_integer("Введите количество рыбаков (от 1 до 100): ", 1, 100)

fishermens_weight = []
for i in range(number_fishermen):
    weight = get_positive_integer(f"Введите вес {i + 1} рыбака: ", 1, weight_in_boat)
    fishermens_weight.append(weight)

print(f"\nЛодка может выдержать вес в {weight_in_boat} кг.\n"
      f"Количество рыбаков: {number_fishermen}\n"
      "Вес каждого рыбака: ", *fishermens_weight, end="\n")
print(f"Минимально необходимое количество лодок: {min_boat(fishermens_weight, weight_in_boat)}")