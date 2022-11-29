# 5. Реализуйте алгоритм перемешивания списка.

import random

number = list()
number2 = list()
n = 10
for i in range(n):
    number.append(i)
print('отсортированный список - ',number)
indexList = len(number)
for i in range(indexList,0,-1):
    if indexList > 0:
       element = random.choice(range(i))
       number2.append(number[element])
       number.pop(int(element))
    else:
        number2.append(number[0])
        break
print('перемешанный список - ',number2)