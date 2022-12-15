#!/usr/bin/env python
# coding: utf-8

#export PATH="/f/IB/Python/P_cod/hw8_sys_os:$PATH"

import sys
import os
import argparse
import shutil

parser = argparse.ArgumentParser(description="This programm remove file or directory")

parser.add_argument('file', nargs='?') 
parser.add_argument('-r', '--recursive', action='store_true', help='remove directories and their contents recursively') 
args=parser.parse_args()

path_to_file=os.path.abspath(args.file)

if args.recursive:
    shutil.rmtree(path_to_file)
else:
    if os.path.isfile(path_to_file):
        os.remove(path_to_file)
    elif os.path.isdir(path_to_file):
        os.rmdir(path_to_file)

