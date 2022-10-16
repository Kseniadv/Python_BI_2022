#!/usr/bin/env python
# coding: utf-8

# In[51]:


#Counting GC content
def GC_comp(seq):
    GC = ((seq.upper().count('C') + seq.upper().count('G'))/len(seq.strip()))*100
    GC = round(GC, 2)
    return (GC)

#Counting average quality
def quality(seq):
    av = 0
    for sym in seq:
        q_score = ord(sym)-33
        av += q_score
    av = round(av/len(seq.strip()), 2)
    return(av)

#Check for file existence 
def is_accessible(path, mode='r'):
    try:
        f = open(path, mode)
        f.close()
    except IOError:
         return False
    return True

def main (input_fastq, output_file_prefix, gc_bounds = (0, 100), length_bounds = (0, 2**32),
          quality_threshold = 0, save_filtered = False):
    
    if type(gc_bounds) != tuple:
        gc_bounds = (0, gc_bounds)
    if type(length_bounds) != tuple:
        length_bounds = (0, length_bounds)
        
    output_passed = output_file_prefix + '_passed.fastq'
    if is_accessible(output_passed, mode='r') == True:
        f = open(output_passed, 'w')
        f.close
        
    output_failed = output_file_prefix + '_failed.fastq'
    if is_accessible(output_failed, mode='r') == True:
        f = open(output_failed, 'w')
        f.close
    
    i = 0

    with open (input_fastq) as file:
        line_count = sum(1 for line in open('test.fastq'))
        while i != line_count:
            one_rid = [next(file) for x in range(4)]
            GC = GC_comp(one_rid[1].strip())
            len_rid = len(one_rid[1].strip())
            av_qual = quality(one_rid[3].strip())
            if ((GC >= gc_bounds[0]) & (GC <= gc_bounds[1])) & ((len_rid >= length_bounds[0]) & (len_rid <= length_bounds[1]) 
                                                            & (av_qual >= quality_threshold)):
                with open (output_passed, 'a') as f:
                    f.writelines(one_rid)
            elif save_filtered == True:
                with open (output_failed, 'a' ) as f:
                    f.writelines(one_rid)            
            one_rid = []
            i +=4           
            

