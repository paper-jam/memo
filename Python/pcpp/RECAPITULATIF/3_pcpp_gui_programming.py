#  --------------- 3 - GUI programming ----------
# pylint: skip-file

# ---------------- Module 1

# -- history
# two classical terminals : IBM 3270,  VT100 / 80*25 
# very expensive models could be equipped with a light pen.
# in a 

# -- GUI -> visual programming -> creation of a window with controls widgets, focusable
# widgets introduces a new paradigm for coding user interaction and relations between widgets
# => event-driven programming (EDP). 

# -- Tk
# Unix world -> GTK and Qt
# Tk is widget toolkit / GUI toolkit / UX library. -> portable
# free, open, since 1991, define more than 30 universal widgets
# implementation is available for many programming languages
# Tk for Python -> tkInter (tk interface)

# -- tkInter
# pronounce T-K-inter 
# contains  functions, constants, classes, objects, and modules for GUI app
# EDP : event driven programmong
import tkinter
from tkinter import Widget, messagebox


def Click():
    replay = messagebox.askquestion("Quit?", "Are you sure?")
    if replay == 'yes':
        skylight.destroy();


skylight = tkinter.Tk()
skylight.title("Skylight")
button = tkinter.Button(skylight, text="Bye!", command=Click)
button.place(x=10, y=10)
skylight.mainloop()

#  main loop => no direct control over the code's execution
# callback can be bound with more than one widget
# modal window – a window which grabs the whole of the application's focus

# -- geometry managers
# three different methods, are EXCLUSIVE, only one by app
# "Place" : the more detailed, need to precisely declare a widget's location
# "grid" : express your general wishes and tries to deploy the widgets according to them.
# "Pack" : the least accurate of the three

# -- place() 
# 4 parameters :
#       - Height, Width : optional
#       - x, y (x : pixels from left side  : y ... from top side)



# -- grid() 
# 4 parameters : column (start at 0), row(start at 0), columspan(defaut1), rowspan(defaut1)

# -- pack 
# order in which the widgets are packed matters
# use it only as a temporary solution as results as surprising
# pack(side=TOP/BOTTOM/LEFT/RIGHT   fill=NONE/X/Y/BOTH)
# side : force the widget in a specified direction
# fill : forec the widged to expand in direction
import tkinter as tk
window = tk.Tk()
button_1 = tk.Button(window, text="Button #1")
button_1.pack(side=tk.RIGHT, fill=tk.Y)

# -- adding colors - at least three method
# 750 predefined color
# RGB -> 16,777,216 colors (Red, Green, Blue)
#  0,0,0 -> black  255,255,255 -> white 
#  hexa  -> black #000000 white -> #FFFFFF
button = tk.Button(window, text="Button #1", bg="red", fg="yellow")


#  Frame is another non-clickable component used to group widgets

# IntVar class are used by tkinter to organize internal communication between different widgets
switch = tk.IntVar()
switch.set(1)

# creates a bidirectional link between the switch variable and the widget
# switch = 1 => the checkbox is cheked
checkbutton = tk.Checkbutton(window, text="Check Button", variable=switch)

# and with radio button
radiobutton_1 = tk.Radiobutton(window, text="Steak", variable=switch, value=0)
radiobutton_2 = tk.Radiobutton(window, text="Salad", variable=switch, value=1)

# messagebox
messagebox.showinfo("info", "someinfo")

# events 
# an event is an object carrying some useful info about what actually happens 
# when the event has been induced (by the user or by another factor).
# each event has its own name and the name is just a unified string.

# binding an event to a widget
# widget.bind(event, callback)

# ---------------- event
# mouse :
<Button-1> <Button-2> <Button-3>
<ButtonRelease-1> <ButtonRelease-2> <ButtonRelease-3> <DoubleButton-1>
<Enter>   Mouse cursor appears over the widget
<Leave>   Mouse cursor leaves the widget area

<Focus-In>  The widget gains the focus
<Focus-Out> The widget loses the focus

<Return>    The user presses the Enter/Return key
<Key>       The user presses any key

