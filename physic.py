'''
физика полета снаряда
'''
from pandas import read_csv

data = read_csv('data.csv')

from math import sin, cos, pi

### ОБРАБОТКА ПОЛЕТА СНАРЯДА ###
from numpy import array as arr, append, add

def sum_vect(v1,v2):
    return tuple(i+j for i,j in zip(v1,v2))


def get_coords(_data):
    '''
    @brief Функция для генерации точек через которые пролетает снаряд
    @param angle - угл подьема пушки по оси z вверх 180>angle>0 -> z>0
    '''
    l = 12.6                                        # длинна дула
    a = _data['angle']*pi/180                       # угол в радианах (Подьем дула)
    b = _data['rotation']*pi/180

    velocity = (float(_data['impulse'])*cos(a)*cos(b)+0.0, float(_data['impulse'])*sin(b)*cos(a)+0.0, float(_data['impulse'])*sin(a)+0.0)    # вектор движения
    gravity=(0,0,-9.8*_data['mass'])                # вектор ускорения по гровитации

    accelerations = [gravity]                       # список ускорений

    
    result = [(l*cos(a)*cos(b)+0.0, l*sin(b)*cos(a)+0.0, l*sin(a)+0.0)]                      # стартовая точка
    
    i = 0
    while (result[i][2]>=0):
        result.append(sum_vect(result[i],velocity))
        for accelerator in accelerations:
            velocity=sum_vect(velocity,accelerator)
        i=i+1
    return result
