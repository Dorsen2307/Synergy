n = 0

while not(1 <= n <= 10000):
    n = int(input("Введите количество чисел: "))
    if not(1 <= n <= 10000):
        print("Количество должно быть от 1  до 10000!")

numbers = [int(input(f"Введите число {i + 1}: ")) for i in range(n)]

reversed_numbers = numbers[::-1]

print("Исходный список:\n", *numbers)
print("\nПеревёрнутый список:\n", *reversed_numbers)