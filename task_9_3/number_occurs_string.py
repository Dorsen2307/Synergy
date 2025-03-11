line = list(map(int, input("Введите числа через пробел: ").split()))
line_set = set(line)

for i in line_set:
    if line.count(i) > 1:
        print(f"{i} - YES")
    else:
        print(f"{i} - NO")