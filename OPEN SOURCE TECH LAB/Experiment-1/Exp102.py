#Experiment 1,program 1.2
#program to implement byte array ,range ,set and string function
#bytearrays
b= bytearray(3)
print('Byte arrays:',b[0],b[1],b[2])    #bytearray() method returns the mutable object which is a mutable sequence of integers in range 0 <=X <= 250
c= b'Hello'
print(c)
print(type(c))  #type() method returns class type of the argument in object

#Range
print('Illustrating range:')
r = range(10)   #range() function returns an immutable sequence object of integers.
print(r[0], r[9])
r = list(range(10 , 20))
print(r)

#set
print('Illustration set')
s1 = {1,2,3}
s2 = {3,4,5,6}
print('Intersection of s1 and s2',s1.intersection(s2))  #intersection() method returns two given sets is the largest set which contains all the elements that are common to both the sets.
print('IS', s1.union(s2),'superset of',s1,' ',s1.union(s2).issuperset(s1))  #The issuperset() method returns True if all elements of a set A occupies set B which is passed as an argument and returns false if all elements of B not present in A

#String Functions
print('Illustration String functions:')
s = input('Enter a string:')
sub = input('Enter aa substring:')
print('Reverse of the string :',s[::-1])
print('Is ', sub,'Substring of :',s, ' ', sub in s)
print('Uppercased:', s.upper())

""""
OUTPUT:-
Byte arrays: 0 0 0
b'Hello'
<class 'bytes'>
Illustrating range:
0 9
[10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
Illustration set
Intersection of s1 and s2 {3}
IS {1, 2, 3, 4, 5, 6} superset of {1, 2, 3}   True
Illustration String functions:
Enter a string:sahil
Enter aa substring:yusuf
Reverse of the string : lihas
Is  mulani Substring of : mohd   False
Uppercased: YUSUF

""""
