#Program: Demonstration of Phonebook Binary File Menu Based Program and using Python Operations
#Topic:Binary File, Python Operations

import pickle

# To Create the Binary File phone.dat

def Append():
    List=[]
    N=int(input("Enter the number of records you want to add: "))
    for i in range(N):
        Name=input("Enter name of the Person: ")
        PhoneNo=int(input("Enter Phone Number of the Person: "))
        Data=[Name,PhoneNo]
        List.append(Data)
    outFile=open("phone.dat","ab")
    pickle.dump(List,outFile)
    outFile.close()
  
#To Read and Display the Entire Binary File phone.dat    

def Display():
    print("\n")
    try:
        inFile=open("phone.dat","rb")
        try:
            while True:
                List=pickle.load(inFile)
                for R in List:
                    print(R)
        except:
            inFile.close()

    except:
        print("File does not exist!\n")

#To Read and Search an Entry in the Binary File phone.dat        

def Search():
    Found=0
    print("\n\n<< SEARCH MENU >>\n\n")
    print("1. Search by Name.\n")
    print("2. Search by Phone Number.\n")
    Ch=int(input("Enter your choice: "))

    if(Ch==1):
        Name=input("Enter Name of the Person to be searched : ")
    else:
        PhoneNo=int(input("Enter Phone Number of the Person to be searched: "))

    print("\nSearched Result:")
        
    try:
        inFile=open("phone.dat","rb")
        try:
            while True:
                List=pickle.load(inFile)
                for L in List:
                    if (Ch==1 and Name==L[0]):
                        print(L)
                        Found=1
                    elif(Ch==2 and PhoneNo==L[1]):
                        print(L)
                        Found=1
        except:
            inFile.close()

    except:
        print("File does not exist!\n")
        
    if(Found==0):
        print("No Match Found!")
                 
# To Search and Modify an Entry in the Binary File phone.dat        

def Modify():
   
    print("\n\n<< MODIFY MENU >>\n\n")
    print("1. Modify by Name.\n")
    print("2. Modify by Phone Number.\n")
    Ch=int(input("Enter your choice: "))

    if(Ch==1):
        Name=input("Enter Name of the Person to be modified: ")
    else:
        PhoneNo=int(input("Enter Phone Number of the Person to be modified: "))

    newList=[]

    try:
        inFile=open("phone.dat","rb")
        try:
            while True:
                List=pickle.load(inFile)
                for L in List:
                    newList.append(L)
        except:
            inFile.close()

    except:
        print("File does not exist!\n")
        newList=[]

    Found=False
    for i in range(len(newList)):
        if (Ch==1 and Name==newList[i][0]):
            Found=True
            PhoneNo=newList[i][1]
            newPhoneNo=int(input("Enter the Modified Phone Number of the Person: "))
            newList[i][1]=newPhoneNo
            print("Phone number of ",newList[i][0]," has been modified from ", PhoneNo, " to ",newPhoneNo,"\n")
            break
        elif(Ch==2 and PhoneNo==newList[i][1]):
            Found=True
            Name=newList[i][0]
            newName=input("Enter the Modified Name of the Person: ")
            newList[i][0]=newName
            print(Name," has been modified as ",newName)
            break


    if(Found):
        outFile=open("phone.dat","wb")
        pickle.dump(newList,outFile)
        outFile.close() 
    else:
        print("No Match Found!")
    

# To Search and Delete an Entry in the Binary File phone.dat  

def Delete():
    print("\n\n<< DELETE MENU >>\n\n")
    print("1. Delete by Name.\n")
    print("2. Delete by Phone Number.\n")
    Ch=int(input("Enter your choice: "))

    if(Ch==1):
        Name=input("Enter Name of the Person to be deleted: ")
    else:
        PhoneNo=int(input("Enter Phone Number of the Person to be deleted: "))

    newList=[]

    try:
        inFile=open("phone.dat","rb")
        try:
            while True:
                List=pickle.load(inFile)
                for L in List:
                    newList.append(L)
        except:
            inFile.close()

    except:
        print("File does not exist!\n")
        newList=[]

    Foundindex=-1
    for i in range(len(newList)):
        if (Ch==1 and Name==newList[i][0]):
            Foundindex=i
            print("The record ",newList[i]," has been deleted")
            break
        elif(Ch==2 and PhoneNo==newList[i][1]):
            Foundindex=i
            print("The record ",newList[i]," has been deleted")
            break


    if(Foundindex>-1):
        newList.pop(Foundindex)
        outFile=open("phone.dat","wb")
        pickle.dump(newList,outFile)
        outFile.close() 
    else:
        print("No Match Found!")

# Main Menu with Choices
def Menu():
    Choice=0
    while(Choice!=6):
        print("\n\n\n")
        print("<<<<<<< BINARY FILE >>>>>>>\n")
        print("<< TELEPHONE DIRECTORY >>\n")
        print("<<<<<<< MAIN MENU >>>>>>>\n\n")
        print("1. Append a Fresh Entry.\n")
        print("2. Display Entire File.\n")
        print("3. Search an Entry.\n")
        print("4. Modify an Entry.\n")
        print("5. Delete an Entry.\n")
        print("6. Quit Program.\n\n")
        Choice=int(input("Enter your choice: "))
        if (Choice==1):
            Append()
        elif (Choice==2):
            Display()
        elif (Choice==3):
            Search()
        elif (Choice==4):
            Modify()
        elif (Choice==5):
            Delete()
        elif (Choice==6):
            print("\n\n\nThank you for using this software!\n\n\n")
        else:
            print("Invalid Input! Try AGain!")
    
Menu()

