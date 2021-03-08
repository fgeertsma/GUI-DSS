from Main_Screen import *
import Global

while(Global.Close_State == False):
    Global.Close_State = True
    root = tk.Tk()
    myWindow = MainScreen(master=root)
    myWindow.master.title("Title")
    myWindow.pack()  # ADDED
    myWindow.start()
    print("Ended")

