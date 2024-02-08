#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Integer
num_int = 5
print("Integer:", num_int)

# Float
num_float = 3.14
print("Float:", num_float)

# String
text_str = "Hello, Python!"
print("String:", text_str)

# Boolean
bool_val = True
print("Boolean:", bool_val)

# List
my_list = [1, 2, 3, "four", 5.0]
print("List:", my_list)

# Tuple
my_tuple = (10, "eleven", 12.5)
print("Tuple:", my_tuple)

# Dictionary
my_dict = {"name": "John", "age": 25, "city": "New York"}
print("Dictionary:", my_dict)


# In[2]:


def add_numbers(a, b):
    """
    Adds two numbers and returns the result.

    Parameters:
    a (int): The first number.
    b (int): The second number.

    Returns:
    int: The sum of the two numbers.
    """
    return a + b


# In[3]:


print(add_numbers.__doc__)


# In[3]:


def check_even_odd(number):
   
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"

user_input = int(input("Enter a number: "))
result = check_even_odd(user_input)
print(f"The number is {result}.")

