import tkinter as tk
from Pages.FTP import *
from tkinter import filedialog
import os

class Restore_Window(tk.Frame):
    def __init__(self, parent=None):
        tk.Frame.__init__(self, parent)  # ADDED parent argument.
        self.master.title("Restore Window")

        Instruct_Label = tk.Label(self, text='Select Backup Folder')

        Restore_Button = tk.Button(self, text="Restore",
                          command=lambda: self.restore())

        Instruct_Label.pack()
        Restore_Button.pack()


    def start(self):
        self.mainloop()

    def restore(self):
        filename = filedialog.askdirectory()  # show an "Open" dialog box and return the path to the selected file
        length=len(filename)
        file = filename[length-17:length]
        path = filename[0:length-len(file)]

        os.system("Restore_Script " + path + " " + file)
