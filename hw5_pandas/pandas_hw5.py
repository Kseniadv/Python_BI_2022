#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


# Task1

def read_gff(file):
    #pd.set_option('display.max_rows', 10) # не работает для styler
    pd.set_option('styler.render.max_rows', 10)
    df = pd.read_table(file, header=0, names = ['seq_id', 'source', 'type', 'start', 'end', 
                                                                  'score', 'strand', 'phase', 'attributes'])

    dfs = df.style.set_table_styles([{"selector":"thead",
                                "props": [("background-color", "lavender"), ("border-bottom","1px solid lightgray"),
                                          ("font-size", "13px")]},
                            {"selector":"th.row_heading",
                                "props": [("background-color", "lavender"), ("border-bottom","1px solid lightgray"),
                                          ("font-size", "12px")]},
                            {"selector" :"td",
                                "props": [("border-bottom","1px solid lightgray"), ("background-color", "white")] }])

    return dfs

read_gff('rrna_annotation.gff')


# In[3]:


def read_bed6(file):
    pd.set_option('styler.render.max_rows', 10)
    df = pd.read_table(file, header = None, names = ['chromosome', 'start', 'end', 'name', 'score', 'strand'] )
    dfb = df.style.set_table_styles([{"selector":"thead",
                                "props": [("background-color", "lavender"), ("border-bottom","1px solid lightgray"),
                                              ("font-size", "13px")]},
                            {"selector":"th.row_heading",
                                "props": [("background-color", "lavender"), ("border-bottom","1px solid lightgray"),
                                          ("font-size", "12px")]},
                            {"selector" :"td",
                                "props": [("border-bottom","1px solid lightgray"), ("background-color", "white")] }])
    
    return dfb

read_bed6('alignment.bed')


# In[4]:


an = pd.read_table('rrna_annotation.gff', header=0, names = ['chromosome', 'source', 'type', 'start', 'end', 
                                                                  'score', 'strand', 'phase', 'attributes'])
an['attributes'] = an['attributes'].str.extract("([1-9]+S)")
an


# In[5]:


pd.set_option('display.max_rows', None)
dr = pd.pivot_table(an,
              index=['chromosome'], columns=['attributes'], values = ['type'], aggfunc=len)
dr


# In[6]:


dr.plot.bar(xlabel="Sequens").legend(['16S','23S', '5S'], loc = 'upper right', fontsize = 'xx-small', 
                                     title = 'RNA type', title_fontsize = 'xx-small')


# In[7]:


pd.set_option('display.max_rows', 10)
bed = pd.read_table('alignment.bed', header = None, names = ['chromosome', 'start', 'end', 'name', 'score', 'strand'] )


# In[8]:


#pd.set_option('styler.render.max_rows', None)

ins = an.merge(bed, how = 'inner', left_on='chromosome', right_on='chromosome')
ins.loc[(ins['start_x'] > ins['start_y']) & (ins['end_x'] < ins['end_y'])!=True, 'start_x'] = 0
intersect = ins[ins['start_x'] != 0]
intersect.style.set_table_styles([{"selector":"thead",
                                "props": [("background-color", "lavender"), ("border-bottom","1px solid lightgray"),
                                          ("font-size", "13px")]},
                            {"selector":"th.row_heading",
                                "props": [("background-color", "lavender"), ("border-bottom","1px solid lightgray"),
                                          ("font-size", "12px")]},
                            {"selector" :"td",
                                "props": [("border-bottom","1px solid lightgray"), ("background-color", "white")] }])




# In[9]:


# Task2

dif = pd.read_table('diffexpr_data.tsv.gz')
dif.loc[(dif['logFC']<0) & (dif['log_pval'] >= 0.05), 'color'] = 'Significantly downregulated'
dif.loc[(dif['logFC']>0) & (dif['log_pval'] >= 0.05), 'color'] = 'Significantly upregulated'
dif.loc[(dif['logFC']<0) & (dif['log_pval'] < 0.05), 'color'] = 'Non-significantly downregulated'
dif.loc[(dif['logFC']>0) & (dif['log_pval'] < 0.05), 'color'] = 'Non-significantly upregulated'
dif.head()


# In[10]:


from matplotlib.ticker import AutoMinorLocator


# In[69]:


ax = sns.scatterplot(data =dif, x= 'logFC', y = 'log_pval', s = 10, hue = 'color',
                     hue_order = ['Significantly downregulated', 'Significantly upregulated',
                                       'Non-significantly downregulated', 'Non-significantly upregulated'])
ax.axhline(0.05, c = 'grey', ls = '--', lw = 1.5)
ax.axvline(0, c = 'grey', ls = '--', lw = 1.5)
ax.text(x=6.5, y=3, s='p value=0.05', fontsize=9, color='grey')


plt.xlabel(r'$log_2$ fold change', size=10, fontstyle='italic', weight =  'bold')
plt.ylabel(r'$-log_{10}$ (p value corrected)', size=10, fontstyle='italic', weight = 'bold')
plt.title('Volcano plot', size=15, fontstyle='italic', weight = 'bold')

ax.xaxis.set_minor_locator(AutoMinorLocator())
ax.yaxis.set_minor_locator(AutoMinorLocator())

ax.tick_params(which='major', width=2)
ax.tick_params(which='minor', length=1.5)

#ax.spines['bottom'].set_linewidth(1)

ax.legend(loc = 'upper right', fontsize=7, shadow=True)


        


# In[ ]:




