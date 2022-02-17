'''
Program 501 for performing operations on file.
'''

def readf():
    try:
        flag=False
        f=open(input('Enter filename: '))
        flag=True
        s=f.readlines()
        for l in s:
            print(l,end='')
    except FileNotFoundError:
        print('File does not exist.')
    except OSError as e:
        print('System Error:',e)
    finally:
        if flag:
            f.close()

def writef():
    f=open(input('Enter filename: '),'w+')
    while True:
        data=input('Enter Data: ')
        f.write(data+'\n')
        ch=input('Want to enter more data (y/n)?: ')
        if ch=='n' or ch=='N':
            break
    f.close()

def appendf():
    pass

def main():
    while True:
        print('\t\t\tMENU')
        print('1. Display.\n2. Write.\n3. Append.\n4. Quit.')
        ch=int(input('Enter your choice::'))
        if ch==4:
            break
        elif ch==1:
            readf()
        elif ch==2:
            writef()
        elif ch==3:
            appendf()
        else:
            print('Wrong choice...')
    
if __name__=='__main__':
    main()
