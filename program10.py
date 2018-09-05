#Date: 26-07-18
#Author: A.Suraj Kumar
#Roll Number: 181046037
#Assignment 10
#Python Program to Calculate the Average of Numbers in a Given List.

n=int(input("Enter the number of elements to be inserted: "))
a=[]
for i in range(0,n):
    m=int(input("Enter element(press enter after insertion): "))
    a.append(m)
avg=sum(a)/n
print("Average of elements in the list",avg)

