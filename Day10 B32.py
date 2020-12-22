#!/usr/bin/env python
# coding: utf-8

# In[ ]:


Introduction to Functions:


# In[ ]:


code reusability : 


# In[ ]:


Defination : When we need to have our own custom requirement fullfilled, we can able to design out functions.

How to define a function :----> By using the keyword called as def
    
Note: Always use small case names for defining the function names.
    


# In[ ]:





# In[ ]:


Req: Design a function to greet


# In[2]:


## Declaring the function OR Defining the function !! ##

def greet():  ## it should be in the small case letters !!!
    'creating a function to greet'   ## Doc String ---> Commenting inside the function
    print('Hello')


# In[3]:


greet()  ## Function call


# In[4]:


def green():
    "creating a functon to green"
    print("color")


# In[5]:


green()


# In[ ]:





# In[ ]:


Req : i want to greet a person..


# In[8]:


def greetuser(user):  ## Passing same info to the function  ## parameter Passing
    "creating the function for greeting the user"
    print(f"Hello, Welcome to AWS, {user}")


# In[9]:


greetuser('Abid sheikh')  ## Passing same info to the function call ## Argument passing


# In[10]:


greetuser('Rachana')


# In[ ]:





# In[ ]:


Introduction to types of arguments:


# In[ ]:


Req: Define a function called lets say describe_pet
    
    pass the below parameters to the above defined function, animal_type, pet_name.

##()-----> Called as paranthesis


# In[24]:


## Declaring the function as per the above requirement

def describe_pet(animal_type,pet_name):  ## params ## parameters!!
    "creating a function to capture information about the pets"
    print(f'I have a {animal_type}')
    print(f"my {animal_type}'s name is {pet_name}")     


# In[25]:


##function call

describe_pet('dog',"bruno")  ## Arguments passing!!


# In[29]:


def describe_pet(animal_type,pet_name):  ## params ## parameters!!
    "creating a function to capture information about the pets"
    print(f'I have a {animal_type}')
    print(f"my {animal_type} name is {pet_name}") 


# In[30]:


describe_pet('Tiger',"Sultan")  ## maintain the same position OR else you will get errors!!


# In[ ]:


1. position arguments ... by default function will be accepting the positoinal arguments..


# In[ ]:


keyword arguments....!


# In[31]:


describe_pet(pet_name = 'Tommy', animal_type = "Dog")


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




