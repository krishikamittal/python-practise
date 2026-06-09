#Program: Demonstration of CSV  File using Menu Based Program and using Python Operations
#Topic: CSV File, Python Operations

import csv                                      

def Create():
    outFile=open('phone.csv','a',newline='')   
    RowWriter=csv.writer(outFile)               
    RowWriter.writerow(['Name','Phone'])        

    for i in range(3):
        Name=input('Enter Name: ')
        Phone=input('Enter Phone Number: ')
        Data=[Name,Phone]
        RowWriter.writerow(Data)                

    outFile.close()


def Display():
    inFile=open('phone.csv','r',newline='\r\n') 
    AllRows=csv.reader(inFile)                  
    print('Name\t\t Phone')
    for aRow in AllRows:                        
        print(aRow[0],'\t\t',aRow[1])            

    inFile.close()


def Search():
    Found=0
    Name=input('Enter the name to be searched: ')
    inFile=open('phone.csv','r',newline='\r\n')
    AllRows=csv.reader(inFile)                 
    print('Name\t\t Phone')
    for aRow in AllRows:
        if aRow[0].lower()==Name.lower():       
            print(aRow[0],'\t\t',aRow[1])
            Found+=1

    if Found==0:
        print('No match found!')
    else:
        print('Total',Found,'match(es) found!')

    inFile.close()


def Modify():
    Found=0
    Name=input('Enter the name to be modified: ')
    inFile=open('phone.csv','r',newline='\r\n') 
    OldRows=csv.reader(inFile)                  
    NewRows=[]
    for aRow in OldRows:                       
        if(aRow[0].lower()==Name.lower()):
            print('Old Phone number is: ',aRow[1])
            aRow[1]=input('Enter the new Phone Number: ')
            Found+=1
        NewRows.append(aRow)
    inFile.close()
    if Found>0:
        outFile=open('phone.csv','w',newline='')
        RowWriter=csv.writer(outFile)           
        RowWriter.writerows(NewRows)            
        outFile.close()
    else:
        print('No match found!')


def Delete():
    Found=0
    Name=input('Enter the name to be modified: ')
    inFile=open('phone.csv','r',newline='\r\n') 
    OldRows=csv.reader(inFile)                 
    NewRows=[]
    for aRow in OldRows:                        
        if(aRow[0].lower()==Name.lower()):
            print('The record ', aRow[0],',',aRow[1],'has been deleted')
            Found+=1
        else:
            NewRows.append(aRow)
    inFile.close()
    if Found>0:
        outFile=open('phone.csv','w',newline='')
        RowWriter=csv.writer(outFile)          
        RowWriter.writerows(NewRows)           
        outFile.close()
    else:
        print('No match found!')
    
Create()
Display()
Search()
Delete()
Display()

