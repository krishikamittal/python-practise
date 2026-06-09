# Mohandas Karamchand Gandhi  -> 

Name=input("Enter full name of the person: ")

BrokenName=Name.split() #  ["Mohandas", "Karamchand", "Gandhi"]


TN=len(BrokenName)  # 3

for i in range(0,TN-1):
    print(BrokenName[i][0],end='.')  ### M.K.

print(BrokenName[TN-1])              ### LAST NAME -> GANDHI
