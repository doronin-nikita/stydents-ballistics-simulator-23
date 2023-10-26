from tkinter import Tk, Frame, BOTH, Canvas, BOTTOM, LEFT, VERTICAL, RIGHT, ALL, X, Y, Label, Entry, INSERT
from tkinter.ttk import Button, Scrollbar
root = Tk()
root.title('REDACTOR')
root.geometry("900x400")
main_frame = Frame(root)
main_frame.pack(fill=BOTH,expand=1)
sec = Frame(main_frame)
sec.pack(fill=X,side=BOTTOM)
my_canvas = Canvas(main_frame)
my_canvas.pack(side=LEFT,fill=BOTH,expand=1)
y_scrollbar = Scrollbar(main_frame,orient=VERTICAL,command=my_canvas.yview)
y_scrollbar.pack(side=RIGHT,fill=Y)
my_canvas.configure(yscrollcommand=y_scrollbar.set)
my_canvas.bind("<Configure>",lambda e: my_canvas.config(scrollregion= my_canvas.bbox(ALL)))
second_frame = Frame(my_canvas)
my_canvas.create_window((0,0),window= second_frame, anchor="nw")

from pandas import read_csv, concat, DataFrame

### Загрузка констант ###
values = read_csv("values.csv") 
base_vector = read_csv("base vector.csv")

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
    for child in second_frame.winfo_children():
        child.destroy()
    current_row=0
    Label(text='Переменные и константы:').grid(row=current_row, column=0, columnspan=5, in_=second_frame)
    current_row=+1
    
    text = Entry(root, width=16, bg = "#9BC2E6") 
    text.grid(row=current_row,column=0, in_=second_frame) #columnspan=j* 
    text.insert(INSERT, 'name') 
    text.config(state='readonly')

    text = Entry(root, width=16*4, bg = "#9BC2E6") 
    text.grid(row=current_row,column=1, columnspan=4, in_=second_frame) #columnspan=j* 
    text.insert(INSERT, 'value') 
    text.config(state='readonly')

    for i in range(0,len(values['name'])):
        current_row+=1
        btn = Button(text=values['name'][i], width=16, command=lambda text="{"+values['name'][i]+"}": insert_name(text))
        btn.grid(row=current_row, column=0, in_=second_frame)

        text = Entry(root, width=16*4) 
        text.grid(row=current_row,column=1,columnspan=4, in_=second_frame)
        text.insert(INSERT, values['value'][i]) 
        text.bind("<1>", lambda e, col_index=i,  text=text: entry_click(col_index, text, e))
    
    current_row+=1
    new_value_name = Entry(root, width=16) 
    new_value_name.grid(row=current_row,column=0, in_=second_frame) 
    new_value_name.insert(INSERT, 'new') 
    new_value_value = Entry(root, width=16*4) 
    new_value_value.grid(row=current_row,column=1, columnspan=4, in_=second_frame) 
    new_value_value.insert(INSERT, '') 
    new_value_value.bind("<1>", lambda e, text= new_value_value: entry_click(None, text, e))
    global new_value_add_btn
    new_value_add_btn= Button(text='add', width=15, command=lambda: add_value(name=new_value_name.get(), value=new_value_value.get()))
    new_value_add_btn.grid(row=current_row, column=5, in_=second_frame)
    
    current_row+=1
    Button(text='save',  width=15*5, command=save_values).grid(row=current_row, column=0, columnspan=5, in_=second_frame)
    
    current_row+=1
    Label(text='-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-').grid(row=current_row, column=0, columnspan=6, in_=second_frame)
    
    current_row+=1
    Label(text='начальная точка {x0, y0, z0}').grid(row=current_row, column=0, columnspan=5, in_=second_frame)
    current_row+=1

    current_column = 1
    for v in {'x', 'y', 'z'}:
        text = Entry(root, width=20, bg = "#9BC2E6")
        text.grid(row=current_row,column=current_column, in_=second_frame) #columnspan=j*
        text.insert(INSERT, v)
        text.config(state='readonly')
        current_column+=1

    for i in range(0,len(base_vector['name'])):
        current_row+=1
        btn = Button(text=base_vector['name'][i], width=16, command=lambda text="{"+base_vector['name'][i]+"}": insert_name(text))
        btn.grid(row=current_row, column=0, in_=second_frame)

        current_column=1
        for v in {'x', 'y', 'z'}:
            text = Entry(root, width=20) 
            text.grid(row=current_row,column=current_column, in_=second_frame)
            text.insert(INSERT, base_vector[v][i]) 
            text.bind("<1>", lambda e, col_index=i,  text=text: entry_click(col_index, text, e))
            current_column+=1
    current_row+=1
    Button(text='save',  width=15*5, command=lambda table=base_vector, file="base vector.csv":table.to_csv(file, index=False)).grid(row=current_row, column=0, columnspan=5, in_=second_frame)

    current_row+=1
    Label(text='вектора скорости').grid(row=current_row, column=0, columnspan=5, in_=second_frame)

    current_row+=1
    Label(text='вектора ускорений').grid(row=current_row, column=0, columnspan=5, in_=second_frame)
    for i in range(0,100):
        current_row+=1
        Button(text='save',  width=15*5, command=save_values).grid(row=current_row, column=0, columnspan=5, in_=second_frame)

    

Redraw()

root.mainloop()
