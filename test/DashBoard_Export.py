

#!/usr/bin/env python

"""Grafana dashboard exporter"""

import json
import os
import requests

HOST = 'http://192.168.180.20'
API_KEY = "eyJrIjoiQm5GWVg2ZmRRbjJQZFhmb1RkeHI3d3RUd3FvVEFTUXMiLCJuIjoiaW5maW5pdCIsImlkIjoxfQ=="

DIR = 'exported-dashboards/'

def main():
    headers = {'Authorization': 'Bearer %s' % (API_KEY,)}
    response = requests.get('%s/api/search?query=&' % (HOST,), headers=headers)
    response.raise_for_status()
    dashboards = response.json()

    if not os.path.exists(DIR):
        os.makedirs(DIR)

    for d in dashboards:
        print ("Saving: " + d['title'])
        response = requests.get('%s/api/dashboards/%s' % (HOST, d['uri']), headers=headers)
        data = response.json()['dashboard']
        dash = json.dumps(data, sort_keys=True, indent=4, separators=(',', ': '))
        name = data['title'].replace(' ', '_').replace('/', '_').replace(':', '').replace('[', '').replace(']', '')
        tmp = open(DIR + name + '.json', 'w')
        tmp.write('{\n' + '   "dashboard": ' + "\n")
        tmp.write(dash)
        tmp.write('\n}')
        tmp.close()

        # with open('C:/Users/frankg/Desktop/Clean/GUI/test/exported-dashboards/Alarm_Panel.json', "r") as file:
        #     lines = file.readlines()
        #
        # lines[0] = '{\n' + '   "dashboard": {' + "\n"
        #
        # with open('C:/Users/frankg/Desktop/Clean/GUI/test/exported-dashboards/Alarm_Panel.json', "w") as file:
        #     for line in lines:
        #         file.write(line)
        #     file.write('\n}')
        # file.close()


if __name__ == '__main__':
    main()