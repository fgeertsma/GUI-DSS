#!/usr/bin/python
import os
import subprocess

Password = 'sm20st07'
Hostname = 'smst@192.168.180.20'

def main(COMMAND_PATH, COMMAND_NAME, ARGUMENTS, SUDO):


    if (COMMAND_PATH == None):
        COMMAND_PATH = ""

    if (ARGUMENTS == None):
        ARGUMENTS = ""

    Command = str(COMMAND_PATH) + str(COMMAND_NAME) + " " + str(ARGUMENTS)

    if (SUDO == True):
        Command= ("echo -e " + Password + " | sudo -S -i && sudo " + Command)

    Command = "plink " + "-batch " + "-ssh " + Hostname + " -t -pw " + Password + ' "' + Command + '"'
    Output = str(subprocess.check_output(Command, shell=True))
    return (Output)


if __name__ == "__main__":
    main()