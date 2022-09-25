# Напишите программу для. проверки истинности утверждения
#  ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

import os
os.system("cls")
print('Проверка истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z')
x = (input('Введите x: '))
y = (input('Введите y: '))
z = (input('Введите z: '))
print((not(x or y or z)) == (not x and not y and not z))
