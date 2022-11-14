# Вариант 10

# Дан список A размера N и целое число K (1 < K < N). Вывести элементы списка с
# порядковыми номерами, кратными K: AK, A2*K, A3*K,... .
# условный оператор не использовать.

import random

try:
    a = []
    n = random.randint(1, 20)
    k = random.randrange(1, n)
    i = 0
    while i < n:
        a.append(random.randint(0, 10))
        i += 1

    for s in range((k - 1), n, k):
        print("Элемент:", a[s], "Порядковый номер:", s + 1)
except:
    print("Некорректно введеные данные")



