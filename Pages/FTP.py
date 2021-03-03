#from Main_Window import *
from Multi import *
import tkinter as tk
import os

class FTP_Window(tk.Frame):
    def __init__(self, parent=None):
        tk.Frame.__init__(self, parent)  # ADDED parent argument.
        self.master.title("Restore Window")

        self.path = "false"
        self.command = "ls"
        self.arguments = '"/"'
        self.sudo = "true"

        self.count = 1

        Instruct_Label = tk.Label(self, text='Select File or Directory')

        FTP_Button = tk.Button(self, text="Command",
                                   command=lambda: self.Set_Label(str(self.FTP(self.path, self.command, self.arguments, self.sudo))))

        Instruct_Label.pack()
        FTP_Button.pack()

    def start(self):
        self.mainloop()

    def FTP(self, path, command, arguments, sudo):
        os.system("Command_Script " + path + " " + command + " " + arguments + " " + sudo)

        output = open('C:/command/file.txt', "r")
        #os.remove('C:/command/file.txt')
        f = output.read()
        #print(f)
        if f.find("[sudo] password for smst: ")!= -1:
            f = f.split("[sudo] password for smst:", 2)[1]

        return f


    def folder(self, x, text):
        #print(x)
        #print(text)
        self.arguments = self.arguments.replace('/*"', '')
        self.arguments = self.arguments + text + '/'
        print(self.arguments)
        self.Set_Label(str(self.FTP(self.path, self.command, self.arguments, self.sudo)))

    def Set_Label(self, string):
        string = string.split()
        # for x in range(len(string)):
        #     print(string[x])
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

                btns.append(tk.Button(self.Dir, bg=self.check(string[x]),
                                           width=9, height=4,
                                           text=string[x], font='Helvetica 7 bold',
                                           command=lambda x=btn_nr: [self.folder(x, btns[x].cget("text")),
                                                                                                          self.update()]))

                if (btn_nr % 4) == 0:
                    line = 0
                    row += 1
                btns[btn_nr].grid(row=row, column=line)
                btn_nr += 1
                line += 1
        self.Dir.pack()

    def check(self, String):
        # path = "false"
        # command = "find"
        # arg = '"-e '
        # arg += String
        # arg += ' && echo file exists || echo file"'
        # sudo = "true"
        # #print("Command_Script " + command + " " + arg + " " + sudo)
        #
        # os.system("Command_Script " + path + " " + command + " " + arg + " " + sudo)
        #
        # output = open('C:/command/file.txt', "r")
        # # os.remove('C:/command/file.txt')
        # f = output.read()
        # if f.find("[sudo] password for smst: ")!= -1:
        #     f = f.split("[sudo] password for smst:", 2)[1]
        # print(f)
        return 'Grey'