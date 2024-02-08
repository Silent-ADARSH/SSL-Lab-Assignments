#!/usr/bin/env python
# coding: utf-8

# In[6]:


a= [10 , 20, 30, 40]
a_byte = bytes(a)
print(a_byte)
a_byte[0]=23
print(a_byte[0])


# In[7]:


a= [10 , 20, 30, 40]
a_byte = bytes(a)
print(a_byte)


# In[11]:


str="a"
str="Hello"
str[0]
str[4]


# In[22]:


str = "Hellipads"
for i in  str:
    print(i)


# In[25]:


str1 = "Hekkimori"
str1[1:3]


# In[26]:


str1[-1]


# In[27]:


str1[-2]


# In[30]:


str1[-9]


# In[39]:


str1 = "Hekkimori"
a_byte = [10,20,215]
a_byte = bytes(a_byte)
a_bytearray = bytearray(a_byte)
a_bytearray[0] = 1 
print(a_bytearray[0])


# In[40]:


a_list = [10, 10.5 , 'Hi', True]


# In[41]:


type(a_list)


# In[54]:


a_list[-3:-2]
#slicing in -ve indexing is possible very much


# In[56]:


a_list[0:3]


# In[57]:


a_list[0:-1]


# In[61]:


a_list[-3:-2]


# In[62]:


print(a_list)


# In[ ]:




