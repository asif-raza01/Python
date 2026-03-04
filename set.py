set1={23,46,56,65,46}
print(set1) #This will print the set set1, which contains the unique elements {23, 46, 56, 65}
print(type(set1)) #This will print the type of the variable set1, which is <class 'set'>
set2=set([1,2,3,4,5]) #This is a set created from a list of integers
print(set2) #This will print the set set2, which contains the unique elements {1, 2, 3, 4, 5}
set3=set('Hello') #This is a set created from a string, which will contain the unique characters in the string  
print(set3) #This will print the set set3, which contains the unique characters {'H', 'e', 'l', 'o'}

set3=set('absedfg') #This is a set created from a string, which will contain the unique characters in the string
set4=set('opqrstumhagdaq') #This is another set created from a string, which will contain the unique characters in the string   
print(set3 | set4) #This will print the union of set3 and set4, which contains all unique characters from both sets
print(set3 ^ set4) #This will print the symmetric difference of set3 and set4
print(set3 & set4) #This will print the intersection of set3 and set4, which contains only the characters that are present in both sets
print(set3 - set4) #This will print the difference of set3 and set4, which contains the characters that are in set3 but not in set4