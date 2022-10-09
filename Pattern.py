#!/usr/bin/env python
# coding: utf-8

# In[8]:


for x in 'ABCDE':
    for y in 'ABCDE':
        if y < x:
            print(x, end="")
        else:
            print(y, end="")
        print()

