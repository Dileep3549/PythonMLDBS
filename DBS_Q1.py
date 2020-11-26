
# coding: utf-8

# The probability of x less than y in the joint probability distribution is 
# double integral of f(x,y)
# Here f(x,y) is e(pow(-x-y))
# so the solution for p(x less than y) is integral(-infinity ,+infinity)integral(o,y)exppfun()dydx
# 

# In[4]:


import math
from scipy import integrate


# In[2]:


def expfun(x,y):
    return math.exp(-x-y)


# In[10]:


sol=integrate.dblquad(expfun, 0, 1, lambda x: 0, lambda x: 1)


# In[20]:


print("probability of x < y is {}".format(sol[0]))

