# Напишите программу, которая удаляет дубликаты из списка длины N.
# Пример работы:
# Пример: ввод N = 8
# [10, 20, 10, 20, 30, 40, 30, 50]
# После удаления дублей:  [10, 20, 30, 40, 50]
lst=list(map(int, input().split()))
sin_duble=[]
for num in lst:
    if not(num in sin_duble):
        sin_duble.append(num)
print(sin_duble)
