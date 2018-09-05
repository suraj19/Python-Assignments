#Date: 26-07-18
#Author: A.Suraj Kumar
#Roll Number: 181046037
#Assignment 3
#Python Program to Print all Numbers in a Range Divisible by a Given Number

n= int(input('Enter your Range of Numbers: '))
l= int(input('Enter divisible number: '))
for i in range(1, n):
	if (i%l==0):
		print('Here are the Value Divisible', +l,' by: ',+i)		
		#print(i)		

#print('Here are the Values Divisible by: ',+l)
