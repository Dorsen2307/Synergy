n = int(input("Сколько будет целых чисел? "))
result = 0

for i in range(n):
    if int(input(f"Введите {i + 1} целое число: ")) == 0:
        result += 1

print(f"\nКоличество целых чисел, равных 0: {result}")