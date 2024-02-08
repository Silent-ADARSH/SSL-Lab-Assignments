#!/usr/bin/env python
# coding: utf-8

# #### Name- ADARSH AGRAWAL
# #### Enroll-0801IT221150
# #### Batch-B2

# #                                        LAB ASSIGNMENT 2

# ### Q1)Create an empty object. Display it’s data type?

# In[7]:


class EmptyObject:
    pass
instance = EmptyObject()
print(type(instance))


# ### Q2) Write a Python program which add five complex number. Display the sum ?
# 

# In[4]:


a=10+0j
b=5+6j
c=10+4j
d=12+1j
e=0+0.5j
f=complex(a+b+c+d+e)
print(f)


# ### Q3 Write a python program to create the complex numbers from the following integers:
# ### i) a = 10
# ### ii) a =5 b=-2
# ### iii) a = 3.5 b = 6.4
# ### iv) a = -6 b =7.2
# ### v) a =8 b =-4

# In[5]:


#1
a=10
x=complex(a)
print(x)


# In[8]:


#2
a=5
b=-2
y=complex(a,b)
print(y)


# In[9]:


#3
a=3.5
b=6.4
z=complex(a,b)
print(z)


# In[10]:


#4
a=-6
b=7.2
k=complex(a,b)
print(k)


# In[11]:


#5
a=8
b=-4
k=complex(a,b)
print(k)


# ### Q4)Write a python program to convert binary number, octal number and hexadecimal number into an integer number. Take five examples of each number.?

# In[4]:


#hexa to decimal
str1 = "1C2"
str2 = "1C3"
str3 = "1C1"
str4 = "1C5"
str5 = "1C4"
n1=int(str1, 16)
n2=int(str2, 16)
n3=int(str3, 16)
n4=int(str4, 16)
n5=int(str5, 16)
print(n1)
print(n2)
print(n3)
print(n4)
print(n5)


# In[5]:


#octal to decimal
str1 = "12"
str2 = "13"
str3 = "11"
str4 = "15"
str5 = "14"
n1=int(str1, 8)
n2=int(str2, 8)
n3=int(str3, 8)
n4=int(str4, 8)
n5=int(str5, 8)
print(n1)
print(n2)
print(n3)
print(n4)
print(n5)


# In[7]:


#binary to decimal
str1 = "1000"
str2 = "1001"
str3 = "1101"
str4 = "1100"
str5 = "1010"
n1=int(str1, 2)
n2=int(str2, 2)
n3=int(str3, 2)
n4=int(str4, 2)
n5=int(str5, 2)
print(n1)
print(n2)
print(n3)
print(n4)
print(n5)


# ### Q5)Write a python program to convert string into decimal number system by using the command int(string, base). Take five examples of each number system?

# In[9]:


str = "1010"
n = int(str, 2)
print(n)


# ### Q6)Q.6 convert a decimal number into binary, octal and hexadecimal number system. Solve five examples of each number system.?

# In[17]:


a1=10
a2=100
a3=1000
a4=10000
a5=100000
#dec to bin conv
b1=bin(a1)
b2=bin(a2)
b3=bin(a3)
b4=bin(a4)
b5=bin(a5)
#dec to oct conv
o1=oct(a1)
o2=oct(a2)
o3=oct(a3)
o4=oct(a4)
o5=oct(a5)
#dec to hex conv
x1=hex(a1)
x2=hex(a2)
x3=hex(a3)
x4=hex(a4)
x5=hex(a5)
#printing the valus:
print("Binary conversions: ")
print("a1 to binary: ", b1)
print("a2 to binary: ", b2)
print("a3 to binary: ", b3)
print("a4 to binary: ", b4)
print("a5 to binary: ", b5)
print("Oct conversions: ")
print("a1 to oct: ", o1)
print("a2 to oct: ", o2)
print("a3 to oct: ", o3)
print("a4 to oct: ", o4)
print("a5 to oct: ", o5)
print("Hexadecimal conversions: ")
print("a1 to hex: ", x1)
print("a2 to hex: ", x2)
print("a3 to hex: ", x3)
print("a4 to hex: ", x4)
print("a5 to hex: ", x5)


# ### Q7)Write a python program to represent False by a string.?

# In[23]:


str1 = "1"
str2 = "12"
print(str1 == str2)


# ### Write a python program to display the output of the following expression
# ### i) True = True
# ### ii) True + False
# ### iii) True – True
# ### iv) True - True

# In[1]:


#1
print(True=True)


# In[26]:


True+False


# In[27]:


True-True


# In[28]:


a=True
print(True)

