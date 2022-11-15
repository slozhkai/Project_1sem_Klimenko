# Вариант 10

# Дан массив размера N. Найти количество его промежутков монотонности (то есть участков, на которых его элементы
#   возрастают или убывают).

from random import randint

while True:
    try:
        n = int(input('Введите размер вашего списка: '))
        a = [randint(1, 25) for i in range(n)]
        print(a)
        num = 0
        for i in range(1, n):
            if a[i - 1] <= a[i] and a[i - 1] < a[i - 2]:
                num += 1
            if a[i] <= a[i - 1] and a[i - 1] > a[i - 2]:
                num += 1
        print(num)

    except ValueError:
        print('Некорректно введенные данные')
