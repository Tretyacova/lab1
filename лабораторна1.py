#варіант 26
from math import *
x = input("введіть число х:")
x = int(x)
import math
z = (2*math.tan(x) - x**0.5)/x
print(z)

# Знайти суму всіх чисел від х до у, кратних числу 3
result = 0
for i in range(0,40):
    if (i % 3 == 0):
        result = result + i
print(result)

#Знайти мінімальний додатний елемент
L = [i for i in range (10)]
print(min(L))

#Вивести ненульові елементи на екран у зворотному порядку
L = [i for i in range (10)]
L.reverse()
print(L)

#Обчислити добуток не нульових елементів масиву
from functools import reduce
res = reduce(lambda x, y: x*y, [1,2,3,4,5,6,7,8,9,10])
print(res)
