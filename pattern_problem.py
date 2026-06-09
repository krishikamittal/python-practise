#Program: Demonstration of Pattern using Python Operations
#Topic: Python Operations

def Pattern(N):
    for i in range(1,1+N):
        for j in range(1,N-i):  
            print(' ',end='')
        for j in range(i,1,-1):
            print(j,end='')
        for j in range(1,i+1):
            print(j,end='')
        print()

Pattern(4)



