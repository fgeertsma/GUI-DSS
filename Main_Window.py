from Pages.FTP import *



class MainScreen(tk.Frame):
    def __init__(self, parent=None):
        tk.Frame.__init__(self, parent)

        nextWin1 = Backup_Window()
        nextWin2 = Window_2()
        nextWin3 = Restore_Window()
        nextWin4 = Command_Window()
        nextWin5 = FTP_Window()

        screen1 = tk.Button(self, text="Screen1",
                            command=lambda: [self.destroy(),
                                             nextWin1.pack(),
                                             nextWin1.start()])

        screen2 = tk.Button(self, text="Screen2",
                            command=lambda: [self.destroy(),
                                             nextWin2.pack(),
                                             nextWin2.start()])

        screen3 = tk.Button(self, text="Screen3",
                            command=lambda: [self.destroy(),
                                             nextWin3.pack(),
                                             nextWin3.start()])

        screen4 = tk.Button(self, text="Screen4",
                            command=lambda: [self.destroy(),
                                             nextWin4.pack(),
                                             nextWin4.start()])

        screen5 = tk.Button(self, text="Screen5",
                            command=lambda: [self.destroy(),
                                             nextWin5.pack(),
                                             nextWin5.start()])

        screen1.pack()
        screen2.pack()
        screen3.pack()
        screen4.pack()
        screen5.pack()

    def start(self):
        self.mainloop()



