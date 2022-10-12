#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import re
regex = "^[AaTtGgCc]+$"
pattern = re.compile(regex)
tra={'A': 'U', 'a': 'u', 'T': 'A', 't': 'a', 'C': 'G', 'c': 'g', 'G': 'C', 'g': 'c'} ##Dictionary of complementary 
                                                                                            #symbols for transcription
comp={'A': 'T', 'a': 't', 'T': 'A', 't': 'a', 'C': 'G', 'c': 'g', 'G': 'C', 'g': 'c'} #Complementary Dictionary
command = ['transcribe', 'reverse', 'complement', 'reverse complement']  #List of valid command
    
#transcribe sequence
def transcribe (a):
    c = []
    for i in range(len(a)): 
        for j in tra:
            if a[i] == j:
                c.append(tra[j])
    return(''.join(c))

#complement sequence
def complement (a):
    c = []
    for i in range(len(a)): 
        for j in comp:
            if a[i] == j:
                c.append(comp[j])
    return(''.join(c))

# reverse complement
def reverse_complement (a):
    c = []
    for i in range(len(a)): 
        for j in comp:
            if a[i] == j:
                c.append(comp[j])
    return(''.join(c[::-1]))



com = input('Enter command:')    #Enter first command
if com == 'exit':
    print('Good luck')
else:
    while com != 'exit':
        if com not in command:      #Command check
            print('Invalid command! Try again!')
            com = input('Enter command:')   
        seq = input('Enter sequence:')  #Enter sequence
        if pattern.search(seq) is not None: #DNA alphabet check
            if com == 'transcribe':
                print(transcribe(seq))
                com = input('Enter command:')
            elif com == 'reverse':
                print(''.join(reversed(seq))) # reverse sequence
                com = input('Enter command:')
            elif com == 'complement':
                print(complement(seq))
                com = input('Enter command:')
            elif com == 'reverse complement':
                print(reverse_complement(seq))
                com = input('Enter command:')
        else:
            print('Invalid alphabet! Try again!')

