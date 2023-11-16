"""! Модуль посвященный классам, обнавляемых через текстовые вырожения, значений
"""
from typing import Any
from pandas import read_csv
from math import sqrt, pow

class Variable():
    def __init__(self, value):
        self.expression = lambda expression_text = str(value).replace("{", "kwargs['").replace("}","']"), **kwargs:eval(expression_text)
        self.value = 0
    def __call__(self):
        return self.value
    def update(self, **kwargs):
        self.value = self.expression(**kwargs)

class VectorVariable_XYZ():
    def __init__(self, x, y, z):
        self.x_expression = lambda x_expression_text = x.replace("{", "kwargs['").replace("}","']"), **kwargs:eval(x_expression_text)
        self.y_expression = lambda y_expression_text = y.replace("{", "kwargs['").replace("}","']"), **kwargs:eval(y_expression_text)
        self.z_expression = lambda z_expression_text = z.replace("{", "kwargs['").replace("}","']"), **kwargs:eval(z_expression_text)
        self.x = 0
        self.y = 0
        self.z = 0
        self.value = sqrt(pow(self.x,2)+pow(self.y,2)+pow(self.z,2))
    def update(self, **kwargs):
        self.x = self.x_expression(**kwargs)
        self.y = self.y_expression(**kwargs)
        self.z = self.z_expression(**kwargs)
        self.value = sqrt(pow(self.x,2)+pow(self.y,2)+pow(self.z,2))

class VariablesList():
    def __init__(self):
        self.variables = {}
    def load(self, file, type_=Variable):
        data = read_csv(file)
        if (type_ is Variable):
            for name, value in zip(data['name'], data['value']):
                self.variables[name]=Variable(value=value)
    def __call__(self):
        dict_ = dict(self.variables)
        for name,value in dict_.items():
            dict_[name]=value()
        return dict_
    def update(self):
        for name, values in self.variables.items():
            values.update()


    


values = VariablesList()
values.load('values.csv')
print(values.variables)
print(values())
values.update()
print(values())
#print(values.variables)
