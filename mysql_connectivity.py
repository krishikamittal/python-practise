#Program: Demonstration of MySQL Connectivity  using Python Operations
#Topic: Python Operations

import mysql.connector as SQL                                        

MyDB=SQL.connect(host='localhost', user='root', password='modern')
if (MyDB.connection_id is not None):
    print('MySQL connectivity established!')


def Create():
    MyDB=SQL.connect(host='localhost', user='root', password='modern')
    MyCursor=MyDB.cursor()                                            

    try:
        MyCursor.execute("CREATE DATABASE PHONEBOOK;")               
    except:
        print('Database cration error!')
        
    try:                                                              
        MyCursor.execute("USE PHONEBOOK;")                            
        MyCursor.execute("CREATE TABLE MYCONTACTS (NAME VARCHAR(100), MOBILENO VARCHAR(15));")
    except:
        print('Table cration error!')


def Append():                                                         
    MyDB=SQL.connect(host='localhost', user='root', password='modern',database='PHONEBOOK')
    MyCursor=MyDB.cursor()                                           
    
    print('Enter the details of a row: ')
    Name=input('Enter Name: ')
    Phone=input('Enter Phone Number: ')
    Data=(Name,Phone)                                                 

    Command="INSERT INTO MYCONTACTS VALUES (%s,%s);"                
    MyCursor.execute(Command,Data)                                    
    
    MyDB.commit()                                                     
    

def Display():                                                       
    MyDB=SQL.connect(host='localhost', user='root', password='modern',database='PHONEBOOK')
    MyCursor=MyDB.cursor()                                            
    
    MyCursor.execute("SELECT * FROM MYCONTACTS;")                     

    print('Name\t\t Phone')

    AllRow=MyCursor.fetchall()                                       
    for aRow in AllRow:
        print(aRow[0],'\t\t',aRow[1])

    print('\nTotal rows:',MyCursor.rowcount)                          

   
def Search():
    Found=0
    Name=input('Enter the name to be searched: ')
                                                                      
    MyDB=SQL.connect(host='localhost', user='root', password='modern',database='PHONEBOOK')
    MyCursor=MyDB.cursor()                                            
                                                                     
    MyCursor.execute("SELECT * FROM MYCONTACTS WHERE NAME = %s ;",(Name,)) 

    print('Name\t\t Phone')
    while True:
        aRow=MyCursor.fetchone()                                     
        if aRow==None:
            break
    
        print(aRow[0],'\t\t',aRow[1])

    print('\nTotal matches:',MyCursor.rowcount)                       


def Modify():
    Found=0
    Name=input('Enter the name to be modified: ')
    Phone=input('Enter the modified Phone Number: ')
                                                                     
    MyDB=SQL.connect(host='localhost', user='root', password='modern',database='PHONEBOOK')
    MyCursor=MyDB.cursor()                                            
                                                                      
    MyCursor.execute("UPDATE MYCONTACTS SET MOBILENO = %s WHERE NAME = %s ;",(Phone,Name))                     
    MyDB.commit()                                                     

   
def Delete():
    Found=0
    Name=input('Enter the name to be deleted: ')
                                                                      
    MyDB=SQL.connect(host='localhost', user='root', password='modern',database='PHONEBOOK')
    MyCursor=MyDB.cursor()                                            
                                                                      
    MyCursor.execute("DELETE FROM MYCONTACTS WHERE NAME = %s ;",(Name,))                    
    MyDB.commit()                                                    
    
    
Create()
Append()
Append()
Display()
Search()
Modify()
Display()
Delete()
Display()

