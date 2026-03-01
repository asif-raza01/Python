#Understanding strings in Python

print('Asif') #This is a string literal
#print('Asif's laptop') #This will cause an error because of the single quote in "Asif's"
#To fix the above error, we can use double quotes to enclose the string
print("Asif's laptop") #This will work correctly
#We can also use escape characters to include special characters in a string
print('Asif\'s laptop') #Using backslash to escape the single quote
#suppose you want to print a string n times, you can use the multiplication operator
print('Asif ' * 3) #This will print 'Asif ' three times
#We can also concatenate strings using the + operator   
print('Asif' 'raza') #This will concatenate the two strings without any space
print('Asif ''raza') #This will also concatenate the two strings without any space
print('Asif ' + 'raza') #This will concatenate the two strings with a space in between
#if you want to make it dynameic, you can use variables to store the strings and then concatenate them
first_name = 'Asif' 
last_name = 'Raza'
full_name = first_name + ' ' + last_name #Concatenating the first name and last name with a space in between
print(full_name) #This will print 'Asif Raza'


#lets understand string indexing and slicing
my_string = 'Hello, World!'
print(my_string[0]) #This will print 'H', which is the first character of the string
print(my_string[7]) #This will print 'W', which is the eighth character of the string
print(my_string[-1]) #This will print '!', which is the last character of the string
print(my_string[-6]) #This will print 'W', which is the sixth character from the end of the string
#interesrtingly we can access characters in a string using both positive and negative indexing

#NOW, let's understand string slicing in Python
print(my_string[0:5]) #This will print 'Hello', which is the substring from index 0 to 4 STARRTING INDEX INCLUSIVE, ENDING INDEX EXCLUSIVE
print(my_string[7:12]) #This will print 'World', which is the substring
#HERE even if we take second index as 13, it will not cause an error because the ending index is exclusive and it will just return the substring up to the last character
#one interesting to note that string are immutable in Python, which means that once a string is created, it cannot be modified. However, we can create a new string by concatenating or slicing existing strings.
#so you can change the value of a string variable, but you cannot change the individual characters of a string. For example:
my_string = 'Hello, World!' 
#my_string[0] = 'h' #This will cause an error because we cannot change the individual characters of a string
print(len(my_string)) #This will print the length of the string, which is 13
My_text="""This is a multi-line string.
It can span multiple lines without the need for escape characters.
This is useful for writing long strings or documentation."""
print(My_text) #This will print the multi-line string as it is, preserving the line breaks.