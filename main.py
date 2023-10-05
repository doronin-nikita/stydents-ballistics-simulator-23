'''
Отображение выстрела в графическом окне
'''

import pyvista as pv
from physic import get_coords, data
from modeles import *

plotter = pv.Plotter()

class myScene:
    def __init__(self, _cannon, _cannon_platform, _data):
        self.data = _data
        self.plot = pv.Plotter()
        self.original_cannon=_cannon
        self.original_cannon_platform=_cannon_platform
        self.actor_cannon = self.plot.add_mesh(self.original_cannon)
        self.actor_cannon_platform = self.plot.add_mesh(self.original_cannon_platform)
    def redraw(self, _data):
        for col in _data:
            self.data[col]=_data[col]
        self.plot.remove_actor(self.actor_cannon)
        self.plot.remove_actor(self.actor_cannon_platform)
        self.actor_cannon = self.plot.add_mesh(self.original_cannon.rotate_y(self.data['angle']).rotate_z(self.data['rotation']))
        self.actor_cannon_platform = self.plot.add_mesh(self.original_cannon_platform.rotate_z(self.data['rotation']))
    def show(self):
        self.plot.show()

    def add_slider_widget(self,_callback, _rng, _value, _pointa, _pointb, _style):
        self.plot.add_slider_widget(callback=_callback, rng=_rng, value=_value, pointa=_pointa, pointb=_pointb, style=_style)


scene = myScene(cannon,cannon_platform,{'angle':0,'rotation':0})
scene.redraw({'angle':0,'rotation':0})

scene.add_slider_widget(
        _callback=lambda value: scene.redraw({'angle':value}),
        _rng=[0,80],
        _value=0,
        _pointa=(0.1,0.1),
        _pointb=(0.4,0.1),
        _style="modern",
)

scene.add_slider_widget(
        _callback=lambda value: scene.redraw({'rotation':value}),
        _rng=[0,80],
        _value=0,
        _pointa=(0.5,0.1),
        _pointb=(0.9,0.1),
        _style="modern",
)

scene.show()


'''
# OLD VERSION CODE
def draw(angle,rotation,impuls,mass,t):
   
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
    
    plotter.meshes.clear()
    print(plotter.meshes[0])

    print(type(plotter))
    plotter.show()    
    


draw(data['angle'][0],data['rotation'][0]+180,data['impulse'][0],data['m'][0],0)
'''
