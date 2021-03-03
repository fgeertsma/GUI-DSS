import requests

headers = {"Accept": "application/json","Content-Type": "application/json" ,"Authorization": "Bearer eyJrIjoiQm5GWVg2ZmRRbjJQZFhmb1RkeHI3d3RUd3FvVEFTUXMiLCJuIjoiaW5maW5pdCIsImlkIjoxfQ=="}

r = requests.get("http://192.168.180.20",headers=headers)
print(r.text)
print(r.status_code)


#url = '192.168.180.20/api/dashboards/uid/cIBgcSjkk'
#myobj = {'somekey': 'somevalue'}
#
#
#x = requests.get(url, data = myobj)
#
#print(x.text)