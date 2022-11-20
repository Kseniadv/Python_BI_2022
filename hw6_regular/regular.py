#!/usr/bin/env python
# coding: utf-8

# In[1]:


import re
import pandas as pd


# In[2]:


#Task 1
# ftp://[user[:password]@]host[:port]/url-path

pattern = re.compile(r'ftp[.a-zA-z0-9/#]+') 

f = open('ftps', 'w')
f.close()

with open ('references.txt') as file:
    for line in file:
        ans = re.findall(pattern, line)
        with open ('ftps', 'a') as f:
            f.writelines('\n'.join(ans))


# In[4]:


#Task 2

pattern = re.compile(r'\d+.?\d+')

with open ('2430AD.txt') as file:
    for line in file:
        ans = re.findall(pattern, line)
        if len(ans) != 0:
            print('\n'.join(ans))


# In[5]:


#Task 3

pattern = re.compile(r'[a-z]*a[a-z]*', re.I)

with open ('2430AD.txt') as file:
    for line in file:
        ans = re.findall(pattern, line)
        if len(ans) != 0:
            print('\n'.join(ans))


# In[6]:


#Task 4

pattern = re.compile(r'[ \w\,\:\;]*\!')

with open ('2430AD.txt') as file:
    for line in file:
        ans = re.findall(pattern, line)
        if len(ans) != 0:
            print('\n'.join(ans))


# In[7]:


#Task 5.1

pattern = re.compile(r'[a-z]+', re.I)

d={}
def words_dict(words):  
    for word in words:        
        if word in d:
            d[word] = d[word] + 1
        else:
            d[word] = 1
    return d

l={}
def lenth_word(words):
    for word in words:
        if word  not in l:
            l[word] = len(word) 

with open ('2430AD.txt') as file:
    for line in file:
        line = line.lower()
        ans = re.findall(pattern, line)
        words_dict(ans)
        lenth_word(ans)

df_count=pd.DataFrame(list(d.items()),
                   columns=['word', 'quantity'])
df_lenth=pd.DataFrame(list(l.items()),
                   columns=['word', 'lenth'])

df_word = df_lenth.merge(df_count, left_on='word', right_on='word')
df_word

#df_word.hist(column='lenth')



        


# In[9]:


#Task 5.2

pattern = re.compile(r'[a-z]+', re.I)

ll={}
def ll_word(words):
    for word in words:
        ll[word] = len(word) 

with open ('2430AD.txt') as file:
    for line in file:
        line = line.lower()
        ans = re.findall(pattern, line)
        ll_word(ans)

df_len=pd.DataFrame(list(l.items()),
                   columns=['word', 'lenth'])


df_len
df_len.hist(bins=15)
       


# In[13]:


#Task 6
def translator(s):
    def replacer(match):
        num = match.group()
        return num+'к'+num
    new_l = [re.sub(r'[ауоиэыяюеёАУОИЭЫЯЮЕЁ]', replacer, l) for l in s] 
    return ''.join(new_l)

