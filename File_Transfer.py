#!/usr/bin/python
import os
import subprocess
import re

Password = 'sm20st07'
Hostname = 'smst@192.168.180.20'

def list(DEST_FILE_PATH, DEST_FILE_NAME, SOURCE_FILE_PATH, SOURCE_FILE_NAME):
    Command = "pscp " + " -pw " + Password + " -P 22 " "-ls " + Hostname + ":" + DEST_FILE_PATH + DEST_FILE_NAME


    try:
        Output = str(subprocess.check_output(Command, shell=True))
    except AttributeError:
        print("File Transfer Error")

    Output = Output.replace(r'\n', '\n')
    Output = Output.replace(r'\r', '\r')
    Output = Output.replace(r'\t', '\t')

    return (Output)


def copy(DEST_FILE_PATH, DEST_FILE_NAME, SOURCE_FILE_PATH, SOURCE_FILE_NAME):
    Command = "pscp " + "-r " + "-P " + "22 " + "-pw " + Password + " " + Hostname + ":" + \
               DEST_FILE_PATH + DEST_FILE_NAME + " " + SOURCE_FILE_PATH + SOURCE_FILE_NAME

    try:
        Output = str(subprocess.check_output(Command, shell=True))
    except AttributeError:
        print("File Transfer Error")

    Output = Output.replace(r'\n', '\n')
    Output = Output.replace(r'\r', '\r')
    Output = Output.replace(r'\t', '\t')

    return (Output)


def paste(DEST_FILE_PATH, DEST_FILE_NAME, SOURCE_FILE_PATH, SOURCE_FILE_NAME):
    Command = "pscp " + "-r " + "-P " + "22 " + "-pw " + Password + " " + SOURCE_FILE_PATH + SOURCE_FILE_NAME + " " + \
                                                         Hostname + ":" + DEST_FILE_PATH + DEST_FILE_NAME
    Progress = True

    if (Progress == True):
        os.system(Command)
        Output = ""
    else:
        try:
            Output = str(subprocess.check_output(Command, shell=True))
        except AttributeError:
            print("File Transfer Error")

    Output = Output.replace(r'\n', '\n')
    Output = Output.replace(r'\r', '\r')
    Output = Output.replace(r'\t', '\t')
    Output = Output[:-1]
    return (Output)
