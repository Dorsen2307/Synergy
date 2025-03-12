import random

def get_matrix(a, b, n):
    """Генерирует матрицу размерностью axb с числами в диапазоне от -n до n"""
    result = [[random.randint(-n, n) for i in range(b)] for j in range(a)]
    return result

def output_matrix(*args):
    """Выводит матрицу на экран"""
    count = 0
    for m in args:
        print(f"Матрица {count + 1}")

        for i in range(len(m)):
            print(m[i])
        print("")

        count += 1

def matrix_addition(m1, m2):
    """Считает сумму двух равнозначных матриц"""
    m3 = []
    row = len(m1)
    col = len(m1[0])

    for r in range(row):
        m3.append([])
        for c in range(col):
            m3[r].append(m1[r][c] + m2[r][c])

    return m3

matrix_1 = get_matrix(4, 4, 100)
matrix_2 = get_matrix(4, 4, 100)
matrix_3 = matrix_addition(matrix_1, matrix_2)

output_matrix(matrix_1, matrix_2, matrix_3)