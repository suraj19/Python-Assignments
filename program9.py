#Date: 26-07-18
#Author: A.Suraj Kumar
#Roll Number: 181046037
#Assignment 9
#Python Program to Reverse a Given Number.

n=int(input('Enter any Number:'))
rev=0
reminder=''
while(n>0):
	reminder=n%10
	rev=(rev*10)+reminder
	n=n//10
print(rev) 

