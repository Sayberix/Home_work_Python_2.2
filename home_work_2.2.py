# 1. Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

#   Пример:
#   0,56 -> 11

number = input('Введите число: ')
sum = 0
if number.isdigit() or float(number):
    for i in range(len(number)):
        if number[i].isdigit():
            sum += int(number[i])
else:
    print('Неверный ввод! Введеные символы должны быть числом!')
print('Сумма цифр числа',number, 'равно: ',sum)
