# Посчитайте угол между двумя векторами размерности N.
# Примечание: Вспомните определение скалярного произведения.
# Изначально вектор заполните рандомными числами.
# Пример: N =3
# вектор a = [0, 1, 0]
# вектор b = [1, 0, 0]
# Угол = 90

from math import acos, pi
n=int(input())
lst_a=list(map(int, input().split()))
lst_b=list(map(int, input().split()))
summ=0
len_a=0
len_b=0
if n==0:
    print('n=0  это точка')
elif lst_a.count(0)==n or lst_b.count(0)==n:
    print('один из векторов точка')
else:
    for i in range(n):
        a = lst_a[i]
        b = lst_b[i]
        summ += a*b
        len_a += a**2
        len_b += b**2
    cos = summ/(len_a*len_b)**0.5

    print(acos(cos)*180/pi)


