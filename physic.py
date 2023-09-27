'''
физика полета снаряда
'''
from pandas import read_csv

data = read_csv('data.csv')
print(data)

from math import sin

def get_cords(i):
    return (i,0,5*sin(i/5))