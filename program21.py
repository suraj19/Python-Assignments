#Date: 28-07-18
#Author: A.Suraj Kumar
#Roll Number: 181046037
#Assignment 20
#Python Program to Calculate the Number of Upper Case Letters and Lower Case Letters in a String.

str_1= input('Enter your conbination of String: ')
count_1=0
count_2=0
for i in str_1:
	if i.isupper():
		count_1=count_1+1
	if i.islower():
		count_2=count_2+1
print('the count of upper case letters is: ',count_1)
print('the count of lower case letters is: ',count_2)
