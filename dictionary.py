dict1={'alice': 1, 'bob': 2, 'charlie': 3}
print(dict1) #This will print the dictionary dict1, which contains the key-value pairs {'alice': 1, 'bob': 2, 'charlie': 3}
print(type(dict1)) #This will print the type of the variable dict1, which is <class 'dict'>
dict2=dict(a=1, b=2, c=3) #This is another way to create a dictionary using keyword arguments
print(dict2) #This will print the dictionary dict2, which contains the key-value pairs {'a': 1, 'b': 2, 'c': 3}
print(dict1['alice']) #This will print the value associated with the key 'alice' in dict1, which is 1
print(dict1.get('bob')) #This will return the value associated with the key 'bob' in dict1, which is 2
print(dict1.get('dave', 'Not Found')) #This will return 'Not Found' since the key 'dave' is not present in dict1
dict1['dave'] = 4 #This will add a new key-value pair 'dave': 4 to dict1
print(dict1) #This will print the updated dictionary dict1, which now contains {'alice': 1, 'bob': 2, 'charlie': 3, 'dave': 4}