n = 0
line = []
k = True

while not(1 <= n <=100000):
    n = int(input("Введите количество чисел: "))
    if not(1 <= n <= 100000):
        print("Число должно быть от 1 до 100000!\n")

while k:
    line = list(map(int, (input(f"Введите числа через пробел ({n} шт.): ")).split()))

    if len(line) == n:
        for num in line:
            if abs(num) >= 2 * (10 ** 9):
                k = True
                print("Число в списке превышает 2*10e9 по модулю!\n")
                break
            else:
                k = False
    else:
        print("Количество введенных чисел больше указанного!\n")

quantity = len(set(line))
print(f"\nИсходный список: ", *line)
print(f"Количество различных чисел в исходном списке: {quantity}")