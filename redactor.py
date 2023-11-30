from tkinter import Tk, Frame, BOTH, Canvas, BOTTOM, LEFT, VERTICAL, RIGHT, ALL, X, Y, Label, Entry, INSERT, StringVar
from tkinter.ttk import Button, Scrollbar
from pandas import read_csv, concat, DataFrame

root = Tk()
root.title('REDACTOR')
root.geometry("900x700")
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

### Загрузка констант ###
tables = {}
tables['values'] = read_csv("values.csv") 
tables['base_vector'] = read_csv("base vector.csv")
tables['velocity_vector'] = read_csv("velocity vector.csv")
tables['acceleration_vectors'] = read_csv("acceleration vectors.csv")
tables['graphics'] = read_csv("graphics.csv")

coord_names = ['x','y','z']

active_entry = None

def select_entry(entry, event):
    global active_entry
    active_entry = entry
def update_table(table, value, row, entry, event):
    select_entry(entry, event)
    tables[table][value][row] = entry.get()+event.char

def add_row(table, row):
    tables[table].loc[len(tables[table].index)] =  row

def redraw():
    global active_entry
    for child in second_frame.winfo_children():
        child.destroy()
    current_row = 0
    Label(second_frame, text='Переменные и константы:').grid(row=current_row, column=0, columnspan=5, in_=second_frame)
    current_row+=1
    Entry(second_frame,  background="#9BC2E6", width=16, textvariable=StringVar(value="name"),cnf={'state':'readonly'}).grid(row=current_row,column=0, in_=second_frame)
    Entry(second_frame,  background="#9BC2E6", width=64, textvariable=StringVar(value="value"),cnf={'state':'readonly'}).grid(row=current_row,column=1, columnspan=4, in_=second_frame)
    current_row+=1    
    Button(second_frame, text="t", width=16, command=lambda bt_name="{""t""}": active_entry.insert(INSERT, bt_name) if (active_entry is not None) else print("select entry")).grid(row=current_row, column=0, in_=second_frame)
    Entry(second_frame, width=64, textvariable=StringVar(value="t+1"),cnf={'state':'readonly'}).grid(row=current_row,column=1, columnspan=4, in_=second_frame)
    current_row+=1    
    for i in range(0,len(tables['values']['name'])):
        Button(second_frame, text=tables['values']['name'][i], width=16, command=lambda bt_name="{"+tables['values']['name'][i]+"}": active_entry.insert(INSERT, bt_name) if (active_entry is not None) else print("select entry")).grid(row=current_row, column=0, in_=second_frame)
        ent = Entry(second_frame, width=64, textvariable=StringVar(value=tables['values']['value'][i]))
        ent.grid(row=current_row,column=1, columnspan=4, in_=second_frame)
        ent.bind("<Key>",func=lambda ev, en=ent,tb='values', vl='value', rw=i:update_table(table=tb, value=vl, row=rw, entry=en, event=ev))
        ent.bind("<1>", func=lambda ev, en=ent: select_entry(entry=en, event=ev))
        current_row+=1
    
    new_variable = Entry(second_frame, width=16, textvariable=StringVar(value="new"))
    new_variable.grid(row=current_row, column=0, in_=second_frame)
    new_variable_value = Entry(second_frame, width=64)
    new_variable_value.grid(row=current_row, column=1,columnspan=4, in_=second_frame)
    new_variable_value.bind("<1>", func=lambda ev, en=new_variable_value: select_entry(entry=en, event=ev))
    Button(second_frame,text="add", command=lambda table="values", nv_name=new_variable, nv_value=new_variable_value: (add_row(table=table, row=[nv_name.get(), nv_value.get()]), redraw())).grid(row=current_row, column=5,in_=second_frame)
    current_row+=1
    Button(second_frame, text='save', width=80, command=lambda tbl='values', file='values.csv': tables[tbl].to_csv(file, index=False)).grid(row=current_row, column=0, columnspan=5, in_=second_frame)
    current_row+=1
    Label(second_frame, text='Начальная точка (вершина дула):').grid(row=current_row, column=0, columnspan=5, in_=second_frame)
    current_row+=1
    for i in range(0,len(coord_names)):
        Entry(second_frame,  background="#9BC2E6", width=20, textvariable=StringVar(value=coord_names[i]),cnf={'state':'readonly'}).grid(row=current_row,column=i+1, in_=second_frame)
        ent = Entry(second_frame, width=20, textvariable=StringVar(value=tables['base_vector'][coord_names[i]][0]))
        ent.grid(row=current_row+1,column=i+1, in_=second_frame)
        ent.bind("<Key>",func=lambda ev, en=ent,tb='base_vector', vl=coord_names[i], rw=0:update_table(table=tb, value=vl, row=rw, entry=en, event=ev))
        ent.bind("<1>", func=lambda ev, en=ent: select_entry(entry=en, event=ev))
    current_row+=1
    Entry(second_frame,  background="#9BC2E6", width=20, textvariable=StringVar(value=tables['base_vector']['name'][0]),cnf={'state':'readonly'}).grid(row=current_row,column=0, in_=second_frame)
    Button(second_frame, text='save', command=lambda tbl='base_vector', file='base vector.csv': tables[tbl].to_csv(file, index=False)).grid(row=current_row, column=5, in_=second_frame)
    current_row+=1
    
    Label(second_frame, text='Вектор скорости:').grid(row=current_row, column=0, columnspan=5, in_=second_frame)
    current_row+=1
    for i in range(0,len(coord_names)):
        Entry(second_frame,  background="#9BC2E6", width=20, textvariable=StringVar(value=coord_names[i]),cnf={'state':'readonly'}).grid(row=current_row,column=i+1, in_=second_frame)
        ent = Entry(second_frame, width=20, textvariable=StringVar(value=tables['velocity_vector'][coord_names[i]][0]))
        ent.grid(row=current_row+1,column=i+1, in_=second_frame)
        ent.bind("<Key>",func=lambda ev, en=ent,tb='velocity_vector', vl=coord_names[i], rw=0:update_table(table=tb, value=vl, row=rw, entry=en, event=ev))
        ent.bind("<1>", func=lambda ev, en=ent: select_entry(entry=en, event=ev))
    current_row+=1
    Entry(second_frame,  background="#9BC2E6", width=20, textvariable=StringVar(value=tables['velocity_vector']['name'][0]),cnf={'state':'readonly'}).grid(row=current_row,column=0, in_=second_frame)
    Button(second_frame, text='save', command=lambda tbl='velocity_vector', file='velocity vector.csv': tables[tbl].to_csv(file, index=False)).grid(row=current_row, column=5, in_=second_frame)
    current_row+=1
    
    Label(second_frame, text='Вектора ускорений:').grid(row=current_row, column=0, columnspan=5, in_=second_frame)
    current_row+=1
    for i in range(0,len(coord_names)):
        Entry(second_frame,  background="#9BC2E6", width=20, textvariable=StringVar(value=coord_names[i]),cnf={'state':'readonly'}).grid(row=current_row,column=i+1, in_=second_frame)
        for k in range(0,len(tables['acceleration_vectors']['name'])):
            ent = Entry(second_frame, width=20, textvariable=StringVar(value=tables['acceleration_vectors'][coord_names[i]][k]))
            ent.grid(row=current_row+1+k,column=i+1, in_=second_frame)
            ent.bind("<Key>",func=lambda ev, en=ent,tb='acceleration_vectors', vl=coord_names[i], rw=k:update_table(table=tb, value=vl, row=rw, entry=en, event=ev))
            ent.bind("<1>", func=lambda ev, en=ent: select_entry(entry=en, event=ev))
    current_row+=1
    for k in range(0,len(tables['acceleration_vectors']['name'])):
        Entry(second_frame,  background="#9BC2E6", width=20, textvariable=StringVar(value=tables['acceleration_vectors']['name'][k]),cnf={'state':'readonly'}).grid(row=current_row,column=0, in_=second_frame)
        current_row+=1
    Button(second_frame, text='save', width=30, command=lambda tbl='acceleration_vectors', file='acceleration vectors.csv': tables[tbl].to_csv(file, index=False)).grid(row=current_row, column=3, columnspan=3, in_=second_frame)
    new_variable = Entry(second_frame, width=20, textvariable=StringVar(value="new"))
    new_variable.grid(row=current_row, column=0, in_=second_frame)
    Button(second_frame,text="add", width=20, command=lambda table='acceleration_vectors', nv_name=new_variable, nv_value=None: (add_row(table=table, row=[nv_name.get(), 0,0,0]), redraw())).grid(row=current_row, column=1,in_=second_frame)
    current_row+=1
    
    Label(second_frame, text='Вывод графиков:').grid(row=current_row, column=0, columnspan=5, in_=second_frame)
    current_row+=1
    Entry(second_frame,  background="#9BC2E6", width=20, textvariable=StringVar(value="name"),cnf={'state':'readonly'}).grid(row=current_row,column=0, in_=second_frame)
    Entry(second_frame,  background="#9BC2E6", width=20, textvariable=StringVar(value="visible"),cnf={'state':'readonly'}).grid(row=current_row,column=1, in_=second_frame)
    Entry(second_frame,  background="#9BC2E6", width=40, textvariable=StringVar(value="values x:y"),cnf={'state':'readonly'}).grid(row=current_row,column=2, columnspan=2, in_=second_frame)
    current_row+=1    

redraw()

root.mainloop()
