# Массив имеет четное число элементов N.
# Заполнить массив случайными числами и
# выполнить реверс отдельно в первой половине и второй половине.
# Пример: ввод N = 6
# [1,2,3,4,5,6]
# Вывод: [3,2,1,6,5,4]
from random import randint
def invers(list, len):
    answer=[]
    for i in range(-1, -1*len-1, -1):
        answer.append(list[i])
    return answer

n=int(input())
lst=[randint(1, 10) for i in range(n)]
print(lst)

left=lst[:n//2]
right=lst[n//2:]

print(invers(left, n//2), invers(right, n//2))