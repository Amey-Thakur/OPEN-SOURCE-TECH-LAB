'''
Experiment No.7
Program to illustrate Python-MySQL database connectivity.
RollNo.: 50
Name: AMEY THAKUR
'''
import mysql.connector

#Theory about MySQL and MySQL-Connector-Python

def insert(myc,r,n,a,m,cr,co,sk,c):
    query="insert into Student values("+str(r)+",'"+n+"','"+m+"','"+a+"','"+c+"',"+str(cr)+",'"+sk+"',"+str(co)+")"
    print(query)
    try:
        myc.execute(query)
        myc.execute('commit')
        print('Record inserted successfully..')
    except Exception:
        print('Insertion failed..')
    
def display(mycursor):
    query='select * from Student'
    mycursor.execute(query)
    for i in mycursor:
        print(i)
    
def update():
    pass
def delete():
    pass
def main():
    mydb = mysql.connector.connect(host="localhost",user="ostl",passwd="ostluser")
    mycursor=mydb.cursor()
    mycursor.execute('use ostldb')
    while True:
        print('\t\t\tMENU\n1. Insert.\n2. Display.\n3. Update.')
        print('4. Delete. \n5. Exit.')
        ch=int(input('Enter your choice:: '))
        if ch==5:
            break
        elif ch==1:
            r=int(input('Enter the Roll No:'))
            n=input('Enter The Name:')
            m=input('Enter Mobile No:')
            a=input('Enter The Address:')
            c=input('Enter The Courses:')
            cr=int(input('Enter The Credits:'))
            sk=input('Enter The Skills:')
            co=int(input('Enter The No of Courses:'))
            insert(mycursor,r,n,a,m,cr,co,sk,c)
        elif ch==2:
            display(mycursor)
        elif ch==3:
            update()
        elif ch==4:
            delete()
        else:
            print('Wrong choice...')

        
if __name__=='__main__':
    main()