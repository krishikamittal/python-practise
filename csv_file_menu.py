

import csv

def CREATE():
    with open('customer.csv', 'w', newline='') as outFile:
        RowWriter = csv.writer(outFile)
        RowWriter.writerow(['BILLNO', 'DATE', 'NAME', 'AMOUNT'])
        billno = input('Enter Bill Number: ')
        date = input('Enter Date (YYYY-MM-DD): ')
        name = input('Enter Customer Name: ')
        amount = input('Enter Amount: ')
        RowWriter.writerow([billno, date, name, amount])
    print("Customer record created successfully!")

def APPEND():
    with open('customer.csv', 'a', newline='') as outFile:
        RowWriter = csv.writer(outFile)
        billno = input('Enter Bill Number: ')
        date = input('Enter Date (YYYY-MM-DD): ')
        name = input('Enter Customer Name: ')
        amount = input('Enter Amount: ')
        RowWriter.writerow([billno, date, name, amount])
    print("Customer record appended successfully!")

def SEARCH(BILLNO):
    found = False
    with open('customer.csv', 'r', newline='') as inFile:
        AllRows = csv.reader(inFile)
        print('BILLNO	DATE	NAME	AMOUNT')
        for row in AllRows:
            if row[0] == BILLNO:
                print(f'{row[0]}	{row[1]}	{row[2]}	{row[3]}')
                found = True
    if not found:
        print('No record found!')

def MODIFY(BILLNO):
    found = False
    newRows = []
    with open('customer.csv', 'r', newline='') as inFile:
        AllRows = csv.reader(inFile)
        for row in AllRows:
            if row[0] == BILLNO:
                print('Old Amount:', row[3])
                row[3] = input('Enter the new Amount: ')
                found = True
            newRows.append(row)
    if found:
        with open('customer.csv', 'w', newline='') as outFile:
            RowWriter = csv.writer(outFile)
            RowWriter.writerows(newRows)
        print('Record updated successfully!')
    else:
        print('No record found!')

def menu():
    while True:
        print('\nMENU')
        print('1. Create File')
        print('2. Append Record')
        print('3. Search Record')
        print('4. Modify Record')
        print('5. Exit')
        choice = input('Enter your choice: ')
        
        if choice == '1':
            CREATE()
        elif choice == '2':
            APPEND()
        elif choice == '3':
            billno = input('Enter Bill Number to search: ')
            SEARCH(billno)
        elif choice == '4':
            billno = input('Enter Bill Number to modify: ')
            MODIFY(billno)
        elif choice == '5':
            print('Exiting program...')
            break
        else:
            print('Invalid choice! Please try again.')

menu()