x           The user presses x key (x can be neither a space nor the < key)
<space>     The user presses the spacebar
<less>      The user presses the < key
<Cancel>    The user presses the key/keys used by the current OS to stop the program (e.g., Ctrl-C or Ctrl-Break)
<BackSpace> The user presses the Backspace key
<Tab>       The user presses Tab key

<Shift_L>   The user presses one of the Shift keys
<Control_L> The user presses one of the Control keys
<Alt_L>     The user presses one of the Alt keys
<Pause>     The user presses the Pause key
<Caps_Lock> The user presses the Caps Lock key
<Esc>       The user presses the Escape keys

<Prior>     The Page Up key
<Next>      The Page Down key
<End>       The End key
<Home>      The Home key

<Left>      Cursor (arrows) keys
<Right>     Cursor (arrows) keys
<Up>        Cursor (arrows) keys
<Down>

<Num_Lock>
<Scroll_Lock>   The two Lock keys

<Shift-x>       The x key has been pressed along with any of the Shift, Alt, or Control keys
<Alt-x>
<Control-x>





# a callback designed for usage with the command property/parameter is a parameterless function;
# a callback intended to cooperate with the bind() method is a one-parameter function;
def click(event=None):
    tk.messagebox.showinfo("Click!", "I love clicks!")

button = tk.Button(window, text="Button", command=click) # direct bind
label = tk.Label(window, text="Label")
label.bind("<Button-1>", click)   # other way of binding

# An event object is an instantiation of the Event class
# widget 	        The widget’s object (not the widget’s name!) to which the event is addressed
# <x><y> 	        The mouse cursor’s coordinates at the moment of the event’s occurrence (both coordinates are counted relative to the target widget)
# <x_root> <y_root> As above, but relative to the screen
# <char> 	        The pressed key character code (only for keyboard events)
# <keysym> 	        The pressed key symbol (only for keyboard events)
# The full list of all recognized key symbols is presented here: https://www.tcl.tk/man/tcl8.4/TkCmd/keysyms.htm
# <keycode> 	    The pressed key numerical code (only for keyboard events)
# Don’t confuse this with char, which is the ASCII/UNICODE code of the character bound to the key
# <num> 	        The number of the clicked mouse button (only for mouse events)
# <type> 	        The event’s type

# -- how to unbind 
button = tk.Button(window, text="Button", command=click)
button.config(command=lambda:None) 
# This binds an empty (i.e., doing absolutely nothing) function to the widget’s callback

# -- another way to unbind
label.unbind("<Button-1>")

# -- un/bind to all widget in the window
window.bind_all(event, callback)
window.unbind_all(event)

# ---- 1.7 Visiting widgets properties

# -- two ways of modifying properties 

    #   1 with dict
button = tk.Button(window, text="OFF", command=on_off)
state = button["text"] # OFF
    #   2 - cget() and config()
state = button.cget("text") 
button.config(text=state)


# -- fonts

# Tkinter represents fonts as tuples  ("font_family_name", "font_size", "font_style")
# font_style is optionnal : bold / italic / underline / overstrike
label_1 = tk.Label(window, text="Hello", font=("Arial", "16", "bold"))    

# -- size of widget
# borderwidth 	        The width of the 3D-frame surrounding some widgets (e.g., Button)
# highlightthickness 	The width of the additional frame drawn around the widget when it gains the focus
# padx, pady 	        The width/height of an additional empty space/margin around the widget
# wraplength 	        If the text filling the widget becomes longer than this property’s value, it will be wrapped (possibly more than once)
# height                The height of the widget
# underline     The index of the character inside the widget’s text, 
#               which should be presented as underlined or -1 otherwise 
#               (the underlined letter/digit can be used as a shortcut key,
#                but it needs a specialized callback to work – no automation here, sorry)
# width 	The width of the widget

# -- color of widget
# background or bg 	    The color of the widget’s background (you can freely use either of these two forms)
# foreground or fgfg 	The color of the widget’s foreground (note: it can mean different things in different widgets; in general, it’s used to specify text color)
# activeforeground
# activebackground 	    Like bg and fg but used when the widget becomes active
# disabledforeground 	Foreground color used when the button is disabled. 

# -- anchors 
# 9 anchors : NW N NE E SE S SW W  CENTER (default)
button_2 = tk.Button(window, text="Another button")
button_2["anchor"] = tk.SW

