a = int(input("Введите первое целое число: "))
b = int(input("Введите второе целое число, больше первого: "))

if a <= b:
    for i in range(a, b + 1):
        if i % 2 == 0:
            print(i, end=" ")
else:
    print(f"{a} НЕ меньше {b}!")