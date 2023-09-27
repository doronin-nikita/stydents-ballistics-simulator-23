'''
физика полета снаряда
'''
from pandas import read_csv

data = read_csv('data.csv')

from math import sin, cos

### ОБРАБОТКА ПОЛЕТА СНАРЯДА ###
from numpy import array as arr, append, add




def get_coords(angle,rotation,impuls,mass):
    '''
    @brief Функция для генерации точек через которые пролетает снаряд
    @param angle - угл подьема пушки по оси z вверх 180>angle>0 -> z>0

    '''

    velocity = [float(impuls),0.0,0.3]   # вектор движения
    gravity = [0.0,0.0,0.0]    # вектор ускорения по гровитации

    accelerations = [gravity]       # список ускорений

    result = [[0.0, 0.0, 0.0]]
    gravity=[0,0,-9.8*mass]
    for i in range(0,100):
        result.append([x+y for x, y in zip(result[i], velocity)])
        #for a in accelerations:
        velocity=[x+y for x, y in zip(result[i], gravity)]
    return result
