#!/usr/bin/python
import argparse
import os

Password = 'sm20st07'
Hostname = 'smst@192.168.180.20'

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', '--COMMAND_PATH')
    parser.add_argument('-n', '--COMMAND_NAME')
    parser.add_argument('-a', '--ARGUMENTS')
    parser.add_argument('-s', dest='SUDO', action='store_true')
    args = parser.parse_args()

    if (args.COMMAND_PATH == None):
        args.COMMAND_PATH = ""

    if (args.ARGUMENTS == None):
        args.ARGUMENTS = ""

    # print(args.COMMAND_PATH)
    # print(args.COMMAND_NAME)
    # print(args.ARGUMENTS)
    # print(args.SUDO)



    Command = str(args.COMMAND_PATH) + str(args.COMMAND_NAME) + " " + str(args.ARGUMENTS)

    if (args.SUDO == True):
        os.system("plink " + "-batch " + "-ssh " + Hostname + " -t -pw " + Password + " echo -e " + Password +
                                                                                " | sudo -S -i && sudo " + Command)
    else:
        os.system("plink " + "-batch " + "-ssh " + Hostname + " -t -pw " + Password + " " + Command)
