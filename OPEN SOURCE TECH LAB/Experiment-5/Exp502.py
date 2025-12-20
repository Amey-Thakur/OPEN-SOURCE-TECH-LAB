'''
Program 502 for using lambda with filter, map and reduce functions.
'''
def main():
    while True:
        print('\t\t\tMENU')
        print('1. Lambda with Filter.\n2. Lambda with Map.\n3. Lambda with Reduce.\n4. Quit.')
        ch=int(input('Enter your choice::'))
        if ch==4:
            break
        elif ch==1:
            li=list()
            n=int(input('How many elements you want in list ?: '))
            for i in range(n):
                li.append(int(input('Enter element: ')))
            oddli=list(filter(lambda x: (x%2!=0),li))
            print('List of Odd elements =>',oddli)
        elif ch==2:
            li=list()
            n=int(input('How many elements you want in list ?: '))
            for i in range(n):
                li.append(int(input('Enter element: ')))
            sqrli=list(map(lambda x: x**2,li))
            print('List of Squared elements =>',sqrli)
        elif ch==3:
            pass
        else:
            print('Wrong choice...')
    
if __name__=='__main__':
    main()
