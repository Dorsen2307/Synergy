def min_boat(weight_f, weight_b, number_f):
    weight_f.sort() # сортируем список

    easy_fishermen = 0 # самый легкий рыбак
    heavy_fishermen = number_f - 1 # самый тяжелый рыбак
    count_boats = 0 # счетчик лодок

    while easy_fishermen <= heavy_fishermen:
        if weight_f[easy_fishermen] + weight_f[heavy_fishermen] <= weight_b:
            easy_fishermen += 1 # убираем самого легкого

        heavy_fishermen -= 1 # убираем самого тяжелого
        count_boats += 1 # увеличиваем счетчик лодок

    return count_boats

weight_in_boat = 0
number_fishermen = 0
weight = 0

while (weight_in_boat < 1) or (weight_in_boat > 10e6):
    weight_in_boat = int(input("Введите вес, который может выдержать лодка: "))
    if (weight_in_boat > 10e6) or (weight_in_boat < 1):
        print(f"Вес должен быть между 1 и 10млн.\n")

while (number_fishermen < 1) or (number_fishermen > 100):
    number_fishermen = int(input("Введите количество рыбаков: "))
    if (number_fishermen > 100) or (number_fishermen < 1):
        print(f"Количество рыбаков должно быть между 1 и 100.\n")

fishermens_weight = [0 for i in range(number_fishermen)]
for i in range(number_fishermen):
    while (fishermens_weight[i] < 1) or (fishermens_weight[i] > weight_in_boat):
        weight = int(input(f"Введите вес {i + 1} рыбака: "))
        if (weight > weight_in_boat) or (weight < 1):
            print(f"Вес должен быть между 1 и {weight_in_boat}.\n")
        else:
            fishermens_weight[i] = weight

print(f"\nЛодка может выдержать вес в {weight_in_boat} кг.\n"
      f"Количество рыбаков: {number_fishermen}\n"
      "Вес каждого рыбака: ", *fishermens_weight, end="\n")
print(f"Минимально необходимое количество лодок: {min_boat(fishermens_weight, weight_in_boat, number_fishermen)}")