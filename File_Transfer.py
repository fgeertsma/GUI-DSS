#!/usr/bin/python
import os
import subprocess
import re

Password = 'sm20st07'
Hostname = 'smst@192.168.180.20'

def main():

#DEST_FILE_PATH, DEST_FILE_NAME, SOURCE_FILE_PATH, SOURCE_FILE_NAME
    DEST_FILE_PATH = "/home/smst/"
    DEST_FILE_NAME = ""
    SOURCE_FILE_PATH = ""
    SOURCE_FILE_NAME = ""

    Command = "pscp " + " -pw " + Password + " -P 22 " "-ls " + Hostname + ":" + DEST_FILE_PATH + DEST_FILE_NAME

    # Command = "pscp " + "-P " + "22 " + "-pw " + Password + " " + Hostname + ":" + \
    #           DEST_FILE_PATH + DEST_FILE_NAME + " " + SOURCE_FILE_PATH + SOURCE_FILE_NAME

    #os.system(Command)
    Output = str(subprocess.check_output(Command, shell=False))
    Output = Output.replace(r'\r\n', '\r\n')
    print(Output)
    #return (Output)


if __name__ == "__main__":
    main()