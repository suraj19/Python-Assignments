#Date: 26-07-18
#Author: A.Suraj Kumar
#Roll Number: 181046037
#Assignment 6
#Python Program to Find the Sum of Digits in a Number.


n=int(input("Enter a number:"))
a=0
while(n>0):
    A=n%10
    a=a+A
    n=n//10  #floor division of operands 
print("The total sum of digits is:",a)
