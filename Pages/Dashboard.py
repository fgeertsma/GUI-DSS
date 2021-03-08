import tkinter as tk
from Pages.FTP import *
from tkinter import filedialog
import os
import File_Transfer
import json
import requests
import Params

HOST = "http://" + Params.IP
DIR = 'exported-dashboards/'

class Dashboard_Window(tk.Frame):
    def __init__(self, parent=None):
        tk.Frame.__init__(self, parent)  # ADDED parent argument.
        self.master.title("Dashboard Window")

        Instruct_Label = tk.Label(self, text='Select Dashboard')

        Dashboard_Export_Button = tk.Button(self, text="Dashboard Export",
                                            command=lambda: self.Dashboard_Export())

        Dashboard_Import_Button = tk.Button(self, text="Dashboard Import",
                                            command=lambda: self.Dashboard_Import())

        Instruct_Label.pack()
        Dashboard_Import_Button.pack()
        Dashboard_Export_Button.pack()


    def start(self):
        self.mainloop()

    def Dashboard_Import(self):
        headers = {"Accept": "application/json",
                   "Content-Type": "application/json",
                   'Authorization': 'Bearer %s' % (Params.API_KEY)}

        filename = filedialog.askopenfilename(initialdir=DIR, title="Select file",
                                              filetypes=(("json files", "*.json"),
                                                         ("all files",
                                                          "*.*")))  # show an "Open" dialog box and return the path to the selected file
        print(filename)

        with open(filename) as json_file:
            data = json.load(json_file)

        response = requests.post('%s/api/dashboards/import' % (HOST), headers=headers, json=data, verify=True)
        print(response)
        print(response.status_code)
        print(response.text)



    def Dashboard_Export(self):
        headers = {'Authorization': 'Bearer %s' % (Params.API_KEY,)}
        response = requests.get('%s/api/search?query=&' % (HOST,), headers=headers)
        response.raise_for_status()
        dashboards = response.json()

        if not os.path.exists(DIR):
            os.makedirs(DIR)

        for d in dashboards:
            print("Saving: " + d['title'])
            response = requests.get('%s/api/dashboards/%s' % (HOST, d['uri']), headers=headers)
            data = response.json()['dashboard']
            dash = json.dumps(data, sort_keys=True, indent=4, separators=(',', ': '))
            name = data['title'].replace(' ', '_').replace('/', '_').replace(':', '').replace('[', '').replace(']', '')
            tmp = open(DIR + name + '.json', 'w')
            tmp.write('{\n' + '   "dashboard": ' + "\n")
            tmp.write(dash)
            tmp.write('\n}')
            tmp.close()
