#from Main_Window import *
from Multi import *

root = tk.Tk()
myWindow = MainScreen(master=root)
myWindow.master.title("Title")
myWindow.pack()  # ADDED
myWindow.start()


