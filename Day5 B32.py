#!/usr/bin/env python
# coding: utf-8

# In[ ]:


Continuation of lists:


# In[30]:


my_students = ['sara','ravi','akash','kiran']


# In[31]:


print(my_students)


# In[ ]:


Req: i want to add kishore to the 2nd index in the above list.


# In[32]:


my_students.insert(2,'kishore')


# In[33]:


print(my_students[2].title())


# In[34]:


print(my_students)


# In[ ]:


get_ipython().set_next_input('interview Question: Can you plz explain what is the diff bet append and insert method in a list');get_ipython().run_line_magic('pinfo', 'list')


# In[ ]:





# In[ ]:


how to Edit the elements from the list...?


# In[35]:


print(my_students)


# In[ ]:


Req: i want to replace ravi ------> with Satish


# In[37]:


my_students[1] = 'Satish'


# In[38]:


print(my_students)


# In[ ]:





# In[ ]:


how to delete the elements from the list..?


# In[42]:


print(my_students)


# In[ ]:


Req: i want to delete akash from the above list..?


# In[44]:


del my_students[3]   # del is method used to delete the elements form the list.


# In[45]:


print(my_students)


# In[ ]:





# In[ ]:


Understanding the pop method ** ---> It is used for deleting the elements only.

It will be keeping a carboncopy of the deleted items...like a backup.


# In[46]:


my_students


# In[47]:


x = my_students.pop()


# In[48]:


print(my_students)


# In[49]:


print(x)


# In[ ]:





# In[ ]:


## Organsing the lists:    


# In[ ]:





# In[57]:


cars = ['bmw','honda','audi','maruthi','benz','toyota']


# In[ ]:





# In[ ]:


Req: what is the total count of elements present in the list..?


# In[58]:


len(cars)


# In[ ]:


Req: i want to arrange the list in a alphabetical order A-Z


# In[ ]:


Two Approches:
    1. Temp Approch ------> sorted
    2. permanant Approch ----> sort


# In[59]:


print(sorted(cars))


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




