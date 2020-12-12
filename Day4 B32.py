#!/usr/bin/env python
# coding: utf-8

# In[ ]:


### Adding whitespaces to strings ###


# In[1]:


print('fav_languagues:pytonc++pascalcobaljavaruby')


# In[ ]:


### \n ------> is the new line delimiter ###


# In[2]:


print('fav_languagues:\python\nc++\npascal\ncobal\njava\nruby')


# In[4]:


print('fav_languagues:\n\tpython\n\tc++\n\tpascal\n\tcobal\n\tjava\n\truby') ### \t ---> 4 lines tab delimiter


# In[ ]:





# In[ ]:


### How TO REMOVE THE WHITESPACE IN PYTHON ###


# In[ ]:





# In[8]:


x = 'python' ### NoStrip 

print(x)


# In[9]:


x = "   python"

print(x)


# In[10]:


x.lstrip()    ### lstrip  


# In[ ]:





# In[12]:


y = 'python  '

print(y)


# In[13]:


y.rstrip()    ### rstrip ----> no search operaton


# In[15]:


z = '  python  '

print(z)


# In[ ]:


z.strip()   ### zstrip ----> 1. search operation 2. it will eliminate


# In[ ]:





# In[ ]:


### INTRODUCTION TO list DATATYPE ###


# In[ ]:


DEFINATION : A list IS A COLLECTION OF ITEMS IN A PARTICULAR ORDER.

Classification : A list has been classified as an mutable datatype. (which we cant change)
    
how do you defind/declare a list ......? [] =====> Square brackets


# In[ ]:





# In[46]:


students = ['abid','joseph','niyaz','vaani','salina','asha','sham']


# In[55]:


print(students)


# In[3]:


type(students)


# In[ ]:





# In[ ]:


Understanding the concept of indexing : 0,1,2,3.....
    
The order of the list is maintained by indexing.....!    


# In[ ]:





# In[ ]:


get_ipython().set_next_input('Req: i want to access niyaz from the above list');get_ipython().run_line_magic('pinfo', 'list')


# In[57]:


print(students[2])


# In[58]:


print(students[2].title())


# In[24]:


print(students[4].title())


# In[ ]:





# In[ ]:


1. how to add new elements to the list...
2. how to edit the elements in the list...
2. how to delete the elements from the list....


# In[ ]:





# In[ ]:


1. how to add new elements to the list...


# In[ ]:


Req: i want to add vinod the above list..?


# In[ ]:


students.append('vinod')


# In[31]:


print(students)


# In[ ]:


Req: i want to add Ram to the above list..?


# In[ ]:


students.append('Ram')


# In[59]:


print(students)


# In[ ]:


Note : append is adding the students at the last place


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




