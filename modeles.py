'''
загрузка и обработка моделей
'''

from pyvista import read

cannon = read('untitled.obj')

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
