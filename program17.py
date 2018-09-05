#Date: 28-07-18
#Author: A.Suraj Kumar
#Roll Number: 181046037
#Assignment 10
#Python Program to Count the Number of Vowels in a String.

str_1=input('Enter a string:')
count=0
for i in str_1:
	if (i=='a'or i=='e'or i=='i'or i=='o' or i=='u'):
		count=count+1
print(count)
