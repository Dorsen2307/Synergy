def modified_array(array):
    """Сдвигает элементы массива, перемещая последний элемент в начало."""
    array.insert(0, array[-1])
    array.pop()
    return array

n = 0
summ = 0
arr = []

# запрос количества чисел
while not(1 <= n <= 100000):
    n = int(input("Введите количество чисел: "))
    if not(1 <= n <= 100000):
        print("Значение должно быть от 1 до 100000!\n")

# запрос чисел и проверка их суммы
while True:
    arr = list(map(int, input("Введите числа через пробел: ").split()))

    if len(arr) == n:
        for i in range(len(arr)):
            summ += arr[i]

        if 1 <= summ <= 10 ** 9:
            break # завершаем цикл, если сумма в пределах
        else:
            summ = 0
            print("Значение должно быть от 1 до 10e9!\n")
    else:
        print("Неверное количество значений!")

print("Исходный список:\n ", *arr)
print("Измененный список по 1 методу:\n ", *modified_array(arr))