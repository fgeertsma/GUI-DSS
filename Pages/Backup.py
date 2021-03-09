from Pages.FTP import *
from tkcalendar import Calendar, DateEntry
import tkinter as tk
import os
import Commander
import File_Transfer
import Global

class BackupWindow(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)  # ADDED parent argument.
        self.master.title("Backup Window")

        Instruct_Label = tk.Label(self, text='Choose date')


        Leave_Button = tk.Button(self, text="Quit",
                          command=lambda:          self.close())


        Backup_Button = tk.Button(self, text="Backup",
                                  command=lambda: self.backup(start_date=str(Start_Date_Calander.get()), start_time=(Start_Time_Slider.get()),
                                                               end_date=(End_Date_Calander.get()), end_time=(End_Time_Slider.get())))

#----------------------------Start-Date--------------------------------------------------------------------------------

        Start_Frame = tk.Frame(self, bg="DarkBlue", borderwidth=2)

        Start_Label = tk.Label(Start_Frame, text="Select Start Date/Time")

        Start_Date_Calander = DateEntry(Start_Frame, width=12, background='darkblue',
                        foreground='white', borderwidth=2, date_pattern='y-mm-dd')

        Start_Time_Slider = tk.Scale(Start_Frame, from_=0, to=23, orient=tk.HORIZONTAL)

#-----------------------------End-Date----------------------------------------------------------------------------------

        End_Frame = tk.Frame(self, bg="DarkRed", borderwidth=2)

        End_Label = tk.Label(End_Frame, text="Select End Date/Time")

        End_Date_Calander = DateEntry(End_Frame, width=12,       background='darkred',
                                            borderwidth=2,  foreground='white',
                                                            date_pattern='y-mm-dd')

        End_Time_Slider = tk.Scale(End_Frame, from_=0, to=23, orient=tk.HORIZONTAL)

#----------------------------Packing------------------------------------------------------------------------------------

        Leave_Button.pack()

        Start_Frame.pack(side=tk.LEFT, anchor=tk.N)
        Start_Label.pack()
        Start_Date_Calander.pack(side=tk.BOTTOM)
        Start_Time_Slider.pack(side=tk.TOP)

        End_Frame.pack(side=tk.RIGHT, anchor=tk.N)
        End_Label.pack()
        End_Date_Calander.pack(side=tk.BOTTOM)
        End_Time_Slider.pack(side=tk.TOP)

        Instruct_Label.pack(side=tk.TOP, anchor=tk.N)
        Backup_Button.pack(anchor=tk.N)
        #Leave_Button.pack(side=tk.BOTTOM)


    def start(self):
        self.mainloop()

    def close(self):
        Global.Close_State = False
        self.master.destroy()

    def backup(self, start_date, start_time, end_date, end_time):
        if(start_time < 10):
            start_time = "0" + str(start_time)
        start_time = str(start_time) + ":00:00"

        if(end_time < 10):
            end_time = "0" + str(end_time)
        end_time = str(end_time) + ":00:00"

        output = str(Commander.main(COMMAND_PATH="/home/smst/",     #make Backup
                                    COMMAND_NAME="Create_Backup_DB",
                                    ARGUMENTS="-s " + (start_date) + " -t " + (start_time) +" -e " + (end_date) + " -z " + (end_time) + " -d " + "dss",
                                    SUDO=True))


        if output.find("[sudo] password for smst: ")!= -1:
            output = output.split("[sudo] password for smst:", 2)[1]

        Count = output.find("meta.00")
        Name = output[Count-18: Count-1]

        if (os.path.exists("backup/")) == False:
            os.mkdir("backup/")

        output = File_Transfer.copy( DEST_FILE_PATH="/home/smst/influxdb/share/",
                                     DEST_FILE_NAME=Name,
                                     SOURCE_FILE_PATH="backup/",
                                     SOURCE_FILE_NAME="",
                                     arg="-r ")

        #print(output)

        output = str(Commander.main(COMMAND_PATH="",  # make Backup
                                    COMMAND_NAME="rm",
                                    ARGUMENTS="-r " + "/home/smst/influxdb/share/" + Name,
                                    SUDO=True))

        print("Exported database: " + Name + " -> " +   "Start: " + start_date + "_" + start_time +
                                                        " End: " + end_date + "_" + end_time)
