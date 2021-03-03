import tkinter as tk

root = tk.Tk()

frame1 = tk.Frame(root, height = 100, width = 100, bg = "WHITE", borderwidth=2)
frame2 = tk.Frame(frame1, height = 100, width = 100, bg = "RED", borderwidth=2)
frame1.pack()
frame2.pack()
label = tk.Label(frame2, text = "Label") #Receive a callback from button here
label.pack()
button = tk.Button(frame1, text="Button") #Send some action to Label here
button.pack()
tk.mainloop()