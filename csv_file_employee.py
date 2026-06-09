#Program: Demonstration of Employee file using CSV File Menu Based Program and using Python Operations
#Topic: CSV File, Python Operations

import csv
def create():
    with open('employee.csv','w',newline='') as outfile:
        writer=csv.writer(outfile)
        writer.writerow(['ECODE','ENAME','SALARY'])
        ecode=input('enter code:')
        ename=input('enter name:')
        salary=input('enter salaray:')
        writer.writerow([ecode,ename,salary])
    print('file created successfulyy!!')

def append():
    with open('employee.csv','a',newline='') as outfile:
        writer=csv.writer(outfile)
        ecode=input('enter code:')
        ename=input('enter name:')
        salary=input('enter salaray:')
        writer.writerow([ecode,ename,salary])
    print('record added to file!')

def display():
    try:
        with open('employee.csv','r',newline='') as infile:
            reader=csv.reader(infile)
            print('ECODE  ENME  SALARY')
            for row in reader:
                print('\t'.join(row))
    except FileNotFoundError:
            print('file not found . create file first!')
create()
append()
display()
