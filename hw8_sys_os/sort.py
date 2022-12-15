#!/usr/bin/env python
# coding: utf-8

#export PATH="/f/IB/Python/P_cod/hw8_sys_os:$PATH"

import sys
import os
import argparse
import re


parser = argparse.ArgumentParser(description="This programm arranges records")

parser.add_argument('file', nargs='?') 

args=parser.parse_args()



if args.file in (None, '-'):
    #args.file=sys.stdin.read().split('\n')
    args.file=re.split("  |\n", sys.stdin.read()) 

sort_list=sorted(args.file)
for line in sort_list:
    print(line)
