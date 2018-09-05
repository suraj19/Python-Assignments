#Date: 26-07-18
#Author: A.Suraj Kumar
#Roll Number: 181046037
#Assignment 7
#Python Program to Find the Smallest Divisor of an Integer.

n=int(input('Enter any Number:'))
a=[]
for i in range(2,n+1):
	if(n%i==0):
		a.append(i)
a.sort()
print('the samllest divisor of given number',+n,'is:',+a[0])
		
		
