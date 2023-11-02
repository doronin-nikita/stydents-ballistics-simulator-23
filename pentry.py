from tkinter import Entry, Tk
from tkinter.ttk import Button
from ctypes import c_wchar_p, pointer

class PEntry(Entry):
    def __init__(self, ptr, **kwargs):
        self.ptr = ptr
        super().__init__(**kwargs)
        self.bind("<Key>",func=self.update)
    def update(self, event):
        self.ptr.contents.value = self.get()+event.char

root = Tk()

variable = c_wchar_p("eeee")
ptr = pointer(variable)
print(ptr.contents)
PEntry(ptr=ptr).pack()

ptr.contents.value="1111"
print(id(variable))
Button(text='var', command=lambda: print("v:",variable.value)).pack()
root.mainloop()