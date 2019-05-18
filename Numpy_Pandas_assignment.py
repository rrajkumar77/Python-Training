#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 17 14:30:57 2019

@author: admin
"""

## ASSIGNMENT 1 - Numpy pandas
## DATAFRAME SLICING

# Slice the following
# Maths column

import numpy as np
import pandas as pd

math_score_array = np.array([95,67,88,45,84])
eng_score_array = np.array([32,67,45,39,67])
gender_array = np.array(["M","M","F","M","F"])

math_column = math_score_array

# Maths and English Column
math_eng_column = {"Maths": math_score_array,
              "English": eng_score_array}


# "Maths" column of "R1001"


score_dict = {"Maths": math_score_array,
              "English": eng_score_array,
              "Gender": gender_array}

df_score = pd.DataFrame(score_dict,index = ["R1001","R1002","R1003","R1004","R1005"])


df_score.loc["R1001","Maths"]

# "Maths" and English column values of "R1001" and "R1003"

df_score.loc[["R1001","R1002"], ["Maths","English"]]


# All rows, 2nd column

df_score.loc[:,["English"]]

# 0th and 3rd row, 0th and 1st 
df_score.iloc[[0,3],[0,1]]


# data frame of Male students alone
cond = df_score["Gender"] == "M"
df_male = df_score[cond]

# english and maths score of Male students
cond1 = df_score["Gender"] == "M"
df_male_engmat = df_score.loc[cond1,["Maths","English"]]                      


# all columns of students who score above 70 in Maths

cond2 = df_score["Maths"]>70
all_70 = df_score[cond2]

# average maths score of students who got above 60 in English

cond3 = df_score["English"]>60
math = df_score.loc[cond3,["Maths"]]
np.mean(math)

# average english score of students who are above average in maths

math1 = df_score["Maths"]
cond4 = df_score["Maths"]>np.mean(math1)
engval = df_score.loc[cond4,["English"]]
np.mean(engval)


# all columns of male students who scores above 60 in maths
maths60 = df_score["Maths"]>60
male60 = df_score.loc[maths60 & cond]
           
"""
slice english and gender column of either 
female students or students with maths score above 60
"""
enggen = df_score.loc[maths60,["English","Gender"]]


# Assignment 2 Numpy pandas

# Creating Data frame 
#Option 1:
arr = np.random.randint(10,100,100)
r_arr = np.reshape(arr,[25,4])
df = pd.DataFrame({'A' : r_arr[:,0],'B':r_arr[:,1],'C' : r_arr[:,2],'D':r_arr[:,3]})
df.index +=1001

#Option 2:
df1 = pd.DataFrame(np.random.randint(10,100,size=(25, 4)), columns=list('ABCD'))
df1.index +=1001

#1. Slice column ‘A’ from df and save it as a series ‘s’
s =  df.iloc[:,0]
s1 = df.A
type(s)
type(s1)

sliA=df1.A
type(sliA)

#2. Slice column ‘A’ and column ‘C’ and save it as df2

df2 = df[['A','C']]
type(df2)

sliac=df1[['A','C']]

#tocheck
df.iloc["A","C"]

#3. Slice 0th and 2nd column using column number and save it as df3
df3 = df1.iloc[:,[0,2]]

#4. Slice from 0 till 5th position in series ‘s’
s[0:5] 

#5. Slice all columns from rows 3 till 19 and save it as df4
df4 = df1.iloc[3:19]

#6. Create df5 which has subset of data from df where column A values are above median of
#column A. Note: slice entire columns based on condition on column A

#Option 1
condA = np.median(df1.A)
condB = df1.A>condA
df5 = df1.A[condB]

#Option2
condC = df1.A > np.median(df1.A)
df7 = df1.A[condC]
