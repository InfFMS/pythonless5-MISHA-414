# Заполнить массив длины N случайными числами в интервале [-100,100] и
# переставить элементы так, чтобы все положительные элементы
# стояли в начала массива, а все отрицательные и нули в конце.
# Пример: ввод N = 6
# [20, -90, 15, -34, 10, 0]
# Вывод: [20, 15, 10, -90, -34, 0]
from random import randint

n=int(input())
lst=[randint(-100, 100) for i in range(n)]

positive=[]
negative=[]
for num in lst:
    if num>0:
        positive.append(num)
    else:
        negative.append(num)
print(positive+negative)