import tkinter as tk
from Pages.FTP import *
from tkinter import filedialog
import os
import File_Transfer
import Commander
import Global

class Restore_Window(tk.Frame):
    def __init__(self, parent=None):
        tk.Frame.__init__(self, parent)  # ADDED parent argument.
        self.master.title("Restore Window")

        Instruct_Label = tk.Label(self, text='Select Backup Folder')

        Restore_Button = tk.Button(self, text="Restore",
                          command=lambda: self.restore())

        Leave_Button = tk.Button(self, text="Quit",
                          command=lambda:          self.close())

        Leave_Button.pack()
        Instruct_Label.pack()
        Restore_Button.pack()


    def start(self):
        self.mainloop()

    def close(self):
        Global.Close_State = False
        self.master.destroy()

    def restore(self):
        filename = filedialog.askdirectory()  # show an "Open" dialog box and return the path to the selected file
        length=len(filename)
        file = filename[length-17:length]
        path = filename[0:length-len(file)]

        output = str(File_Transfer.paste( SOURCE_FILE_PATH=path,
                                          SOURCE_FILE_NAME=file,
                                          DEST_FILE_PATH="/home/smst/",
                                          DEST_FILE_NAME=""))
        #print(output)

        output = str(Commander.main(COMMAND_PATH="/home/smst/",
                                    COMMAND_NAME="Restore_Backup_DB",
                                    ARGUMENTS="-p " + "/home/smst/ " + "-n " + file,
                                    SUDO=True))
        #print(output)

        output = str(Commander.main(COMMAND_PATH="/home/smst/",
                                    COMMAND_NAME="Switch_DB",
                                    ARGUMENTS="-n " + file,
                                    SUDO=True))

        #print(output)

        output = str(Commander.main(COMMAND_PATH="",  # make Backup
                                    COMMAND_NAME="rm",
                                    ARGUMENTS="-r " + "/home/smst/influxdb/share/" + file,
                                    SUDO=True))

        #print(output)

        #os.system("Restore_Script " + path + " " + file)
