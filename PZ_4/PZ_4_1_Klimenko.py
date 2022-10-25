#Вариант 10
n = int(input()) #Ввод числа
i = 0
result = 0
while n + 1 != i: #Условие цикла
    result += (n + i) ** 2 #Тело цикла
    i += 1
print(result) #Вывод результата
