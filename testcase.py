                                                                                                                                                                                                                                                                                     #Date: 08-07-18
#Author: A.Suraj Kumar
#Roll Number: 181046037
#Assignment 1
#Testcases

#1.
import program1
'''def exchange_values(a,b):
	a,b=b,a
	return a,b
	exchange_values(10,20)'''
assert(program1.exchange_values(10,20)==(20,10))
#2.
def isPositiveNumber(Num):
	return num>-1
	assert(PositiveNumber(10)==True)


#3.
def Divisible(n,l):
	for i in range(1, n):
		if (i%l==0):
			return i
	assert(Divisible(5,8))
	
#4.
def Rem(n,l):
	i=n/l
	j=n%l
	assert(Rem(5,9))
	
#5.
def odd(n):
	i%2!=0
	return i
	assert(odd(50))
#6.
def SumD(n):
	A=n%10
	a=a+A
	n=n//10
	return a
	assert(SumD(n))
#7.
def SamDiv(n):
	a=[]	
	for i in range(2,n+1):
		if(n%i==0):
			a.append(i)
	a.sort()
	return a[0]
	assert(SamDiv(5))
#8.
def compute(n,m):
	for i in range(1,m):
		str_2= str_2+str_1
		str_2= str(n)  
		sum_1= sum_1+int(str_2) 
	return sum_1
	assert(compute(10,30)) 
#9.
def reverse(n):
	rev=0
	while(n>0):
		reminder=n%10
		rev=(rev*10)+reminder
		n=n//10
	return n
	assert(reverse(159))
#10.
def Avarage(a,n):
	a=[]
	for i in range(0,n):
    		m=int(input("Enter element(press enter after insertion): "))
    		a.append(m)
	avg=sum(a)/n
	return avg
	assert(avarage(10,7))



