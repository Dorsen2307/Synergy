line = input("Введите строку без пробелов: ")

if line == line[::-1]:
    print("yes")
else:
    print("no")