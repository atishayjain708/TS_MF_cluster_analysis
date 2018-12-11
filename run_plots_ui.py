import tkinter as tk
from tkinter import messagebox
import pygubu
import os


class MyApplication(pygubu.TkApplication):

    def _create_ui(self):
        #1: Create a builder
        builder = pygubu.Builder()

        #2: Load an ui file
        builder.add_from_file('small_ui.ui')

        #3: Create the widget using self.master as parent
        self.mainwindow = builder.get_object('Toplevel', self.master)

        # Connect method callbacks
        builder.connect_callbacks(self)

        linkage_method = self.linkage_box.get("1.0",END)
        # return input

    # define the method callbacks
    def generate_subplots(self):
        os.system('python3 gen_subplots.py '+linkage_method)


if __name__ == '__main__':
    root = tk.Tk()
    app = MyApplication(root)
    app.run()