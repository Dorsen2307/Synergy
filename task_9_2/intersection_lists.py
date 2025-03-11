def count_common_numbers(lst1, lst2):
    """Возвращает количество общих чисел в двух списках."""
    set1 = set(lst1)
    set2 = set(lst2)

    common_numbers = set1.intersection(set2)
    return len(common_numbers)

def get_positive_integer(prompt, min_value, max_value):
    """Запрашивает у пользователя ввод положительного целого числа в заданном диапазоне."""
    while True:
        value = int(input(prompt))
        if min_value <= value <= max_value:
            return value
        else:
            print(f"Число должно быть от {min_value} до {max_value}!\n")

def get_number_list(n):
    """Запрашивает у пользователя ввод n целых чисел и возвращает список."""
    numbers = []
    for i in range(n):
        while True:
            number = int(input(f"Введите число {i + 1}: "))
            numbers.append(number)
            break
    return numbers

n1 = get_positive_integer("Введите количество чисел в первом списке: ", 1, 100000)
list1 = get_number_list(n1)

n2 = get_positive_integer("Введите количество чисел во втором списке: ", 1, 100000)
list2 = get_number_list(n2)

res = count_common_numbers(list1, list2)

print(f"Количество чисел, содержащихся в обоих списках: {res}.")