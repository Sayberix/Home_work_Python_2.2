# 4. Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных индексах. Индексы вводятся одной строкой, через пробел.
# 
# Пример:
# n = 3
# [-3, -2, -1, 0, 1, 2, 3]
# --> 0 2 3
# -3 * -1 * 0 = 0
# Вывод: 0

n = int(input('Введите целое число: '))
listOfNumber = list()
countList = 0
for i in range(-n,n+1):
    listOfNumber.append(i)
    countList += 1
print(listOfNumber, 'количество элементов в списке: ', countList)
seq = input('Введите индексы элементов через пробел, произведение которых необходимо найти: ')
multiplication = 1
for i in range(len(seq)):
    if seq[i].isdigit():
        if int(seq[i]) < countList:
            multiplication *= listOfNumber[int(seq[i])]
        else:
            print('Ошибка в вводе. Введенный элемент вне диапазона списка. Программа завершает работу!')
            break
    if i == len(seq)-1:
        print('Произведение выбранных элементов: ', multiplication)