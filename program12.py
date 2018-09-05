#Date: 26-07-18
#Author: A.Suraj Kumar
#Roll Number: 181046037
#Assignment 12
#Python Program to Check if a Number is a Palindrome.

num = int(input("enter a number: "))
 
temp = num
r = 0
 
while (temp != 0):
    r= (r * 10) + (temp % 10)
    temp = temp // 10
 
if (num == r):
    print("number is palindrome")
else:
    print("number is not palindrome")
