import numpy as np
import pyvista as pv
from pyvista import examples
dem = examples.download_crater_topo()
dem = dem.extract_subset((40,900,40,900,0,0), (1,1,1))
terrain = dem.warp_by_scalar()
#terrain.plot()

pt = pv.Plotter(shape="1|1")
pt.show_grid()
pt.add_mesh(terrain)
pt.show()
