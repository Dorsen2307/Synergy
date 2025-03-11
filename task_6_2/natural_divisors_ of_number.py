x = 0
while not(0 < x <= 2 ** 9):
    x = int(input("Введите число: "))
    if not (0 < x <= 2 ** 9):
        print("Число должно быть от 0 до 2e9!")

i = 1
result = 0
while i * i <= x:
    if x % i == 0:
        if i * i == x:
            result += 1
        else:
            result += 2
    i += 1
print(f"Количество натуральных делителей числа {x}: {result}")