# -- mouse cursor
# https://www.tcl.tk/man/tcl8.4/TkCmd/cursors.html
label_3 = tk.Label(window, height=3, text="heart", cursor="crosshair")


# ---- 1.8 Interacting with widgets methods

# -- some methods

Widget.after(1000, function)    # 1000 ms, using .sleep() freeze the whole application
Widget.after_cancel(id)         #  the method cancels the planned invocation identified by the id argument.
Widget.destroy()                # destroy a widget and its children in a recursively way
Widget.focus_get()              # returns a reference to the currently focused widget, or None (no widget has ficous)
Widget.focus_set()              # focuses the widget from the method which was invoked

#  focus_get -> you can invoke from any widget, including the main window


# ---- 1.9 Looking at variables

# -- observable variable
# you can only create an observable variable after the main window initialization
# a variable of that kind has to be explicitly created and initialized.
# these variables are typed,  -> don't change type during variable's life

# -- defiing a variable
# 4 constructor(default) :
# - BooleanVar (False),
# - DoubleVar (0.0),
# - IntVar (0),
# - StringVar("")
variable = tk.StringVar()  # define
variable.set('bonjour')    # set
print(variable.get())      # get

# -- adding an observer (unlimited) of a variable

obsid = variable.trace(trace_mode, observer)
# obsid is a string which is a unique observer identifier, it has low  utility 
# trace_mode : 
#   "r" :  if you want to be aware of the variable reads (accessing its value through get()
#   "w" – if you want to be aware of the variable writes (changing its value through set()
#   "u" – if you want to be aware of the variable's annihilation  (changing its value through set()

# defining an abserver 
def observer(id, ix, act):
# id – an internal observable variable identifier (unusable for us);
# ix – an empty string (always – don’t ask us why, it’s tkinter’s business)
# act – a string informing us what happened to the variable or, in other words, what reason triggered the observer ('r', 'w' or 'u')
#  If you don’t need any of the arguments, you can declare the observer as: def obs(*):

# removing observer 
s.trace_vdelete(trace_mode,obsid)

# trace_mode – the mode in which the observer has been created;
# obsid – the observer’s identifier obtained from the previous trace() invocation.




# ========================== Module 2 - lexicon of widgets ==================

two categories: clickable and non-clickable

# #  -- ========= clickable widgets

# -- Buton
# property : command (callback),  justify (text), state (disable, normal, active-> mouse above)
# method : flash( does not change its state), invoke (only way to invoke the callback)

# -- Checkbutton

# property : command, bd (border size), justify, state, variable, offvalue, onvalue
# method : deselect(), flash(), invoke(), select(), toggle()

# -- RadioButton
#  when two Radiobuttons use different observable variables, they belong to different groups by definition.
# property : command, justify, state, variable (IntVar or StringVar), value
# method : deselect(), flash(), invoke(), select()


#  -- ========= Non-clickable widgets


# -- Label
# property : text (use  as usual), textvariable (binded to a StringVar())
# method : no method ! but bind() is usable
# NB : the 2 properies are mutually exclusive

# -- Message
# The Message widget is very similar to the Label
# but it is able to format the presented text by fitting it automatically to the widget’s size.
# property : same as Label
# method : no method

# -- Frame
# the Frame has its own coordinate system
# the Frame can grasp virtually any widget – including another Frame.
# normally, the Frame doesn’t take the focus
# Each frame has its own geometry manager
# property : takefocus=1 
# method : none

# -- LabelFrame
# property : takefocus=1 , text, labelanchor (one of 12 compass coordinate)
# method : none
# compass coordinate : 3 by side: (NW-N-NE) (EN-E-ES) (SE-S-SW) (WS-S-WN)


# ---- 2.3 A small lexicon of widgets - part 3

# -- Entry
# binding a call back with the command properti is not the right way
# => setting the tracer function for the observable variable which cooperates with Entry
# property : command, show='*' (e.g. show='*' to enter a password), state, textvariable  (observable StringVar), width (in nb chars)
# method : get(), set(s),  insert(index,s)
# method : delete(first, last=None) 
#           if firts only -> one char. is deleted,
#           if last is specified as END, it points to the place after the last field’s character

