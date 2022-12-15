#!/usr/bin/env python
# coding: utf-8

#export PATH="/f/IB/Python/P_cod/hw8_sys_os:$PATH"

import sys
import os
import argparse
import shutil

parser = argparse.ArgumentParser(description="This programm copy file or directory")

parser.add_argument('path_from', nargs='?') 
parser.add_argument('path_to', nargs='?') 
parser.add_argument('-r', '--recursive', action='store_true', help='copy directories and their contents recursively') 
args=parser.parse_args()

path_from_copy=os.path.abspath(args.path_from)
path_to_copy=os.path.abspath(args.path_to)

if args.recursive:
    shutil.copytree(path_from_copy, path_to_copy,  dirs_exist_ok=True)
else:
    shutil.copy2(path_from_copy, path_to_copy)


