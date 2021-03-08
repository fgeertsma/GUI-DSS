#!/usr/bin/python
import os
import subprocess
import Params

Hostname = Params.User + '@' + Params.IP

def main(COMMAND_PATH, COMMAND_NAME, ARGUMENTS, SUDO):

    if (COMMAND_PATH == None):
        COMMAND_PATH = ""

    if (ARGUMENTS == None):
        ARGUMENTS = ""

    Command = str(COMMAND_PATH) + str(COMMAND_NAME) + " " + str(ARGUMENTS)

    if (SUDO == True):
        Command= ("echo -e " + Params.Password + " | sudo -S -i && sudo " + Command)

    Command = "plink " + "-batch " + "-ssh " + Hostname + " -t -pw " + Params.Password + ' "' + Command + '"'
    print(Command)
    try:
        Output = str(subprocess.check_output(Command, shell=True))
    except AttributeError:
        print("Command Error")

    Output = Output.replace(r'\n', '\n')
    Output = Output.replace(r'\r', '\r')
    Output = Output.replace(r'\t', '\t')
    Output = Output.replace("b'", "")       #Remove the b' at the start of every output
    Output = Output[:-1]                    #Remove the ' at the end of every output
    return (Output)

