# Введите массив длины N с клавиатуры и найдите (за один проход)
# количество элементов, имеющих максимальное значение.
lst=list(map(int, input().split()))
count= 0
ma=lst[0]
for i in range(len(lst)):
    if lst[i]==ma:
        count+=1
    elif lst[i]>ma:
        count=1
        ma=lst[i]
print(count)