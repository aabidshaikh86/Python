#!/usr/bin/env python
# coding: utf-8

# In[ ]:


Facebook Account:


# In[20]:


user = {'username':'codetraining09','Fname':'code','lname':'traning','pwd':76708,'dob':'1-1-2020'}


# In[25]:


print(user)


# In[6]:


type(user)


# In[ ]:


## give the key and get the Value!!!


# In[22]:


user['Fname']


# In[23]:


user['lname']


# In[ ]:


Req : Can we give the value and get the key


# In[36]:


user['codetraining09']


# In[ ]:


Note : ## Key ------------------> Value  ----> valid
    
       ## value ----------------> key    ----> invalid approch


# In[1]:





# In[ ]:


For loop implimentation on Top of a Dictionary::


# In[ ]:


General Formula:


# In[ ]:


------------FORMULA -----------------

for tempvar1, tempvar2 in mainvar.items():
    print(tempvar1)
    print(tempvar2)


# In[41]:


for x,y in user.items():
    print(x.upper())
    print(y)


# In[39]:


for x,y in user.items():
    print(f'key:{x}')
    print(f'value{y}\n')


# In[ ]:


req: i want to have only keys from the above.


# In[32]:


for x in user.keys():
    print(x)


# In[ ]:


Req: i want to have only values form the above.


# In[34]:


for y in user.values():
    print(y)


# In[ ]:





# In[ ]:




