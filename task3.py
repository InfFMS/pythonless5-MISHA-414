from random import randint
# Заполните массив длины N случайными числами в интервале [0,100].
# Определить, есть ли в нем элементы с одинаковыми значениями,
# не обязательно стоящие рядом.
# Если есть, то выведете значение и индекс повторяющихся элементов
# Если нет, то написать "Нет"
# Пример: ввод N = 6
# [1, 2, 3, 2, 5, 10]
# Вывод:
# значение:2 индексы 1 и 3
n=int(input())
lst=[randint(1, 100) for i in range(n)]
print(lst)
count_lst=[[]]*100
count=0
for ind in range(n):

    num=lst[ind]

    if num==0:
        continue
    count_lst[num-1].append(ind)
    lst[ind]=0
    print(count_lst)
    for i in range(ind+1, n):
        if lst[i]==num:
            count+=1
            count_lst[num - 1].append(i)
            lst[i]=0



'''
if count==0:
    print('NO')
else:
    for i in range(100):
        indexes=count_lst[i]
        if len(indexes)>1:
            print(f'значения {i+1}: {indexes}')'''

