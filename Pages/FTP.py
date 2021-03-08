#from Main_Window import *
from Main_Screen import *
import tkinter as tk
import os
import subprocess
import Commander
import re

path = ""
command = "ls"
arguments = "/"
sudo = True

class FTP_Window(tk.Frame):
    def __init__(self, parent=None):
        tk.Frame.__init__(self, parent)  # ADDED parent argument.
        self.master.title("Restore Window")



        self.count = 1

        Instruct_Label = tk.Label(self, text='Select File or Directory')

        FTP_Button = tk.Button(self, text="Command",
                                   command=lambda: self.Set_Label(str(self.FTP(path, command, arguments, sudo))))

        Instruct_Label.pack()
        FTP_Button.pack()

    def start(self):
        self.mainloop()

    def FTP(self, path, command, arguments, sudo):
        print(arguments)
        self.arguments = arguments


        output = str(Commander.main(COMMAND_PATH=path,
                                    COMMAND_NAME=command,
                                    ARGUMENTS=arguments,
                                    SUDO=sudo))

        if output.find("[sudo] password for smst: ")!= -1:
            output = output.split("[sudo] password for smst:", 2)[1]

        return output


    def folder(self, x, text):
        #print(x)
        #print(text)
        arguments = self.arguments.replace('/*"', '')
        arguments = arguments + text + '/'
        print(arguments)


    def Set_Label(self, string):
        #print(string)
        string = string.replace(r'\t', '   ')
        string = string.replace(r'\r', '   ')
        string = string.replace(r'\n', '   ')

        string = string.split()
        #for x in range(len(string)):
        #    print(string[x])
        btn_nr = 0
        btns = []
        try:
            self.Dir.destroy()
        except AttributeError:
            print("Dir does not exist")
        self.Dir = tk.Frame(self, bg="DarkBlue", borderwidth=2)
        line = 0
        row = 0
        self.Length = len(string)
        for x in range(self.Length):
            btns.append(tk.Button(self.Dir, bg='Grey',
                                       width=11, height=4,
                                       text=string[x], font='Helvetica 7 bold',
                                       command=lambda x=btn_nr: [self.Set_Label(str(self.FTP(
                                                                        path=path,
                                                                        command=command,
                                                                        arguments=(self.arguments + (btns[x].cget("text") + '/')),
                                                                        sudo=sudo))),
                                                                        self.update()]))

            if (btn_nr % 4) == 0:
                line = 0
                row += 1
            btns[btn_nr].grid(row=line, column=row)
            btn_nr += 1
            line += 1
            self.Dir.pack()

