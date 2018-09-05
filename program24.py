#Date: 28-07-18
#Author: A.Suraj Kumar
#Roll Number: 181046037
#Assignment 24
#Python Program to sum of a list [1, 2, 4, …] is defined as  [1, 3, 7, . . .] Write a function cumulative_sum() to compute cumulative sum of a list


a=[]
n= int(input("Enter the number of elements in list:"))
for x in range(0,n):
    element=int(input("Enter element" + str(x+1)+':'))
    a.append(element)
b=[sum(a[0:x+1]) for x in range(0,len(a))]
print("The original list is: ",a)
print("The new list is: ",b)
