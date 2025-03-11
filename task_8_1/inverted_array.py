n = 0
k = True
summ = 0
numbers = []

# запрос количества чисел
while not(1 <= n <= 10000):
    n = int(input("Введите количество чисел (от 1 до 10000): "))
    if not(1 <= n <= 10000):
        print("Количество должно быть от 1  до 10000!\n")

# запрос чисел и проверка их суммы
while k:
    numbers = [int(input(f"Введите число {i + 1}: ")) for i in range(n)]

    if len(numbers) == n:
        for i in range(len(numbers)):
            summ += numbers[i]

        if 1 <= summ <= 10 ** 9:
            k = False
        else:
            summ = 0
            print("Значение должно быть от 1 до 10e9!\n")
    else:
        print("Неверное количество значений!\n")

reversed_numbers = numbers[::-1]

print("Исходный список:\n", *numbers)
print("\nПеревёрнутый список:\n", *reversed_numbers)