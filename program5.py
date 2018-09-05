#Date: 26-07-18
#Author: A.Suraj Kumar
#Roll Number: 181046037
#Assignment 5
#Python Program to Print Odd Numbers Within a Given Range.


n= int(input("Enter a range for Odd Numbers: "))
n=n+1
for i in range(0, n):
	if (i%2!=0):
		print('Odd Integers:', +i)	
