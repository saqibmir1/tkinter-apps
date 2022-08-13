#!/usr/bin/python


from tkinter import *
from tkinter import filedialog
from tkinter import font

root=Tk()
root.title('Text Editor')
#root.iconbitmap('icon.ico')
root.geometry("1200x660")

#set var for open file name
global open_status_name
open_status_name=False

global selected
selected=False

# functions(commands)
def new_file():
    my_text.delete("1.0", END)
    root.title("New File - Text Editor")
    status_bar.config(text="New File        ")
    global open_status_name
    open_status_name=False

def open_file():
    my_text.delete("1.0", END)
    text_file=filedialog.askopenfilename(initialdir="/home/saqib", title="Open File")

    if text_file:
        global open_status_name
        open_status_name=text_file
        
    name=text_file
    status_bar.config(text=(f'{name}        '))
    name=name.replace("/home/saqib/", "")
    root.title(f'{name} - Text Editor')
    
    text_file=open(text_file, 'r')
    stuff=text_file.read()
    my_text.insert(END, stuff)
    text_file.close()

def save_as_file():
    text_file=filedialog.asksaveasfilename(defaultextension=".*", initialdir="/home/saqib", title="Save AS")
    if text_file:
        name=text_file
        status_bar.config(text=(f'Saved: {name}        '))
        name=name.replace("/home/saqib", "")
        root.title(f'{name} - Text Editor')

        text_file=open(text_file, 'w')
        text_file.write(my_text.get(1.0, END))
        text_file.close()

def save_file():
    global open_status_name
    if open_status_name:
        text_file=open(open_status_name, 'w')
        text_file.write(my_text.get(1.0, END))
        text_file.close()
        status_bar.config(text=(f'Saved: {open_status_name}        '))
    else:
        save_as_file()

def cut_text(e):
    global selected
    #check to see if keyboard shortct is used
    if e:
        selected=root.clipboard_get()
    else:
        if my_text.selection_get():
            #grab selected text
            selected=my_text.selection_get()
            #delete
            my_text.delete("sel.first", "sel.last")
            root.clipboard_clear()
            root.clipboard_append(selected)
        
def copy_text(e):
    global selected
    if e:
        selected=root.clipboard_get()
        
    if my_text.selection_get():
        selected=my_text.selection_get()
        #clear clipboard and append
        root.clipboard_clear()
        root.clipboard_append(selected)

def paste_text(e):
    global selected
    #check to see if keyboard shortcut used
    if e:
        selected=root.clipboard_get()
    else:
        if selected:
            position=my_text.index(INSERT)
            my_text.insert(position, selected)


#create main frame
my_frame=Frame(root)
my_frame.pack(pady=5)

#create scroll bar for text box
text_scroll=Scrollbar(my_frame)
text_scroll.pack(side=RIGHT, fill=Y)

#create text box
my_text=Text(my_frame, width=97, height=25, font=("Helvetica", 16), selectbackground="yellow", selectforeground="black", undo=True, yscrollcommand=text_scroll.set)
my_text.pack()

#configure scrollbar
text_scroll.config(command=my_text.yview)

#create menu
my_menu=Menu(root)
root.config(menu=my_menu)

#add file menu
file_menu=Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_command(label="Save As", command=save_as_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)

#add edit menu
edit_menu=Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Cut    (Ctrl+x)", command=lambda: cut_text(False))
edit_menu.add_command(label="Copy   (Ctrl+c)", command=lambda: copy_text(False))
edit_menu.add_command(label="Paste  (Ctrl+v)", command=lambda: paste_text(False))
edit_menu.add_command(label="Undo")
edit_menu.add_command(label="Redo")

#add status bar to bottom 
status_bar=Label(root, text='Ready        ', anchor=E)
status_bar.pack(fill=X, side=BOTTOM, ipady=5)

#edit bindings
root.bind('<Control-Key-x>', cut_text)
root.bind('<Control-Key-c>', copy_text)
root.bind('<Control-Key-v>', paste_text)


root.mainloop()
