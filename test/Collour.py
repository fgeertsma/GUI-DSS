from tkinter import *

root = Tk()

button = Button(root, text="Click me!")
img = PhotoImage(file="C:/Users/frank/PycharmProjects/GUI/Buttons/Button-PNG-Picture.png") # make sure to add "/" not "\"
button.config(image=img)
button.pack() # Displaying the button

root.mainloop()