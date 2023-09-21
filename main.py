'''
Отображение выстрела в графическом окне
'''

import pyvista as pv
from physic import get_cords, data
from modeles import *

objs = []
for i in range(0,16):
    objs.append(pv.Sphere(center=get_cords(i),radius=0.1))

red_sphere = pv.Sphere(center=get_cords(0),radius=0.11)

eng = MyCustomRoutine(red_sphere)



plotter = pv.Plotter()

plotter.add_mesh(cannon.rotate_y(data["angle"][0]))
plotter.add_mesh(cannon_platform)

for i in range(0,16):
    plotter.add_mesh(objs[i], color='gray')
plotter.add_mesh(red_sphere, color='red')
plotter.add_slider_widget(
    callback=lambda value: eng('center',get_cords(value)) ,
    rng=[0,16],
    value=0,
    pointa=(0.1,0.1),
    pointb=(0.9,0.1),
    style="modern",
)
plotter.show_grid()
plotter.show()