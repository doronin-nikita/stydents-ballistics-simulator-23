'''
Отображение выстрела в графическом окне
'''

import pyvista as pv
from physic import get_coords_new as get_coords, data, velocity_chart
from modeles import *

plotter = pv.Plotter()

class myScene:
    '''
    @brief Класс отвечающий за создание интерактивной сцены пущечного выстрела
    '''
    def __init__(self, _cannon, _cannon_platform, _data):
        '''
        @brief инициализация обьекта сцены пушечного выстрела
        @param _cannon, указывает на модель дула пушки
        @param __cannon_platform, указывает на модель основания пушки
        в последствии эти модели будут задействавоны как исходники преобразованных моделей на сцене
        @param _data, копирует таблицу числовых параметров физических показателей обьектов сцены
        '''
        self.data = _data
        self.plot = pv.Plotter(shape="1|1")

        self.plot.title = 'cannon simulator'
        self.original_cannon=_cannon                                # изначальные модели дула и платформы
        self.original_cannon_platform=_cannon_platform
        self.actor_cannon = self.plot.add_mesh(self.original_cannon)
        self.actor_cannon_platform = self.plot.add_mesh(self.original_cannon_platform)

        self.bullets = []

        self.plot.subplot(1)
        self.plot.set_background('gray', all_renderers=False)
        self.plot.label="Velocity"
        self.plot.subplot(0)

        self.plot.show_grid()
        self.plot.add_camera_orientation_widget()

        self.plot.suppress_rendering = True
    
    def redraw(self, _data=None):
        '''
        @brief метод обновления моделей сцены
        @param _data - таблица параметров, которые будут обнавлены в сцене (параметры выбираются при инициализации)
        '''
        if _data is not None:
            for col in _data:
                self.data[col]=_data[col]
        
        self.plot.remove_actor(self.actor_cannon)
        self.plot.remove_actor(self.actor_cannon_platform)

        for bullet in self.bullets:
            self.plot.remove_actor(bullet)

        self.bullets = []

        for coords in get_coords(self.data):
            self.bullets.append(self.plot.add_mesh(pv.Sphere(center=coords, radius=0.3), color="red"))

        self.actor_cannon = self.plot.add_mesh(self.original_cannon.rotate_y(360-self.data['angle']).rotate_z(self.data['rotation']), color="g")
        self.actor_cannon_platform = self.plot.add_mesh(self.original_cannon_platform.rotate_z(self.data['rotation']), color="g")

        self.plot.subplot(1) 
        self.plot.add_chart(velocity_chart)  

        self.plot.subplot(0)
        self.plot.render()
        
    def show(self):
        '''
        @brief метод передающий вызов отрисовки сцены
        '''
        self.plot.show()


scene = myScene(cannon,cannon_platform,{'rotation':0, 'angle':0})
scene.redraw()

scene.plot.add_slider_widget(
        callback=lambda value: scene.redraw({'angle':value}),
        rng=[0,80],
        value=0,
        pointa=(0.1,0.1),
        pointb=(0.4,0.1),
        style="modern",
)

scene.plot.add_slider_widget(
        callback=lambda value: scene.redraw({'rotation':value}),
        rng=[0,359],
        value=0,
        pointa=(0.5,0.1),
        pointb=(0.9,0.1),
        style="modern",
)



scene.show()