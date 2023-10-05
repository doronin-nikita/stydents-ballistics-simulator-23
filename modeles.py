'''
загрузка и обработка моделей
'''

from pyvista import read        #, read_texture

cannon = read('gun.obj').rotate_z(180)
#tex=read_texture('gun.mtl')
cannon_platform = read('base.obj').rotate_z(180)