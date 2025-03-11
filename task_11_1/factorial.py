def factorial(number):
    """Вычисляет факториал числа"""
    result = 1

    for i in range(2, number + 1):
        result *= i

    return result

def list_factorial(rf):
    """Заполняет список результатами вычислений факториалов"""
    list_factorials = [factorial(i) for i in range(rf, 0, -1)]
    return list_factorials

n = int(input("Введите число: "))

result_factorial = factorial(n)
result_list_factorial = list_factorial(result_factorial)

print(f"\nФакториал числа '{n}' = {result_factorial}")
print(f"Список факториалов числа '{result_factorial}':\n{result_list_factorial}")
