x = int(input("Введите число: "))

if x <= 2e9:
    i = 1
    result = 0
    while i * i <= x:
        if x % i == 0 and i * i != x:
            result += 2
        elif x % i == 0 and i * i == x:
            result += 1
        i += 1
    print(f"Количество натуральных делителей числа {x}: {result}")