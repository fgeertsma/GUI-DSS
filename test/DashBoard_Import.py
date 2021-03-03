#!/usr/bin/env python

"""Grafana dashboard exporter"""

import json
import os
import requests
from tkinter import filedialog

HOST = 'http://192.168.180.20'
API_KEY = "eyJrIjoiUUJVRzNrcXZVczVXcnk0bUE5UWpoZHI4NzRid3ZneEQiLCJuIjoiRWRpdCBpbmZpbml0IiwiaWQiOjF9"

DIR = 'exported-dashboards'

def main():
    headers = {"Accept": "application/json",
               "Content-Type": "application/json",
               'Authorization': 'Bearer %s' % (API_KEY)}

    #response = requests.get('%s/api/search?query=&' % (HOST,), headers=headers)
    #response.raise_for_status()
    #dashboards = response.json()
    #print(dashboards)
    #
    filename = filedialog.askopenfilename(initialdir = DIR,title = "Select file",
                                          filetypes = (("json files","*.json"),
                                                       ("all files","*.*")))  # show an "Open" dialog box and return the path to the selected file
    print(filename)
    # if not os.path.exists(DIR):
    #     os.makedirs(DIR)
    #

    with open(filename) as json_file:
        data = json.load(json_file)


    #print(data)
    #print('%s/api/dashboards/import/' % (HOST))
    #print(data)

    response = requests.post('%s/api/dashboards/import' % (HOST), headers=headers, json=data, verify=True)
    print(response)
    print(response.status_code)
    print(response.text)

    #for d in dashboards:
    #     print ("Saving: " + d['title'])
    #     response = requests.get('%s/api/dashboards/%s' % (HOST, d['uri']), headers=headers)
    #     data = response.json()['dashboard']
    #     dash = json.dumps(data, sort_keys=True, indent=4, separators=(',', ': '))
    #     name = data['title'].replace(' ', '_').replace('/', '_').replace(':', '').replace('[', '').replace(']', '')
    #     tmp = open(DIR + name + '.json', 'w')
    #     tmp.write(dash)
    #     tmp.write('\n')
    #     tmp.close()


if __name__ == '__main__':
    main()
