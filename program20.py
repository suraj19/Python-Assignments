#Date: 28-07-18
#Author: A.Suraj Kumar
#Roll Number: 181046037
#Assignment 20
#Python Program to Take in Two Strings and Display the Larger String without Using Built-in Functions.

str_1=input('Enter your first String: ')
str_2=input('Enter your second String: ')
count_1=0
count_2=0
for i in str_1:
	count_1=count_1+1
for j in str_2:
		count_2=count_2+1
if (count_1>count_2):
	print(str_1)
else:
	print(str_2)
