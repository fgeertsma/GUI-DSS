import tkinter as tk
from Pages.FTP import *
from tkcalendar import Calendar, DateEntry
import os
import Commander
from datetime import datetime
from datetime import date
import Params

class Report_Window(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)  # ADDED parent argument.

        self.master.title("Report Window")

        Instruct_Label = tk.Label(self, text='Choose date')

        Report_Button = tk.Button(self, text="Report",
                                  command=lambda: self.report(Start_Date_Calander.get(), Start_Time_Slider.get(),
                                                              End_Date_Calander.get(), End_Time_Slider.get()))

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

        Start_Frame.pack(side=tk.LEFT, anchor=tk.N)
        Start_Label.pack()
        Start_Date_Calander.pack(side=tk.BOTTOM)
        Start_Time_Slider.pack(side=tk.TOP)

        End_Frame.pack(side=tk.RIGHT, anchor=tk.N)
        End_Label.pack()
        End_Date_Calander.pack(side=tk.BOTTOM)
        End_Time_Slider.pack(side=tk.TOP)

        Instruct_Label.pack(side=tk.TOP, anchor=tk.N)
        Report_Button.pack(anchor=tk.N)

        #end_slide.set(os.popen("time /T").read()[1:2])                                                            #Set slider equal to time

    def start(self):
        self.mainloop()


    def report(self, start_date, start_time, end_date, end_time):
        #start_time = str(start_time) + ":00:00"
        #if start_time < 10:
            #start_time = "0" + start_time

        #end_time = str(end_time) + ":00:00"
        #if e_time < 10:
           # end_time = "0" + end_time

        start_date = date(int(start_date[0:4]), int(start_date[6:7]), int(start_date[9:10]))
        end_date = date(int(end_date[0:4]), int(end_date[6:7]), int(end_date[9:10]))

        now = str(datetime.now())
        now_time = now[11:16]

        now_date = date(int(now[0:4]), int(now[6:7]), int(now[9:10]))

        start_time_delta = str(int(now_time[0:2]) - start_time) + ":" + str(int(now_time[3:5]))
        end_time_delta = str(int(now_time[0:2]) - end_time) + ":" + str(int(now_time[3:5]))

        start_date_delta = str(now_date - start_date)
        start_date_delta = start_date_delta.split("0:00:00", 2)[0]
        start_date_delta = start_date_delta.split("days,", 2)[0]
        end_date_delta = str(now_date - end_date)
        end_date_delta = end_date_delta.split("0:00:00", 2)[0]
        end_date_delta = end_date_delta.split("days,", 2)[0]




        start = str(start_date_delta)[:-1] + 'd'

        end = str(end_date_delta)[:-1]

        TimeSpan = "'from=now-" + start
        TimeSpan += "&to=now"
        if (end != ""):
            TimeSpan += "-"  + end + 'd' +"'"
        else:
            TimeSpan += "'"

        filename = TimeSpan + ".pdf"
        Dashboard = "oBjEVCPGz"
        API = "eyJrIjoieUNXNzdZZDB4aFV5MklkRFF3MDVFaTZHOTE1cEtqWVEiLCJuIjoiS2V5IiwiaWQiOjF9"
        IP = Params.IP + ':' + str(Params.Report_Port)

        output = str(Commander.main(  COMMAND_PATH="/home/smst/go/bin/",
                                      COMMAND_NAME="grafana-reporter",
                                      ARGUMENTS="-cmd_enable=1 -cmd_apiKey " + Params.API_KEY + " -ip " + IP + " -cmd_dashboard " + Dashboard + " -cmd_ts " + TimeSpan + " -cmd_o " + filename,
                                      SUDO=True))
        print(output)
        #os.system("Report_Script " + start_date + " " + start_time + " " + end_date + " " + end_time)
