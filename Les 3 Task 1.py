from typing import Any, Union

a = int(input('Введите число a - делимое:'))
b = int(input('Введите число b - делитель:'))

def calc(num1, num2):
    if a >= 0 and b >= 1:
        print('частное =', a / b)
    else:
        print('На 0 делить нельзя!')

calc(a,b)


