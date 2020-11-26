
# coding: utf-8

# In[1]:


import os


# In[22]:


def similar_employee(data):
    #We will use following approach go column wise and get indices for count(element)>1
    #for the purpose of readability we will operate among lists 
    uname_list,ph_list,email_list,sameperson,notsameperson=[],[],[],[],[]
    for uname,phone,email in data:
        uname_list.append(uname)
        ph_list.append(phone)
        email_list.append(email)
    sameperson_uname=[i for i,user in enumerate(uname_list) if uname_list.count(user)>1]
    sameperson_phone=[i for i,user in enumerate(ph_list) if ph_list.count(user)>1]
    sameperson_email=[i for i,user in enumerate(email_list) if email_list.count(user)>1]
    for ele in [sameperson_uname,sameperson_phone,sameperson_email]:
        sameperson.extend(ele)
    sp=list(set(sameperson))
    for i in range(len(data)):
        if i not in sp:
            notsameperson.extend([i])
    return [sp,notsameperson]


# In[23]:


data = [
 ("username1","phone_number1", "email1"),
 ("usernameX","phone_number1", "emailX"),
 ("usernameZ","phone_numberZ", "email1Z"),
 ("usernameY","phone_numberY", "emailX"),
 ("username1","phone_numbera",  "emailY"),
  ("username0","phone_numbea",  "email"),
    ("username1","phone_numbera",""),
    ("username1","phone_number1", "email1")
  ]


# In[26]:


similar_employee(data)


# In[25]:


data = [
 ("username1","phone_number1", "email1")
  ]

