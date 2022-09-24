# Напишите программу, которая принимает на вход координаты двух точек 
# и находит расстояние между ними в 2D пространстве.
# Пример:
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

import os, math
os.system("cls")
def user_input(a):
    while True:
        try:
            return int(input(a))            
        except:
            print('Неверный ввод. Должно быть целое число, повторите')

print('Введите координаты точки А')
x1 = user_input('X: ')
y1 = user_input('Y: ')
print('Введите координаты точки B')
x2 = user_input('X:')
y2 = user_input('Y:')
distance = math.sqrt(math.pow(x2 - x1, 2) + math.pow(y1 - y2, 2))
print(f'Расстояние между точками А и В - {round(distance, 3)}')
