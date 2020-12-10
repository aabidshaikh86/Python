#!/usr/bin/env python
# coding: utf-8

# In[2]:


fullname = 'abid sheikh'

print(fullname )


# In[ ]:


# Req: correct the name format above by using the string method.


# In[3]:


print(fullname.title()) # Titlecase ---> first Letter of the word will be capital


# In[ ]:





# In[ ]:


# Req: I want all the name to be in capital.


# In[4]:


print(fullname.upper()) ### Uppercase 


# In[ ]:





# In[ ]:


# Req: I want all the name to be in smallcase..


# In[5]:


print(fullname.lower())  ### Lowercase


# In[ ]:





# In[ ]:


*** Introduction to f strings in python.***


# In[ ]:





# In[ ]:


firstname = 'abid'
lastname = 'sheikh'


# In[ ]:


# Req: get me a fullname.


# In[ ]:


General syntax of a f string
f" custom string {placeholder1} {placeholder2} ......{nplaceholder}" ----> refercing point of the above variable created.


# In[16]:


x = f"{firstname} {lastname}"

print(x)


# In[17]:


print(x.title())


# In[ ]:





# In[ ]:


req :  i want to appreciate Abid for sending the practice file URL daily on time.


# In[18]:


print(f"keep up the goodwork, {x.title()}")


# In[ ]:




