number_int = input("Введите пятизначное число: ")

if len(number_int) == 5:
    dozens = int(number_int[-1])
    units = int(number_int[-2])
    hundreds = int(number_int[-3])
    thousands = int(number_int[-4])
    tens_thousands = int(number_int[-5])

    print(f"({units}^{dozens} * {hundreds}) / ({tens_thousands} - {thousands}) = "
          f"{float((units ** dozens * hundreds) / (tens_thousands - thousands))}")
else:
    print("Это не 5-ти значное число!")