#!/usr/bin/env python
#export PATH="/f/IB/Python/P_cod/hw8_sys_os:$PATH"

import sys
import os
import argparse


parser = argparse.ArgumentParser(prog = 'wc', description = 'The program count lines and words in file, prtint the bites of counts')

parser.add_argument('filename', nargs='*') 
parser.add_argument('-l', '--lines', help='coun lines in file', action='store_true')
parser.add_argument('-w', '--words', help='coun words in file', action='store_true') 
parser.add_argument('-c', '--bites', help='return size of file', action='store_true') 

args = parser.parse_args()

#if args.filename==[]:
#    args.filename = sys.stdin.readline().strip()
#print(args.filename)

def count_lines(file):
    with open(file) as f:
        lines = len(f.readlines())
    return lines

def count_words(file):
    with open(file) as f:
        words = len(f.read().split())
    return words

def count_bites(path):
    bites = os.path.getsize(path)
    return bites


count={'lines': 0, 'words': 0, 'bites': 0}

for files in args.filename:
    path_to_file = os.path.abspath(files)
    answer=[]
    if args.lines:
        answer.append(count_lines(path_to_file))
        count['lines']+=count_lines(path_to_file)
        
    if args.words:
        answer.append(count_words(path_to_file))
        count['words']+=count_words(path_to_file)
    if args.bites:
        answer.append(count_bites(path_to_file))
        count['bites']+=count_bites(path_to_file)
    
    if len(answer)==0:
        answer=[count_lines(path_to_file), count_words(path_to_file), count_bites(path_to_file)]
        count['lines']+=count_lines(path_to_file)
        count['words']+=count_words(path_to_file)
        count['bites']+=count_bites(path_to_file)
    
    answer.append(os.path.basename(path_to_file))
    print(*answer)
    
if len(args.filename)>1:
    print(*[val for val in dict.values(count) if val>0], 'total')