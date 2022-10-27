#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np

if __name__ == "__main__":
        ar1 = np.array([1, 2, 21])
        ar2 = np.arange(1,19).reshape(3,-1)
        ar3 = np.zeros(5)

def matrix_multiplication(h,i):
    #s = np.matmul(h, i)
    s = np.dot(h,i)
    return s

def multiplication_check(L): #L - list of matrix
    c = []
    for i in range(len(L)-1):
        if (L[i].shape[1] == L[i+1].shape[0]):
            c.append(True)
        else:
            c.append(False)
            break
    if False not in c:
        return True
    else:
        return False
    
def  multiply_matrices(L):
    if multiplication_check(L) == True:
        for i in range(len(L)-1):
            pr = np.dot(L[i],L[i+1])
    else:
        pr = "None"
    return pr

def compute_2d_distance(a,b):
    d = np.sqrt((b[0]-a[0])**2 + (b[1]-a[1])**2)
    return d

def compute_multidimensional_distance(e,f):
    s=0
    for i in range(e.shape[0]):
        s += (f[i]-e[i])**2
    dist = np.sqrt(s)
    return  dist 

def compute_pair_distances(ar):
    new = np.zeros([ar.shape[0], ar.shape[0]])      
    for i in range(ar.shape[0]):
        for j in range(ar.shape[0]):
            if i != j:
                new[i,j] = compute_multidimensional_distance(ar[i],ar[j])
            else:
                new[i,j] = 0
    return new

