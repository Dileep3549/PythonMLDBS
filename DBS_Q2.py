
# coding: utf-8

# Question 2.
# 
# Counting the pairs with k different from an integer list. 
# 
# eg: list = [1, 3,5] and k = 2
# 
# expected: we will have 2 pairs: {(1,3), (3,5)}
# 
# Note: we also consider the negative numbers. You may only use Python
# 

# In[16]:


import os
import itertools
os.getcwd()


# In[1]:


" tried in two different ways"


# In[8]:


def count_pairs(l,k):
    ret_pairs=[]
    for i,a in enumerate(l):
        for j,b in enumerate(l):
            if a!=b and abs(a-b)==k:
                ret_pairs.append(tuple(sorted([a,b])))
    return set(ret_pairs)         


# In[20]:


l=[1,3,5,-1,-2]
k=2
count_pairs(l,k)


# In[21]:


def disp_pairs(l,k):
    ret_pairs=[]
    iter_out=list(itertools.product(l,l))
    for ele in iter_out:
        if abs(ele[0]-ele[1])==k:
            ret_pairs.append(tuple(sorted(ele)))
    return(set(ret_pairs))


# In[22]:


l=[1,3,5,-1,-2]
k=2
disp_pairs(l,k)

