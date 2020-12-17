#!/usr/bin/env python
# coding: utf-8

# In[ ]:


Introducting to tuple datatype::


# In[ ]:


Defination : A tuple is nothing but in immutable list OR
    
An Immutable list is called a tuple.

Classification : it is classified as an immutable datatype.
    
how do you define a tuple ..? ()  -----> General brackets.


# In[ ]:





# In[2]:


students = ('dilip','rachana','chandana','abid','kumar')


# In[3]:


print(students)


# In[4]:


type(students)


# In[ ]:


Req : i want to replace dilip with suhail


# In[5]:


students[0] = "suhail"  ## Tuple doent support item assignment..


# In[7]:


dimension = (200,100)  ## Dimension


# In[8]:


print(dimension)


# In[9]:


dimension = (140,50)


# In[10]:


print(dimension)


# In[ ]:





# In[11]:


print(students)


# In[14]:


students[1]


# In[ ]:





# In[ ]:


### for loop implimentation on top of a tuple!!! ###


# In[16]:


for x in students:     ## Looping Method
    print(x.title())


# In[ ]:





# In[ ]:


**** Introduction to Dictionary Datatype: ****


# In[ ]:


defination : A dictionary is a combination of Key-value pairs.
    
Classification : A dictionary is classified as mutable datatype.

How to define a dictionary...? {} ------> Curly brackets Or Flower Brackets


# In[ ]:





# In[ ]:


Note : its the most widely used datatype across the applications.


# In[ ]:





# In[17]:


alien = {'color': 'green', 'points': 5}


# In[21]:


print(alien)


# In[ ]:


Note : In dictionary we can use keys to access the data.


# In[19]:


alien['color']  ##key ------>value


# In[20]:


alien['points']


# In[23]:


fruit = {'apple':'100','banana': 50}


# In[27]:


print(fruit)


# In[29]:


fruit['banana']


# In[30]:


fruit['apple']


# In[ ]:




