#Date: 30-07-18
#Author: A.Suraj Kumar
#Roll Number: 181046037
#Python Program to generate 5 random integers between 1 to 20 such that numbers should be unique.

import random
a=[]
n=int(input('Enter the range of random number: '))
for i in range(0,n):
	j=random.randint(1,20)
	if j not in a:
		a.append(j)	
print('list of random numbers:',a)




