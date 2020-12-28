#!/usr/bin/env python
# coding: utf-8

# In[ ]:


Continuatin to functions:


# In[ ]:


Recap :  What are functions
         1. How to define function
         2. function call
            
    -----> Parameters
    -----> Arguments
    
Type of Arguments

    -----> Positional arguments
    -----> Keyword arguments  
        


# In[ ]:





# In[13]:


def describe_pet(animal_type, pet_name):
    'creating the function to describe the pets'
    print(f'I have a {animal_type}')
    print(f'My {animal_type}s name is {pet_name}')


# In[14]:


describe_pet('cat', "snowbell")


# In[4]:


describe_pet('rose')  ## Need to give to arguments


# In[ ]:


## Default argumetns:


# In[ ]:


## Pet_name for sure

## animal_type info we will be missing sometime.-----> in case of missing info assure the animal_type is a dog..


# In[5]:


def describe_pet(animal_type = 'dog', pet_name):
    'creating the function to describe the pets'
    print(f'I have a {animal_type}')
    print(f'My {animal_type}s name is {pet_name}')


# In[ ]:


Note : Always keep the default argument at the last.


# In[9]:


def describe_pet(pet_name,animal_type = 'dog'):
    'creating the function to describe the pets'
    print(f'I have a {animal_type}')
    print(f'My {animal_type}s name is {pet_name}')


# In[10]:


describe_pet('rose')


# In[8]:


describe_pet('peacock', 'bird')


# In[ ]:





# In[16]:


def make_pizza(toppings):
    "creating the make pizza function and choosing the toppomgs on top of it"
    print(toppings)


# In[17]:


make_pizza('corn')


# In[18]:


make_pizza('olives','onion')


# In[19]:


make_pizza('chicken', 'olivves',"extracheese")


# In[20]:


def make_pizza(*toppings):  ## * ----> assertedrisk
    'creating the make pizza function and chossing the toppings on top of it'
    print(toppings)
  


# In[24]:


make_pizza('chicken', 'olives', 'extracheese') ## Arbitary arguments


# In[ ]:


Type of arguments:
    
    Positional arguments
    Keyword arguments
    default arguments
    arbitary arguments


# In[ ]:





# In[ ]:


Introduction to python classes:


# In[ ]:


Things to know:
    1. Class
    2. methods
    3. attributes
    4. self
    5. object
    


# In[ ]:


class ----> It is a high level design of the program.

we have to use the keyword called "class" to define the class.

naming convention ----> use title case for declaring the class name.


Ex : 
    
    class: Test


# In[ ]:


Methods : A function written inside the class is called as method.
    
Attribute : A variable written inside the class is called as an attribute.
   
Self : A self is a temprory placeholder for an object
    
Object : It is an access point for entering in to the or access in the class methods...!!    


# In[ ]:





# In[ ]:




