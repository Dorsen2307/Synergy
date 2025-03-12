my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]

def output_list(n):
    print(my_list[n])
    if n < len(my_list) - 1:
        n += 1
        output_list(n)
    else:
        print("Конец списка")

output_list(0)