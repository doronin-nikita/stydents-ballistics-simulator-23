from tkinter import *
from tkinter.ttk import Button
from pandas import read_csv

### Загрузка констант ###
values = read_csv("values.csv") 

window = Tk() 
window.geometry(f"{5*160}x500")

def Redraw():
    current_row=0
    Label(text='Переменные и константы:').grid(row=current_row, column=0, columnspan=5)
    current_row=+1
    j = 0
    for col in values:
        text = Entry(window, width=16, bg = "#9BC2E6") 
        text.grid(row=current_row,column=j) #columnspan=j* 
        text.insert(INSERT, col) 
        text.config(state='readonly')
        j+=1
    for i in range(0,len(values['name'])):
        current_row+=1




Redraw()
#print(values['name'][0])
window.mainloop()




'''
n_rows = df.shape[0] 
n_cols = df.shape[1] 





print(f"{(n_cols+1)*160}x500")
column_names = df.columns 
i=0
Label(text="Константные параметры используемые в вычислениях:").grid(row=0, column=0, columnspan=n_cols, pady=10, padx=10)

for j, col in enumerate(column_names): 
    text = Entry(window, width=16, bg = "#9BC2E6") 
    text.grid(row=i+1,column=j) 
    text.insert(INSERT, col) 
    text.config(state='readonly')
    


# adding all the other rows into the grid 
for i in range(n_rows): 
    for j in range(n_cols): 
        text = Entry(window, width=16) 
        text.grid(row=i+2,column=j) 
        text.insert(INSERT, df.loc[i][j]) 


Button(text="Записать").grid(row=2, column=n_cols, pady=10, padx=10)
Label(text="Вектор начальной скорости:").grid(row=4, column=0, columnspan=n_cols, pady=10, padx=10)

coords = ['№','x','y','z']
startImpulseVectorBoxs = {}
for j in range(0,len(coords)):
    text = Entry(window, width=16, bg = "#9BC2E6") 
    text.grid(row=5,column=j) 
    text.insert(INSERT, coords[j]) 
    text.config(state='readonly')

    startImpulseVectorBoxs[coords[j]] = Entry(window, width=16) 
    startImpulseVectorBoxs[coords[j]].grid(row=6,column=j)

Button(text="Записать").grid(row=6, column=n_cols, pady=10, padx=10)
Label(text="Вектора ускорений:").grid(row=7, column=0, columnspan=n_cols, pady=10, padx=10)

aceleratorVectorBoxs = {}
for j in range(0,len(coords)):
    text = Entry(window, width=16, bg = "#9BC2E6") 
    text.grid(row=8,column=j) 
    text.insert(INSERT, coords[j]) 
    text.config(state='readonly')

    
for i in range(0,9):
    for j in range(0,len(coords)):
        aceleratorVectorBoxs[coords[j]] = Entry(window, width=16) 
        aceleratorVectorBoxs[coords[j]].grid(row=9+i,column=j)

Button(text="Записать все").grid(row=8, column=n_cols, pady=10, padx=10)

'''