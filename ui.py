#!/usr/bin/python
import sys
import os
from tkinter import *

master=Tk()
master.title('Plotter')
#You can set the geometry attribute to change the root windows size
master.geometry("500x500") #You want the size of the app to be 500x500
master.resizable(0, 0) #Don't allow resizing

bg = Frame(master, bg='gray')
bg.pack_propagate(0)
bg.pack(fill=BOTH, expand=1) #Expand the frame to fill the root window

# Display the custom image
img = PhotoImage(file='Plots/UI-Image.png')
panel = Label(bg, image = img)
panel.place(x=250, y=130, anchor='center')

# Display the box where we enter the name of clustering method
linkage_box = Entry(master=bg)
linkage_box.place(x=250, y=250, anchor='center')
# linkage_box.pack()

def show_plots():
    linkage_method = str(linkage_box.get())
    os.system('python3 gen_subplots.py '+linkage_method)

plot_button = Button(master=bg,text="Generate Subplots",command= show_plots)
plot_button.place(x=250, y=280, anchor='center')

master.mainloop()