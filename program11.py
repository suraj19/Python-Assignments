#Date: 26-07-18
#Author: A.Suraj Kumar
#Roll Number: 181046037
#Assignment 10
#Python Program to Count the Number of Digits in a Number.

n=int(input("Enter your number:"))
count=0
while(n>0):
	count=count+1
	n=n//10
print(count)

