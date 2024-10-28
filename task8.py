# Заполнить массив длины N случайными числами в диапазоне от 10 до 100000 и
# отобрать в другой массив все числа, которые состоят из одинаковых цифр.
# Используйте для этого логическую функцию.
# Пример: ввод N = 4
# [12, 77, 5555, 97]
# Вывод: [77, 5555]
from random import randint
def only_num(num):

    while num>9:
        if num%10!=num//10%10:
            return 0
        num=num//10
    return 1

n=int(input())
lst=[randint(10, 100000) for i in range(n)]
answer=[]
for num in lst:
    if only_num(num):
        answer.append(num)
print(answer)
