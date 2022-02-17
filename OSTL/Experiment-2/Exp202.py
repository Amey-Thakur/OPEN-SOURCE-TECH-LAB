'''
EXPERIMENT No. : 2
Name : AMEY THAKUR

Aim : Program to implement FOR & WHILE loop.
'''

n=int(input('ENTER A NUMBER: '))

'''
FOR loop is used to execute a set of statements, once for each item in a list, tuple, set etc.
SYNTAX:
for variable in sequence:
    ARGUMENTS
'''

f=1
for i in range(1,n+1):
    f=f*i
print('FACTORIAL OF',n,'IS: ',f)

'''
WHILE loop can be used to execute a set of statements as long as a condition is true.
while (CONDITION):
    ARGUMENTS
'''

a,b=0,1
c=a+b
print('FIBONACCI SERIES TILL',n,'IS: ',a,b,end=' ')

while (c<=n):
    print(c,end=' ')
    a,b=b,c
    c=a+b
print(' ')