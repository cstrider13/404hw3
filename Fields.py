
# coding: utf-8

# In[13]:

from sympy import *

def Fields():
    n = int(input("Enter a number: "))
    if(isprime(n) == true):
        print("field")
        return
    
    x_good = 1
    z_good = 0
    for x in range(1, n):
        for z in range(1, n):#Skip 0 because this rule doesn't include 0
            if((x*z) % n == 1):
                z_good = 1
            else:
                x_good = 0
                print("ring")
                return
    if(x_good == 1):
        print("field")
        return
Fields()


# In[ ]:



