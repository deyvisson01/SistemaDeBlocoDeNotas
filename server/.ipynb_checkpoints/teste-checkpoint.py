import glob
import os
import socket
import json
import threading

import sys
from os import rmdir


def files_path10(path):
    # '''return list of string'''
    return [os.path.join(p, file) for p, _, files in os.walk(os.path.abspath(path)) for file in files]

def caminhos(pasta):

    a = [os.path.join(pasta, nome) for nome in os.listdir(pasta)]


url = "Deyvisson/"


arg = files_path10(url)
args = caminhos(url)

print(arg)
print("\n")
print(args)
print("\n")
