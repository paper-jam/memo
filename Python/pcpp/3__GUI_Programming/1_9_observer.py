import tkinter as tk

def r_observer(*args):
    print("Reading")


def w_observer(*args):
    print("Writing")

dummy = tk.Tk()    # we need this although we won't display any windows
variable = tk.StringVar()
variable.set("abc")
r_obsid = variable.trace("r", r_observer)
w_obsid = variable.trace("w", w_observer)

variable.set(variable.get() + 'd')  # read followed by write

variable.trace_vdelete("r", r_obsid)    # removing reader observer
variable.set(variable.get() + 'e')      # read followed by write but only write observer is active 
variable.trace_vdelete("w", w_obsid)    # removing writer observer
variable.set(variable.get() + 'f')      # read followed by write but neither write or read observer
print(variable.get())
