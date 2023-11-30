'''
физика полета снаряда
'''
from pandas import read_csv
from math import sin, cos, pi, sqrt

### ОБРАБОТКА ПОЛЕТА СНАРЯДА ###
from numpy import array as arr, append, add

def sum_vect(v1,v2):
    return tuple(i+j for i,j in zip(v1,v2))


### Графики скорости ####

from pyvista import Chart2D
graphics = {}
parametres = {}

graphics_table = read_csv("graphics.csv") 
for i in graphics_table.index:
    if graphics_table['show'][i]==0:
        graphics_table=graphics_table.drop(index=i)
for i in graphics_table.index:
   graphics[graphics_table['name'][i]]=Chart2D()
   parametres[graphics_table['name'][i]]={'x':[], 'y':[]}
   zamena = { '{''t''}':'t', '{''x''}':'x', '{''y''}':'y', '{''z''}':'z', '{''velocity''}':'sqrt(velocity[0]*velocity[0]+velocity[1]*velocity[1]+velocity[2]*velocity[2])'}
   for vl in zamena:
       if graphics_table['x'][i]==vl:
            parametres[graphics_table['name'][i]]['x_param']=zamena[vl]   
       if graphics_table['y'][i]==vl:
            parametres[graphics_table['name'][i]]['y_param']=zamena[vl]   
  
def get_coords(_data):
    variables = read_csv("values.csv") 
    base_vector = read_csv("base vector.csv")
    velocity_vector = read_csv("velocity vector.csv")
    acceleration_vectors = read_csv("acceleration vectors.csv")
    ### изменение значений ### 
    if _data is not None:
        for i in range(0, len(variables['name'])):
            if variables['name'][i] in _data:
                variables['value'][i] = _data[variables['name'][i]]
            if variables['name'][i] in ['angle', 'rotation']:
                variables['value'][i]=float(variables['value'][i])*3.14/180
    ### переменные ###
    vars = {"t": lambda **kwargs: 0}
    
    for i in range(0, len(variables['name'])):
        vars[variables['name'][i]]=lambda my_str = str(variables['value'][i]).replace("{", "kwargs['").replace("}","']"), **kwargs: eval(my_str)
    var_values = {}
    
    
    
    for name in variables['name']:
        var_values[name]=vars[name](**var_values)
     
    #print(var_values)

    result = []
    ### BASE VECTOR ###
    r_vector = []
    for v in ['x','y','z']:
        r_vector.append(eval(base_vector[v][0].replace("{", "var_values['").replace("}","']")))
    
    result.append((r_vector[0],r_vector[1],r_vector[2]))


    ### скорость ###
    r_vector = []
    for v in ['x','y','z']:
        r_vector.append(eval(velocity_vector[v][0].replace("{", "var_values['").replace("}","']")))
    velocity = (r_vector[0],r_vector[1],r_vector[2])
    ### ускорения ###
    accelerators = []
    for i in range(0,len(acceleration_vectors['name'])):
        r_vector = []
        for v in ['x','y','z']:
            r_vector.append(eval(str(acceleration_vectors[v][i]).replace("{", "var_values['").replace("}","']")))
        accelerators.append((r_vector[0],r_vector[1],r_vector[2]))
    print(accelerators)
    ### расчет точек ###
    t = 0
    for graphic in graphics:
        parametres[graphic]['x']=[]
        parametres[graphic]['y']=[]
        graphics[graphic].clear("line")
        graphics[graphic].clear("scatter")
    while (result[t][2]>=0):
        x = result[t][0]
        y = result[t][1]
        z = result[t][2]        
        result.append(sum_vect(result[t],velocity))
        for accelerator in accelerators:
            velocity=sum_vect(velocity,accelerator)
            for graphic in graphics:
                parametres[graphic]['x'].append(eval(parametres[graphic]['x_param']))
                parametres[graphic]['y'].append(eval(parametres[graphic]['y_param']))
            #velocity_t.append(t)
            #velocity_value.append(sqrt(velocity[0]*velocity[0]+velocity[1]*velocity[1]+velocity[2]*velocity[2]))
        t=t+1
        for graphic in graphics:
            _ = graphics[graphic].scatter(parametres[graphic]['x'], parametres[graphic]['y'])
            _ = graphics[graphic].line(parametres[graphic]['x'], parametres[graphic]['y'], 'r')
        #_ = velocity_chart.scatter(velocity_t,velocity_value)
        #_ = velocity_chart.line(velocity_t,velocity_value,'r')
    return result