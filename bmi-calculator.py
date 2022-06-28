#!/usr/bin/env python
# coding: utf-8

# In[1]:


print("Welcome to the BMI Calculator\n")

height = input("Enter your height in m: ")
weight = input("Enter your weight in kg: ")

new_height = float(height)
new_weight = int(weight)

BMI = (new_weight / new_height ** 2)
new_BMI = str(BMI)

print("Your BMI is " + new_BMI) 

