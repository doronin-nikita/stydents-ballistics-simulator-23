'''
Отображение выстрела в графическом окне
'''

import pyvista as pv
from physic import get_coords, data
from modeles import *

plotter = pv.Plotter()

def draw(angle,rotation,impuls,mass,t):
    '''
    @brief метод отвечающий за перерисовку
    '''
    plotter.clear()
    plotter.add_mesh(cannon.rotate_y(angle).rotate_z(rotation))
    plotter.add_mesh(cannon_platform.rotate_z(rotation))
    coords = get_coords(angle,rotation,impuls,mass)
    red_sphere = pv.Sphere(center=coords[0],radius=0.11)
    eng = MyCustomRoutine(red_sphere)

    for i in range(0,15):
        plotter.add_mesh(pv.Sphere(center=coords[i],radius=0.1), color='gray')
    plotter.add_mesh(red_sphere, color='red')
    plotter.add_slider_widget(
        callback=lambda value: eng('center',(coords[int(value)])) ,
        rng=[0,100],
        value=0,
        pointa=(0.05,0.9),
        pointb=(0.05,0.2),
        style="modern",
    )
    plotter.add_slider_widget(
        callback=lambda value: update(cannon,value,plotter),
        rng=[0,100],
        value=0,
        pointa=(0.1,0.1),
        pointb=(0.4,0.1),
        style="modern",
    )
    plotter.show_grid()
    plotter.add_camera_orientation_widget()
    plotter.show()    
    


draw(data['angle'][0],data['rotation'][0]+180,data['impulse'][0],data['m'][0],0)

