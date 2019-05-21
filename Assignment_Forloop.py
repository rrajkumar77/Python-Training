#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 20 15:01:57 2019

@author: admin
"""

import numpy as np

'''
1. Create a list of birth years of 5 friends/family member (e.g: br_yr = [1986, 1989, 1975, 1981,
1978]). Calculate their age (years alone) as of Dec 31, 2017 using 3 approaches and save it a list.
 Regular for loops
 List comprehension
 Vectorized operation using numpy array
'''

# Regular for loops
br_yr = [1986, 1989, 1975, 1981,1978]  
age_yr= [0]*len(br_yr)
for i in range(len(br_yr)):
    age_yr[i] = 2017 - br_yr[i]
print(age_yr)

#List comprehension
age_yr1 = [2017 - i for i in br_yr]

# Vectorized operation using numpy array
age_yr2 = [2017 - np.array(br_yr)]


'''
2. Create a string “this is a python exercise which is neither too easy nor too hard to be solved in
the given amount of time”. 
Split the string to list of individual words [Hint: split command. Don’t
search in classwork]. 
Remove words like ‘a’ 'is’, ‘and ‘the’ programmatically using 3 approaches
 Regular for loops
 List comprehension
 Vectorized operation using numpy array
'''

# Regular for loops
Str = ("this is a python exercise which is neither too easy nor too hard to be solved in the given amount of time")
str_lst = Str.split()
rem = [0]*len(str_lst)
for i in range (len(str_lst)):
    remove = {"is", "a","the"}
    rem_wrd = [ele for ele in str_lst if ele not in remove] 
print (rem_wrd)    
    
#List comprehension
rem_wrd = [ele for ele in str_lst if ele not in remove] 

# Vectorized operation using numpy array
str_arr= np.array(str_lst)
np.setdiff1d(str_arr,remove)


