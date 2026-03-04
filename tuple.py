list=[1,2,3,4,5]
print(type(list)) #This will print the type of the variable list, which is <class 'list'>
tup=(1,2,3,4,5) #This is a tuple of integers
print(type(tup)) #This will print the type of the variable tup, which is <class 'tuple'>
print(min(tup)) #This will print the minimum value in the tuple, which is 1
print(max(tup)) #This will print the maximum value in the tuple, which is 5
# tup[2]=10 #This will raise a TypeError because tuples are immutable and cannot be modified after they have been created
# print(tup) #This will not be executed due to the error in the previous line
tupA=(1,2,3) #This is a tuple of integers
num1,num2,num3=tupA #This will unpack the values from the tuple tupA into the variables num1, num2, and num3
print(num1) #This will print the value of num1, which is 1  
print(num2) #This will print the value of num2, which is 2
print(num3) #This will print the value of num3, which is 3
tupB=(4,'Navin',[3,4,5,6]) #This is a tuple that contains an integer, a string, and a list
tupB[2][1]=9 #This will modify the second element of the list that is the third element of the tuple tupB, changing the value 4 to 9
print(tupB) #This will print the updated tuple tupB, which now contains the modified list with the value 9 instead of 4
print('Navin' in tupB) #This will print the result of the previous line