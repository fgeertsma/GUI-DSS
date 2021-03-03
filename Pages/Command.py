import tkinter as tk
import os

class Command_Window(tk.Frame):
    def __init__(self, parent=None):
        tk.Frame.__init__(self, parent)  # ADDED parent argument.
        self.master.title("Restore Window")

        path = "false"
        command = "ls"
        arguments = '"/home/smst/ -a"'
        sudo = "true"

        def Set_Label(string):
            output.insert(1.0, string)


        Instruct_Label = tk.Label(self, text='Select Command')

        Command_Button = tk.Button(self,    text="Command",
                                            command=lambda: Set_Label(str(self.command(path, command, arguments, sudo))))

        output = tk.Text(self.master)
        output.pack()



        Instruct_Label.pack()
        Command_Button.pack()

    def start(self):
        self.mainloop()

    def command(self, path, command, arguments, sudo):
        os.system("Command_Script " + path + " " + command + " " + arguments + " " + sudo)

        output = open('C:/command/file.txt', "r")
        #os.remove('C:/command/file.txt')
        f = output.read()
        #print(f)
        if f.find("[sudo] password for smst: ")!= -1:
            f = f.split("[sudo] password for smst:", 2)[1]

        return f

