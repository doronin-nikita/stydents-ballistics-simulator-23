'''
загрузка и обработка моделей
'''

from pyvista import read

cannon = read('gun.obj')
cannon_platform = read('base.obj')

from pyvista import Sphere
class MyCustomRoutine:
    def __init__(self, mesh):
        self.output = mesh
        self.kwargs = {
            'radius': 0.3,
            'theta_resolution': 30,
            'phi_resolution': 30,
        }
        self.dkwargs = {
            'rotate_y': 0,
        }

    def __call__(self, param, value):
        if (param in self.dkwargs):
            self.dkwargs[param] = value
        else:
            self.kwargs[param] = value
        self.update()

    def update(self):
        result = Sphere(**self.kwargs).rotate_y(self.dkwargs['rotate_y'])
        self.output.overwrite(result)
        return