# -- Menu
# to implement a menu :
# - create a top-level menu object
# - embed it inside the window
# - bind a number of required submenus (this is called a cascade) or connect a single callback.
main_menu = tk.Menu(window)
window.config(menu=main_menu)
sub_menu_file = tk.Menu(main_menu)
main_menu.add_cascade(label="File", menu=sub_menu_file)

 # item of a menu is not a widget, so to modify, we use : 
# item.entryconfigure(i, prop=value), ex :
sub_menu.entryconfigure(1, state=accessible)

# ---- 2.4 Shapping the main window  and conversing with the user (13 pages)

# modifying the logo in window requires a low-level mechanisms directly communicating with the OS’s window manager
window.tk.call('wm', 'iconphoto', window._w, PhotoImage(file='logo.png'))

# setting the size requires a string 
window.geometry("500x500")

# restricting the size to a minimum or a maximum or forbid resizing
window.minsize(width=250, height=200)
window.maxsize(width=500, height=300)
window.resizable(width=False, height=False)

# calling low level function to close window
def really():
    if messagebox.askyesno("?", "Wilt thou be gone?"):
        window.destroy()
#...
window.protocol("WM_DELETE_WINDOW", really)

# -- messagebox and all its options
messagebox.askyesno("?", "To be or not to be?")
# default, CANCEL, IGNORE, OK, NO, RETRY, and YES
# icon -> ERROR, INFO, QUESTION, and WARNING

# here are some more variations
answer = messagebox.askokcancel("?", "I'm going to format your hard drive")
answer = messagebox.askretrycancel("?", "Do you want to retry")
messagebox.askquestion("?", "I'm going to format your hard drive") # // yes or no
answer = messagebox.showerror("!", "Your code does nothing!")
answer = messagebox.showwarning("Be careful!", "Big Brother is watching you!")


# ---- 2.5 working with the Canvas (10 pages)

# a canvas can scroll itself and react to many events 

# -- creating a canvas
canvas = tk.Canvas(window, width=400, height=400, bg='yellow')

# -- creating a line : 
# smooth -> arrondi les angles vacec des paraboles
# arrow -> FIRST, END, BOTH
canvas.create_line(10, 380, 200, 10, 380, 380, 10, 380, arrow=tk.BOTH, fill='red', smooth=True, width=3)

# -- creating a rectangle 
# outline : is transparent if parameter missing
canvas.create_rectangle(200, 100, 300, 300, outline='white', width=5, fill='red')

# -- creating a polygone
#  he last segment (connecting the first and the last points) in the chain is drawn automatically
canvas.create_polygon(20, 380, 200, 68, 380, 380, outline='red', width=5, fill='yellow')

# -- creating an ellipse or a circle
# The method draws an ellipse inscribed in a rectangle with vertices at the points (x0,y0) and (x1,y1).
# If the rectangle is a square, the ellipse becomes a circle.
canvas.create_oval(100, 100, 300, 200, outline='red', width=20, fill='white')

# trigonometric direction, by defaut start at 0, and with an 90° angle 
canvas.create_arc(10, 100, 380, 300, outline='red', width=3, style=tk.PIESLICE, start=0, extent=90)
canvas.create_arc(10, 100, 380, 300, outline='blue', width=5, style=tk.CHORD, start=90, fill='white')
canvas.create_arc(10, 100, 380, 300, outline='green', width=5, style=tk.ARC, start=180, extent=180)

# -- creating text
canvas.create_text(200, 200, text="Maryhadalittlelamb", font=("Arial","40","bold"), justify=tk.CENTER, fill='white')
# fill 	    text color
# font 	    text font
# justify 	text justification: LEFT (default), CENTER, RIGHT
# text 	    text to display ( works as expected)
# width 	normally, the rectangle is as wide as the longest text line; using the width option forces the text to be aligned to that size

# -- creating image 
image = tk.PhotoImage(file='logo.png')
canvas.create_image(200, 200, image=image)
#  works only with png and gif 

# -- ... and with JPEG files
import PIL
# ...
jpg = PIL.Image.open('logo.jpg')
image = PIL.ImageTk.PhotoImage(jpg)
canvas.create_image(200, 200, image=image)

#  ==================================================== FIN ===============================






