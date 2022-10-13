#!/usr/bin/env python
# coding: utf-8

# In[40]:


#Counting GC content
def GC_comp(seq):
    GC = ((seq.upper().count('C') + seq.upper().count('G'))/len(seq))*100
    return (GC)

#Counting average quality
def quality(seq):
    av = 0
    for sym in seq:
        q_score = ord(sym)-33
        av += q_score
    av = round(av/len(seq), 2)
    return(av)

def main (input_fastq, output_file_prefix, gc_bounds = (0, 100), length_bounds = (0, 2**32),
          quality_threshold = 0, save_filtered = False):
    
    if type(gc_bounds) == int or type(gc_bounds) == float:
        gc_bounds = (0, gc_bounds)
    if type(length_bounds) == int or type(length_bounds) == float:
        length_bounds = (0, length_bounds)
        
    output_passed = output_file_prefix + '_passed.fastq'
    output_failed = output_file_prefix + '_failed.fastq'
    
    one_read = []
    i = 0

    with open (input_fastq) as file:
        if i != 4:
            for line in file:         
                one_read.append(line.strip())
                i = i + 1  
                
        GC = GC_comp(one_read[1])
        len_rid = len(one_read[1])
        av_qual = quality(one_read[3])
        
        if ((GC >= gc_bounds[0]) & (GC <= gc_bounds[1])) & ((len_rid >= length_bounds[0]) & (len_rid <= length_bounds[1]) 
                                                            & (av_qual >= quality_threshold)):
            with open (output_passed, 'a' ) as f:
                for element in one_read:
                    f.write(element)
                    f.write('\n')
        elif save_filtered == True:
            with open (output_failed, 'a' ) as f:
                for element in one_read:
                    f.write(element)
                    f.write('\n')
        i = 0
        one_read = []

