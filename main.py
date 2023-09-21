import pyvista as pv
from math import sin

def get_cords(i):
    return (i,0,5*sin(i/5))

objs = []
for i in range(0,16):
    objs.append(pv.Sphere(center=get_cords(i),radius=0.1))

block1 = pv.Cube(center=(0,0,0), x_length=1, y_length=0.2, z_length=0.2).rotate_y(-45, inplace=False)

plotter = pv.Plotter()
plotter.add_mesh(block1, color='blue')
for i in range(0,16):
    plotter.add_mesh(objs[i], color='red')
plotter.show_grid()
plotter.show()