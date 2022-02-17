#Experiment 1. Program 1.1
#Program to implement Comments, Datatypes, Expressions, Input and Output Functions
#Single line comment simply by beginning a line with the hash (#) Charachter, and they are automatically terminated as end of line.
""""
Name: AMEY THAKUR

Comments that span multiple lines - used to explain things in more details - are crested by adding a delimiter (''') on
each end of a comment. Otherwise it is not recommended while developing any application software.
"""
print("hello")
print('Illustration of data type')  
i = 10
f = 24.5
s = 'Hello user'
c = 2+3j    #Complex number
print('Integer value:',i,'\nFloat value:',f,'\nString value:',s,'\nComplex value:',c)
print('Illustration of Expression:')
print('Division is',21/i)   #returns division
print('Quotient is',21//i)  #returns quotient
print('Remainder is',21%i)  #returns remainder
print('Power of 2 to 3:',2**3)  #Can also be written as pow(2,3)
print('Divmod of 5/2', divmod(5,2))
x,y = divmod(5,2)   #divmod method returns two number of pair of numbers consisting quotient and remainder
print('Divmod of 5/2',x,y)
print('Illustration of Input and output function!')
i = int(input('Enter a Integer:'))
f = float(input('Enter a Float:'))
s = input('Enter a String:')
c = complex(input('Enter a Complex:'))
print('Integer value:',i,'\nFloat value:',f,'\nString value:',s,'\nComplex value:',c)

"""
OUTPUT:-
hello
Illustration of data type
Integer value: 10
Float value: 24.5
String value: Hello user
Complex value: (2+3j)
Illustration of Expression:
Division is 2.1
Quotient is 2
Remainder is 1
Power of 2 to 3: 8
Divmod of 5/2 (2, 1)
Divmod of 5/2 2 1
Illustration of Input and output function!
Enter a Integer:10
Enter a Float:7.35
Enter a String:yusuf
Enter a Complex:7+5j
Integer value: 10
Float value: 7.35
String value: yusuf
Complex value: (7+5j)

"""
