import tkinter as tk
import os
import Commander
import Global

class Command_Window(tk.Frame):
    def __init__(self, parent=None):
        tk.Frame.__init__(self, parent)  # ADDED parent argument.
        self.master.title("Restore Window")

        path = ""
        command = "ls"
        arguments = "/home/smst/ -a"
        sudo = True

        def Set_Label(string):
            output.insert(1.0, string)


        Instruct_Label = tk.Label(self, text='Select Command')

        Command_Button = tk.Button(self,    text="Command",
                                            command=lambda: Set_Label(str(self.command(path, command, arguments, sudo))))

        Leave_Button = tk.Button(self, text="Quit",
                          command=lambda:          self.close())


        output = tk.Text(self.master)
        output.pack()

        Leave_Button.pack()
        Instruct_Label.pack()
        Command_Button.pack()

    def start(self):
        self.mainloop()

    def close(self):
        Global.Close_State = False
        self.master.destroy()

    def command(self, path, command, arguments, sudo):

        output = str(Commander.main(COMMAND_PATH=path,
                                    COMMAND_NAME=command,
                                    ARGUMENTS=arguments,
                                    SUDO=sudo))

        if output.find("[sudo] password for smst: ")!= -1:
            output = output.split("[sudo] password for smst:", 2)[1]

        return output

