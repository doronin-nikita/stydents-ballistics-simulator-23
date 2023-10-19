from tkinter import *
from tkinter.ttk import Button
from pandas import read_csv, concat, DataFrame

### Загрузка констант ###
values = read_csv("values.csv") 
base_vector = read_csv("base vector.csv")

window = Tk() 
window.geometry(f"{5*180}x500")

def add_value(name, value):
    global values
    values.loc[len(values.index)] =  [name, value]
    new_value_add_btn.destroy()
    entry_click()
    Redraw()
    print(values)

ActiveEntry = None
ActiveColumn= None

def entry_click(col_index=None, clickedEntry=None, event=None):
    global ActiveEntry
    global ActiveColumn
    if (ActiveColumn is not None):
        values['value'][ActiveColumn]=ActiveEntry.get()
    
    ActiveColumn = col_index
    if (clickedEntry is not None):
        ActiveEntry = clickedEntry

def insert_name(text):
    global ActiveEntry
    ActiveEntry.insert(INSERT, text) 

def save_values():
    values.to_csv('values.csv', index=False)

def Redraw():
    global ActiveEntry

    current_row=0
    Label(text='Переменные и константы:').grid(row=current_row, column=0, columnspan=5)
    current_row=+1
    
    text = Entry(window, width=16, bg = "#9BC2E6") 
    text.grid(row=current_row,column=0) #columnspan=j* 
    text.insert(INSERT, 'name') 
    text.config(state='readonly')

    text = Entry(window, width=16*4, bg = "#9BC2E6") 
    text.grid(row=current_row,column=1, columnspan=4) #columnspan=j* 
    text.insert(INSERT, 'value') 
    text.config(state='readonly')

    for i in range(0,len(values['name'])):
        current_row+=1
        btn = Button(text=values['name'][i], width=16, command=lambda text="{"+values['name'][i]+"}": insert_name(text))
        btn.grid(row=current_row, column=0)

        text = Entry(window, width=16*4) 
        text.grid(row=current_row,column=1,columnspan=4)
        text.insert(INSERT, values['value'][i]) 
        text.bind("<1>", lambda e, col_index=i,  text=text: entry_click(col_index, text, e))
    
    current_row+=1
    new_value_name = Entry(window, width=16) 
    new_value_name.grid(row=current_row,column=0) 
    new_value_name.insert(INSERT, 'new') 
    new_value_value = Entry(window, width=16*4) 
    new_value_value.grid(row=current_row,column=1, columnspan=4) 
    new_value_value.insert(INSERT, '') 
    new_value_value.bind("<1>", lambda e, text= new_value_value: entry_click(None, text, e))
    global new_value_add_btn
    new_value_add_btn= Button(text='add', width=15, command=lambda: add_value(name=new_value_name.get(), value=new_value_value.get()))
    new_value_add_btn.grid(row=current_row, column=5)
    
    current_row+=1
    Button(text='save',  width=15*5, command=save_values).grid(row=current_row, column=0, columnspan=5)

    current_row+=1
    Label(text='x0, y0, z0').grid(row=current_row, column=0, columnspan=5)
    
    current_row+=1
    Label(text='вектора скорости').grid(row=current_row, column=0, columnspan=5)

    current_row+=1
    Label(text='вектора ускорений').grid(row=current_row, column=0, columnspan=5)
    for i in range(0,100):
        current_row+=1
        Button(text='save',  width=15*5, command=save_values).grid(row=current_row, column=0, columnspan=5)

    

Redraw()
window.mainloop()