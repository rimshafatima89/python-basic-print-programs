# write a program to install external model and perform two operations of your interset
# we install numpy modules
# to install modules  used" pip install numpy"
import numpy as np
# np is small name for numpy
# we import first import numpy libraray because python dont know external libraraies
# Creating arrays
a= np.array([1,2,3,4])
# np.array is a special type of container for storing numbers (or other data) in an efficient way.
'''array:An array is a collection of items 
 stored in a single variable, where all the items are of the same type (like all numbers, or all string'''
# Performing math operations
b= np.array([2,4,5,6])
addition = np.add (a,b)
mean = np.mean(a)
subtraction = np.subtract(b,a)
multi = np.multiply(a, b)
divide = np.divide(a, b)
power = np.power(a, b)
# Printing each element of arrays line by line
print("addition(a+b):")
for x in addition:
    print (x)
print("subtraction (b - a):")
for x in subtraction:
    print(x)
print("\nmulti(a*b):")
for x in multi:
    print(x)

print("\nmean of a:")
print("\nPower (a ** b):")
for num in power:
    print(num)
print("\nDivide (a / b):")
for num in divide:
    print(num)