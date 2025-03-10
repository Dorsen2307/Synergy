
def count_common_numbers(lst1, lst2):
    set1 = set(lst1)
    set2 = set(lst2)

    common_numbers = set1.intersection(set2)
    return len(common_numbers)

n1 = 0
n2 = 0

while not(1 <= n1 <= 100000):
    n1 = int(input("Введите количество чисел в первом списке: "))
    if not(1 <= n1 <= 100000):
        print("Количество не должно превышать 100000!")

list1 = [int(input()) for _ in range(n1)]

while not(1 <= n2 <= 100000):
    n2 = int(input("Введите количество чисел во втором списке: "))
    if not(1 <= n2 <= 100000):
        print("Количество не должно превышать 100000!")

list2 = [int(input()) for _ in range(n2)]

res = count_common_numbers(list1, list2)

print(f"Количество чисел, содержащихся в обоих списках: {res}.")