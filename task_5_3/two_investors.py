sum_michael = int(input("Сколько долларов у Майкла? "))
sum_ivan = int(input("Сколько долларов у Ивана? "))
min_sum_inv = int(input("Введите минимальную сумму инвестирования: "))

if sum_michael > min_sum_inv and sum_ivan > min_sum_inv:
    res = 2
elif sum_michael > min_sum_inv:
    res = "Mike"
elif sum_ivan > min_sum_inv:
    res = "Ivan"
elif sum_michael + sum_ivan > min_sum_inv:
    res = 1
else:
    res = 0

print(res)