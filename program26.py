#Date: 30-07-18
#Author: A.Suraj Kumar
#Roll Number: 181046037
#Python Program to generate 10 random integers between 1 to 20 (both inclusive).

import random
a=[]
n=int(input('Enter the range of random number: '))
for i in range(10):
	a.append(random.randrange(1,20))
print('list of random numbers:',a)




