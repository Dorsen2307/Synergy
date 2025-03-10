n = 0
line = []
k = 0

while not(1 <= n <=100000):
    n = int(input("Введите количество чисел: "))
    if not(1 <= n <= 100000):
        print("Число должно быть от 1 до 100000!\n")

while k == 0:
    line = list(map(int, (input(f"Введите числа через пробел ({n} шт.): ")).split()))

    if len(line) == n:
        for i in range(n - 1):
            if abs(line[i]) >= (2 * 10e9):
                k = 0
                print("Число в списке превышает 2*10e9!\n")
                break
            else:
                k = 1
    else:
        print("Количество введенных чисел больше указанного!\n")

quantity = len(set(line))
print(f"\nИсходный список: ", *line)
print(f"Количество различных чисел в исходном списке: {quantity}")