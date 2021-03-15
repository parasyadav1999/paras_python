vowels=["a","e","i","o","u"]             #refrence sequence to compare the input
x=input("enter the sentence")
found=[]                                #empty list used to store the vowels present in  input sentence
for i in x:                             #loop to find vowels present in input sentence
    if i in vowels:
        if i not in found:
            found.append(i)
print("vowels present in ",x,"is",found)
letter={}.fromkeys(found,0)            #dictionary to find the no. of vowels present in input sentence
for i in x:
    if i in letter:
        letter[i]+=1
values=list(letter.values())
print("no. of vowels present in ",x,"is",values)



