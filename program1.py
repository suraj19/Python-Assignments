#Date: 26-07-18
#Author: A.Suraj Kumar
#Roll Number: 181046037
#Assignment 1
#1. Python Program to Exchange the Values of Two Numbers Without Using a Temporary Variable.

a=int(input("Enter A Value:"))
b=int(input("Enter B Value:"))
def  exchange_values(a,b):	
	a,b=b,a
	print(a)
	print(b)
	return a,b
exchange_values(a,b)
