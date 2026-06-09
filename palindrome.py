#Palindrome

Word=input("Enter a word: ")

RWord=Word[::-1]  ###############

if RWord.upper()==Word.upper():
    print(Word," is a Palindrome!")
else:
    print(Word," is NOT a Palindrome!")
a=input()
