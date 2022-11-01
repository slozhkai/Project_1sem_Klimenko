# Вариант 10

# Дано целое число N(>0). Найти сумму N^2 + (N+1)^2  + (N+2)^2 + ... + (2N)^2

try:
    n = int(input("Введите число n: "))
    i = 0
    result = 0
    while n + 1 != i:
        result += (n + i) ** 2
        i += 1
    print(result)
except ValueError:
    print('Ошбика ввода данных')
