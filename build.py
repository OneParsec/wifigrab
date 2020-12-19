#!/usr/bin/python3
import argparse
from os import system

parser = argparse.ArgumentParser(description="WifiGrab Build System")
parser.add_argument("-S", action="store", dest="script", required=True, help="Script name")
parser.add_argument("-I", action="store", dest="icon", default="icon.ico", help="Icon name")
args = parser.parse_args()

buildcommand = "pyinstaller -F " + args.script + " -i " + args.icon
system(buildcommand)