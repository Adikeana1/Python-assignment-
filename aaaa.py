# Name: Hassan Ibrahim Adi
#ID no: 26613
#assignment

#write a python functions that takes
#two pafameters (a and b)
#andreturn their sum
#testthefunction with different value
#input
def addtwo(a, b):
	add = a + b
	return add
	
print(addtwo(5,7))
print(addtwo(8, 9))

#create a pyhton function that #calculate the factorial of a function
#of a given number. allow the user
#to input number  and display reslt.

import math

def fact():
	b =  int(input("please, enter a factorial number: "))
	c = math.factorial(b)
	return c
	
print(fact())

#implement a function to check #wether a given number is prime or #not, check the functions with #various numbers to demobstrate #its accuaracy.


	
def prime_or_not(a):
	for i in range(2, a):
		if  a % i == 0:
			print(" its not a prime")
		if a < 1:
			print("it is not a prime")
		if a == 1:
			print("it is a prime number")
	else:
			print(" it is a prime number")
			
			
prime_or_not(3)


#develope a function thpt 
#a list of numbers and return #average. test the function with a #sample list of numbers 

def lst(a: list):
	b = sum(a)/len(a)
	return b
	
a = [1, 2, 3]
print(lst(a))
print(lst(a))