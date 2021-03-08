from Main_Screen import *

root = tk.Tk()
myWindow = MainScreen(master=root)
myWindow.master.title("Title")
myWindow.pack()  # ADDED
myWindow.start()


