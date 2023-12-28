'''
Отображение выстрела в графическом окне
'''

import pyvista as pv
from physic_2 import get_coords, graphics
from modeles import *
import platform
 
map_img =  pv.examples.download_crater_topo()
mp2 = pv.examples.load_random_hills()
show_map = False
def toggle_map_view():
    global show_map
    show_map=not(show_map)

rendering = platform.system()=="Linux"

plotter = pv.Plotter()

class myScene:
    '''!
    @brief Класс отвечающий за создание интерактивной сцены пущечного выстрела
    '''
    def __init__(self, _cannon, _cannon_platform, _data):
        '''!
        @brief инициализация обьекта сцены пушечного выстрела
        @param _cannon, указывает на модель дула пушки
        @param __cannon_platform, указывает на модель основания пушки
        в последствии эти модели будут задействавоны как исходники преобразованных моделей на сцене
        @param _data, копирует таблицу числовых параметров физических показателей обьектов сцены
        '''
        self.data = _data
        self.plot = pv.Plotter(shape=f"1|{len(graphics)}")

        self.plot.title = 'cannon simulator'
        self.plot.add_text('balistic simulator')
        self.original_cannon=_cannon                                # изначальные модели дула и платформы
        self.original_cannon_platform=_cannon_platform
        self.actor_cannon = self.plot.add_mesh(self.original_cannon)
        self.actor_cannon_platform = self.plot.add_mesh(self.original_cannon_platform)
        if show_map:
            n_mp = map_img.extract_subset((40,50,40,50,0,0), (1,1,1))
            terrain = n_mp.warp_by_scalar()
            self.terrain = self.plot.add_mesh(mesh=terrain)
        else:
            self.terrain = None
        
        self.bullets = []
        i = 1
        for graphic in graphics:
            self.plot.subplot(i)
            self.plot.set_background('gray', all_renderers=False)
            self.plot.add_text(graphic)
            i+=1
        self.plot.subplot(0)

        self.plot.show_grid()
        self.plot.add_camera_orientation_widget()
        if rendering:
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

        if show_map:
            self.plot.remove_actor(self.terrain)
            self.terrain = self.plot.add_mesh(mp2)
            print(mp2)
        self.bullets = []

        for coords in get_coords(self.data):

            self.bullets.append(self.plot.add_mesh(pv.Sphere(center=(coords[0], coords[1], coords[2]+1.5), radius=0.3), color="red"))

        self.actor_cannon = self.plot.add_mesh(self.original_cannon.rotate_y(360-self.data['angle']).rotate_z(self.data['rotation']), color="g")
        self.actor_cannon_platform = self.plot.add_mesh(self.original_cannon_platform.rotate_z(self.data['rotation']), color="g")

        

        i = 0
        for graphic in graphics:
            i+=1
            self.plot.subplot(i) 
            self.plot.add_chart(graphics[graphic])

        self.plot.subplot(0)
        if rendering:
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

scene.plot.add_checkbox_button_widget(lambda v: (toggle_map_view(), scene.redraw()), value=False)
#scene.plot.add_floor()


scene.show()