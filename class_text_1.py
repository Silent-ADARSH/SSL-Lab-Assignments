#!/usr/bin/env python
# coding: utf-8

# In[1]:


#program to add two numbers
a=10
b=20
print("Sum of the two numbers is ", (a+b))


# In[5]:


#This is a single line comment


# In[6]:


'''This is a multiline comment option 1'''
"""This is a multiline comment option 2"""


# In[4]:


#This is a function defining
def sum():
    a=10
    b=20
    c=a+b
    return c
print(sum())


# In[11]:


def add(x,y):
    """ 
    This is a function taking two numbers and add them 
    and then display The result of the sum and print sum
    """
    c=x+y
    print(c)
    return c
#This goes for single line comment 
def message():
    '''
    This is a message display function used to 
    print welcome message my friends
    '''
    print("Welcome to the python world be like snake and be like a cunning hunter who captures it !!!!")
#now call the function
add(10,25)
message()


# ##### Using Type command

# In[20]:


print(((int),'name'))


# In[21]:


print(type("Hell"))


# In[22]:


print(type(4.3))


# In[23]:


print(type(4))


# In[24]:


print(type(154818416))


# In[30]:


python -m pydoc -w Untitled.py


# In[ ]:




