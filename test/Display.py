import tkinter as tk
import os
import json
from tkinter import Toplevel
cert = ""

username = ""
password = ""
base_url = ''
url = ''
splash_page = ''

class BuildApplication(tk.Frame):

    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        self.lUSER = tk.Label(self, text="Username: ")
        self.lUSER.pack(side="left")
        self.eUSER = tk.Entry(self)
        self.eUSER.pack(side="left")

        self.lPASS = tk.Label(self, text="Password: ")
        self.lPASS.pack(side="left")
        self.ePASS = tk.Entry(self, show="*")
        self.ePASS.pack(side="left")

        #ive tried command= lambda: self.setCredentials(self.eUSER.get(),self.ePASS.get())
        #            command = self.setCredentials(self.eUSER.get(),self.ePASS.get())
        #          But none if it works....
        self.LOGIN = tk.Button(self, text = "Login", fg="green", command=self.setCredentials )
        self.LOGIN.pack(side="left")

        self.QUIT = tk.Button(self, text="QUIT", fg="red", command=self.master.destroy)
        self.QUIT.pack(side="left")

        #self.mainloop()

    def setCredentials(self):
        username = self.eUSER.get()
        password = self.ePASS.get()
        print("username", username)
        print("password", password)
        self.master.destroy()

class SearchApplication(tk.Frame):

    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        print()
        self.some_abel = tk.Label(self, text="create somethng")
        self.some_abel.pack(side="left")
        self.quitb = tk.Button(self, text = "quit", fg="green", command=self.master.destroy )
        self.quitb.pack(side="left")

class MainApplication(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        #Build Data
        self.bBuild = tk.Button(self, text="Build Data", command=self.build)
        self.bBuild.pack(side="top")

        #Search Data
        self.bSearch = tk.Button(self, text="Search",command=self.search)
        self.bSearch["text"] = "Search"
        self.bSearch["command"] = self.search
        self.bSearch.pack(side="top")

        #quit
        self.QUIT = tk.Button(self, text="QUIT", fg="red", command= self.master.destroy)
        self.QUIT.pack(side="bottom")

    def build(self):
        print("Building")
        root2  = tk.Toplevel()
        buildApp = BuildApplication(master=root2)


    def search(self):
        print("Search")
        root3  = tk.Toplevel()
        app2 = SearchApplication(master=root3)

root = tk.Tk()
app = MainApplication(master=root)
app.master.title("fdsafds")

app.mainloop()