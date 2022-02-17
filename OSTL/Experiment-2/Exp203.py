'''
EXPERIMENT No. : 2
Name : AMEY THAKUR

Aim : Program to implement Functions in Python.
'''

'''
A function is a set of statements that take inputs, do some specific computation and produces output.
SYNTAX:
def FUNCTION_NAME():
  ARGUMENTS
'''

def fact(n):
    """FUNCTION TO RTURN FACTORIAL VALUE OF GIVEN INTEGER"""
    if(type(n)==int):
        f=1
        for i in range(1,n+1):
            f=f*i
        return f
    else:
        return'CANNOT FIND THE FACTORIAL OF NON-INTEGER INPUT'

def fibo(n):
    """FUNCTION TO RETURN LIST OF FIBONACCHI SERIES OF GIVEN INTEGER"""
    l = list()
    l.append(0)
    l.append(1)
    while (l[-1]+l[-2] <= n):
        l.append(l[-1]+l[-2])
    return l

def chkprime(n):
    """FUNCTION TO CHECK THE PRIMALITY OF A GIVEN INTEGER"""
    for i in range(2,n//2+1):
        if(n%i==0):
            return False
    return True  

def sumfibo(n):
    l = fibo(n)
    sum = 0
    for i in l:
        sum+=i
    return sum

while True:
    print('\t\t\tMENU\n1. FACTORIAL OF A GIVEN NUMBER\n2. FIBONACCI OF GIVEN NUMBER\n3. SUMMATION OF FIBONACCI\n4. PRIMALITY\n0. EXIT')
    ch = int(input('ENTER YOUT CHOICE: '))
    if ch in range(1,5):
        n = int(input('ENTER THE NUMBER: '))
    if ch == 1:
        print('FACTORIAL OF',n,'IS',fact(n))
    elif ch == 2:
        print('FIBONACCI SERIES TILL',n,'IS',fibo(n))
    elif ch == 3:
        print('SUMMATION OF FIBONACCI SEIES TILL',n,'IS',sumfibo(n))
    elif ch == 4:
        print('PRIMALITY OF',n,'IS',chkprime(n))
    elif ch == 0:
        break
    else:
        print('ENTER A VALID INPUT!')