#Date: 28-07-18
#Author: A.Suraj Kumar
#Roll Number: 181046037
#Assignment 20
#Python Program to Calculate the Number of Digits and Letters in a String.

str_1=input('Enter a String:')
count_1=0
count_2=0
for i in str_1:
	if i.isdigit(): 
		count_1=count_1+1
	else: 
		i.isalpha()
		count_2=count_2+1
print('The number of Digits in Sting is: ',count_1)
print('The number of number in Sting is: ',count_2)
