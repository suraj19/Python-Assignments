#Date: 26-07-18
#Author: A.Suraj Kumar
#Roll Number: 181046037
#Assignment 6
#Python Program to Read a number n and Compute n+nn+nnn.


n=int(input("Enter your value:"))
m=int(input("Sequence Number:"))
str_1= str(n)
sum_1= n
str_2=''
for i in range(1,m):
	str_2= str_2+str_1
	str_2= str(n)  #intialising a result as a sting
	sum_1= sum_1+int(str_2) #converting string back to integer
	print(sum_1)	


