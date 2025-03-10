def modified_array_1(array):
    array.insert(0, array[-1])
    array.pop()
    return array

def modified_array_2(array):
    modify_array = []
    for i in range(len(array)):
        modify_array.append(array[len(array) - 1 - i // 2] if i % 2 == 0 else array[i // 2])

    return modify_array

n = int(input("Введите количество чисел: "))

arr = list(map(int, input("Введите числа через пробел: ").split()))

print("Исходный список:\n ", *arr)
print("Измененный список по 1 методу:\n ", *modified_array_1(arr))
print("Измененный список по 2 методу:\n ", *modified_array_2(arr))