#!/usr/bin/env python
# coding: utf-8

# In[ ]:


list Continuation :


# In[ ]:





# In[1]:


cars = ['benz','toyota','maruti','audi','bnw']


# In[ ]:


## Organising the list datatype


# In[ ]:


req : i want to organise the data in the alphabetical order !!! A  to  Z


# In[ ]:


Two different approcahes :
    1. Temp approch       -------> sorted
    2. Permanent approch  -------> sort


# In[ ]:


## In the sorted (temp) approach we will be having the orginal order of the list!!

## In the sort (permanenet) approch we will not be having the original order back!!


# In[8]:


print(sorted(cars))  ## Temp approach


# In[10]:


print(cars)  ## Original Approch


# In[11]:


cars.sort()   ## permanent approach

print(cars)


# In[12]:


print(cars)


# In[ ]:


*** Interview : what is the diff bet sorted and Sort?? ***


# In[ ]:





# In[ ]:


get_ipython().set_next_input('Req: i want to print the list in the reverse order');get_ipython().run_line_magic('pinfo', 'order')


# In[13]:


print(cars)


# In[14]:


cars.reverse()    ## Reverse Order 
 
print(cars)


# In[ ]:


## How do you count the no of Elements in a list?? ##


# In[15]:


len(cars)      ## Count method


# In[ ]:


## introduction to slicing of the lists::


# In[17]:


students = ['mohini','rachana','uma','swapna','vidhya','naveena']


# In[18]:


print(students)


# In[19]:


type(students)


# In[ ]:


## General syntex of slicing:

-------FORMULA-----------

var[startvalue:stopvalue:step count] ------> this is the formula.

Note : Last value is always exclusive..!!


# In[28]:


print(students[0:1])


# In[29]:


print(students[0:2])


# In[36]:


print(students[4:6]) ## Last value is always exclusive and it will not be considered!!


# In[38]:


print(students[0:6:2])  ## Alternare name of the students..!!


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




