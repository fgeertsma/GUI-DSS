with open('C:/Users/frankg/Desktop/Clean/GUI/test/exported-dashboards/Alarm_Panel.json', "r") as file:
    lines = file.readlines()

lines[0] = '{\n' + '   "dashboard": {' + "\n"

with open('C:/Users/frankg/Desktop/Clean/GUI/test/exported-dashboards/Alarm_Panel.json', "w") as file:
    for line in lines:
        file.write(line)
    file.write('\n}')
file.close()