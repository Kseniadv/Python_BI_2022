#!/usr/bin/env python
# coding: utf-8
 
#export PATH="/f/IB/Python/P_cod/hw8_sys_os:$PATH"

import sys
import os
import argparse
import stat


description = """
The program print lists the files and 
subdirectories contained in a target directory
"""

parser = argparse.ArgumentParser(description)

parser.add_argument('path_to_directory', nargs='?') 
parser.add_argument('-a', '--all', action='store_true', help=' do not ignore entries starting with')

args=parser.parse_args()

if args.path_to_directory in (None, '-'):
    args.path_to_directory = './'

print('  '.join(os.listdir(args.path_to_directory)))

#list=os.listdir(args.path_to_directory)
#out = sys.stdout
#for item in list:
#    out.write('  '+item)


