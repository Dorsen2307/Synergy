n = int(input("Введите количество чисел: "))

numbers = [int(input(f"Введите число {i + 1}: ")) for i in range(n)]

reversed_numbers = numbers[::-1]

print("Исходный список:\n", *numbers)
print("\nПеревёрнутый список:\n", *reversed_numbers)