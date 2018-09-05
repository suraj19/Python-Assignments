#Date: 30-07-18
#Author: A.Suraj Kumar
#Roll Number: 181046037
#Python Program to generate 10 random numbers between 1 to 100 such that there should one number between 1 to 10 one number between 11 to 20 etc.

import random
a=[]
r=random.randint(1,10)
a=random.sample(range(1,100,10),10)
a.sort()
print(a)



