
# coding: utf-8

# In[1]:


from functools import lru_cache


# In[2]:


class pycache:
    setd=dict()
    sets=set()
    def __init__(self,cmd,*inp):
        self.command=cmd
        self.params=inp   
    @lru_cache()
    def operations(cmd,*inp,setd=setd):
        if cmd=="SET":
            setd[inp[0]]=inp[1]
            return setd,True  
        if cmd=="GET":
            if inp[0] in setd:
                return [setd[inp[0]]]
        if cmd=="MSET":
            for i in range(0,len(inp),2):
                setd[inp[i]]=inp[i+1]
            return setd
        if cmd=="MGET":
            return ([setd[i] for i in list(inp) if i in setd])            
            


# In[8]:


#examples


# In[3]:


op=pycache


# In[5]:


op.operations("SET",1,2)


# In[7]:


op.operations("GET",1)


# In[8]:


op.operations("MSET",1,2,3,4,5,6)


# In[9]:


op.operations("MGET",1,3,5)

