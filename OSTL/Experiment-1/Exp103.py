from  array import*
print("------List------")
print("")
l=[12,23,-5,0.8,'python',"CO"] #Creating a list of variable datatypes
print("printing original list",l) #printing list
print("printing first three elements of a list",l[0:3]) #printing first three element
print("printing last element of a list",l[-1]) #printing last element of a list 
print("printing first three element of a list twice",l[0:3]*2) #printing first three elements twice
print("")
print("-----LIST FUNCTIONS-----")
print("")
l1=list(range(1,8)) #creating a list of range 1 to 7
print("List of range 1 to 7",l1)
l1.append(9) #adding 1 element to list which is 9
print("Apppend 9:",l1)
l1.sort(reverse=true)
print("Desending Sort:",l1)
l1.sort()
print("Ascending Sort",l1)
l1.reverse()
print("Reverse:",l1)
l1.sort()
l1.remove(9)
print("Remove 9:",l1)
print("count:",l1.count(5)) #counting the no of element 5
print("max:",max(l1))
print("min:",min(l1))
print("Index of 6:",l1.index(6))
print("-----MATRICES using LIST-----")
print("")
m1=[1,2,3],[4,5,6],[7,8,9]
for r in m1:
    print(r)
print("")
print("-----TUPLE DATATYPES (READ ONLY LIST)-----")
print("")
tpl=(-5,0.8,'python','bj') #creating a tuple
print("Created tuple is ",tpl)
print("Touple elements o to 2 is",tpl[0:2]) #printing first two element of tuple
print("")
print("-----TUPLE FUNCTIONS-----")
tpl2=(1,2,3,4,5,6,7,8,9,0,1) #Creating a tuple2
print("Created 2nd tuple is",tpl2)
print("Length:",len(tpl2))
print("Min:",min(tpl2))
print("Max:",max(tpl2))
print("Count no. of 10's",tpl2.count(10))
print("Reverse Sort:",sorted(tpl2,reverse=true))
print("")
print("-----DICTIONARIES i.e. key:value pair-----")
print("")
d1={'NAME':"CO",'GENDER':"M",'age':"19",'COLLEGE':"AITKTC"} #create dictionary
print("print dicitonary:",d1)
print("")
print("-->Keys:",d1.keys())
print("-->Values:",d1.values())
print("-->Keys and Values:",d1.itmes())
d1.update({'Country':"India"})
print("-->Print updated dictionary:",d1)
#c=sorted(d1.itmes(),key=lambda)#,t:t[1])
#print("-->Sort By values   :",c)
print("-----ARRAYS-----")
print("")
arrays=array('i',[1,2,3,4,5,6,7,8,9,0]) #Create array with integer valyues
print("The Array Element are ")
for i in arrays: #i is element and arrays in array name 
    print(i) #Requires indentation
print("length of array is",len(arrays))
array1=array('u',['a','b','c','d']) #Create array with character values
print("The character Array elements are")
for ch in array1: #i is element and array1 in array name
    print(ch) #Requires indentation


