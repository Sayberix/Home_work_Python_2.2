# 5. Реализуйте алгоритм перемешивания списка.

import random

number = list()
print('инициализированный список - ',number)
n = 10
for i in range(n):
    number.append(i)
print('отсортированный список - ',number)
random.shuffle(number)
print('перемешанный список - ',number)