# Напишите программу, которая принимает на вход цифру, обозначающую день недели,
#  и проверяет, является ли этот день выходным.
# Пример:
# - 6 -> да
# - 7 -> да
# - 1 -> нет

import os
os.system("cls")
while True:
    num_weekday = input('Введите порядковый номер дня недели от 1 до 7: ')
    if not num_weekday.isnumeric():
        print("Введено не число, повторите ввод")
    elif not 0 < int(num_weekday) < 8:
        print("Ваше число не диапазоне, повторите ввод")
    else:
        break
num_weekday = int(num_weekday)
if num_weekday == 6 or num_weekday == 7:
    print('Это выходной? Да')
else:
    print('Это выходной? Нет')