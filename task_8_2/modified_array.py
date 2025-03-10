def modified_array_1(array):
    array.insert(0, array[-1])
    array.pop()
    return array

def modified_array_2(array):
    modify_array = []
    for i in range(len(array)):
        modify_array.append(array[len(array) - 1 - i // 2] if i % 2 == 0 else array[i // 2])

    return modify_array

n = 0
summ = 0
k = 0
arr = []

while not(1 <= n <= 100000):
    n = int(input("Введите количество чисел: "))
    if not(1 <= n <= 100000):
        print("Значение должно быть от 1 до 100000!\n")

while k == 0:
    arr = list(map(int, input("Введите числа через пробел: ").split()))

    if len(arr) == n:
        for i in range(len(arr)):
            summ += arr[i]
        if 1 <= summ <= 10e9:
            k = 1
        else:
            k = 0
            summ = 0
            print("Значение должно быть от 1 до 10e9!\n")
    else:
        print("Неверное количество значений!")

print("Исходный список:\n ", *arr)
print("Измененный список по 1 методу:\n ", *modified_array_1(arr))
print("Измененный список по 2 методу:\n ", *modified_array_2(arr))