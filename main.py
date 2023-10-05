'''
Отображение выстрела в графическом окне
'''

import pyvista as pv
from physic import get_coords, data
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
        self.plot = pv.Plotter()
        self.plot.title = 'cannon simulator'
        self.original_cannon=_cannon
        self.original_cannon_platform=_cannon_platform
        self.actor_cannon = self.plot.add_mesh(self.original_cannon)
        self.actor_cannon_platform = self.plot.add_mesh(self.original_cannon_platform)

        self.plot.show_grid()
        self.plot.add_camera_orientation_widget()
    
    def redraw(self, _data=None):
        '''
        @brief метод обновления моделей сцены
        @param _data - таблица параметров, которые будут обнавлены в сцене
        '''
        if _data is not None:
            for col in _data:
                self.data[col]=_data[col]
        self.plot.remove_actor(self.actor_cannon)
        self.plot.remove_actor(self.actor_cannon_platform)
        self.actor_cannon = self.plot.add_mesh(self.original_cannon.rotate_y(self.data['angle']).rotate_z(self.data['rotation']))
        self.actor_cannon_platform = self.plot.add_mesh(self.original_cannon_platform.rotate_z(self.data['rotation']))


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