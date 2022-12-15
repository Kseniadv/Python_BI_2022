#!/usr/bin/env python
# coding: utf-8

#export PATH="/f/IB/Python/P_cod/hw8_sys_os:$PATH"

import sys
import os
import argparse
import shutil

parser = argparse.ArgumentParser(description="This programm move file or directory")

parser.add_argument('path_from', nargs='?') 
parser.add_argument('path_to', nargs='?') 
args=parser.parse_args()

path_from_move=os.path.abspath(args.path_from)
path_to_move=os.path.abspath(args.path_to)


shutil.move(path_from_move, path_to_move)

