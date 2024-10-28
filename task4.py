# При анализе данных, собранных в рамках научного эксперимента,
# бывает полезно удалить самое большое и самое маленькое значение.
# Сымитруем данные списком длины N со случайными числами в диапазоне от 0 до 1000
# Удалите из этого списка все значения, которые на 30 % отличаются
# от среднего значения списка
from random import randint

n=int(input())
lst=[randint(1, 1000) for i in range(n)]
print(lst)
sred=sum(lst)/n
for i in range(n):
    if lst[i]<=0.7*sred or lst[i]>=1.3*sred:
        lst[i]=0
answer=[]
for num in lst:
    if num!=0:
        answer.append(num)

print(answer)