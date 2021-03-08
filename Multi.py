from Pages.Backup import *
from Pages.Report import *
from Pages.Restore import *
from Pages.Command import *
from Pages.Dashboard import *

Windows = ["Backup_Window",
           "Report_Window",
           "Restore_Window",
           "Command_Window",
           "FTP_Window",
           "Dashboard_Window"]

Collour = ['Blue',
           'Red',
           'Yellow',
           'Green',
           'Purple',
           'Cyan']

class MainScreen(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)

        w = tk.Label(self, text="Main Screen")
        w.pack()

        self.btn_nr = 0
        self.btns = []

        for x in range(0, len(Windows)):
                self.btns.append(tk.Button(self,    bg=Collour[self.btn_nr],
                                                    width=20, height=6,
                                                    text=Windows[self.btn_nr], font='Helvetica 12 bold',
                                                    command=lambda x=self.btn_nr: [ self.destroy(),
                                                                                    self.action(x)]))

                self.btns[self.btn_nr].pack()
                self.btn_nr += 1


    def action(self, button):
        self.name = Windows[button]
        self.name += "()"

        self.nextWin = eval(self.name)
        self.nextWin.pack()

        self.nextWin.start()

    def start(self):
        self.mainloop()