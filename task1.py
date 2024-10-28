from random import sample
# Заполните список длины N случайными числами в диапазоне от 0 до 1000
# Выведите:
# 1.длину списка;
# 2.последний элемент списка;
# 3.список в обратном порядке (вспоминаем срезы);
# 4.YES, если список содержит трехзначное число, состоящее из одинаковых цифр
# NO в противном случае;
# 5.список с удаленными первым и последним элементами.
def only_num(num):

    while num>9:
        if num%10!=num//10%10:
            return 0
        num=num//10
    return 1


nums=[i for i in range(1, 1001)]
n=int(input())
lst=sample(nums, n)

print(n)
print(lst[-1])
print(lst[::-1])

for num in lst:
    if only_num(num) and num>99 and num<1000:
        print('Yes')
        break
else:
    print('No')
print(lst[1:-1])
