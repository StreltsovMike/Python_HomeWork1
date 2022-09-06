# Напишите программу, которая принимает на вход координаты двух точек 
# и находит расстояние между ними в 2D пространстве

x1 = int(input('X1 = '))
y1 = int(input('Y1 = '))
x2 = int(input('X2 = '))
y2 = int(input('Y1 = '))

import math
distance = math.sqrt(((x2-x1)**2) + ((y2 - y1)**2) )
distance = math.floor(distance*100)/100

print(f'Расстояние между точками = {distance}')