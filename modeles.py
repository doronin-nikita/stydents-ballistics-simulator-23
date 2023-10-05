'''
загрузка и обработка моделей
'''

from pyvista import read        #, read_texture

cannon = read('gun.obj')
#tex=read_texture('gun.mtl')
cannon_platform = read('base.obj')

def update(mesh, angle, p):
    mesh.overwrite(mesh.rotate_y(angle))
    #p.update()

from pyvista import Sphere
class MyCustomRoutine:
    def __init__(self, mesh):
        self.output = mesh
        self.kwargs = {
            'radius': 0.3,
            'theta_resolution': 30,
            'phi_resolution': 30,
        }

    def __call__(self, param, value):
        self.kwargs[param] = value
        self.update()

    def update(self):
        result = Sphere(**self.kwargs)
        self.output.overwrite(result)
        return
    
class MyCustomRoutine2:
    def __init__(self, mesh):
        self.output = mesh

    def updates(self, angle):
        result = cannon.rotate_y(angle)
        self.output.overwrite(result)
        return