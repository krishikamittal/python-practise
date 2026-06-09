import csv                                  

outFile=open('phone.csv','w',newline='')

RowWriter=csv.writer(outFile)              
RowWriter.writerow(['Name','Phone'])        
ListRows=[]

for i in range(5):
    Name=input('Enter Name: ')
    Phone=input('Enter Phone Number ')
    Data=[Name,Phone]
    RowWriter.writerow(Data)               

outFile.close()

inFile=open('phone.csv','r',newline='\r\n')

ListRows=csv.reader(inFile)                 

for aRow in ListRows:
    print(aRow[0]," - ",aRow[1])           

inFile.close()
