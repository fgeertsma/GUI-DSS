import tkinter as tk
from Pages.FTP import *
from tkcalendar import Calendar, DateEntry
import os


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


    def report(self, start_date, s_time, end_date, e_time):
        start_time = str(s_time) + ":00:00"
        #if s_time < 10:
            #start_time = "0" + start_time

        end_time = str(e_time) + ":00:00"
        #if e_time < 10:
           # end_time = "0" + end_time

        os.system("Report_Script " + start_date + " " + start_time + " " + end_date + " " + end_time)
