#!/usr/bin/python
from tkinter import *
import platform, pwd

root=Tk()
root.title("System Info App")
root.geometry("900x300")

system_info= f"System: {platform.system()}\n \
        User Name: {platform.node()}\n \
        Version: {platform.version()}\n \
        Machine: {platform.machine()}\n \
        Processor: {platform.processor()}\n \
        Python Version: {platform.python_version()}\n \
"


label_system_info=Label(root, text=system_info, font=("Helvetica", 14))
label_system_info.pack(pady=20)

root.mainloop()
