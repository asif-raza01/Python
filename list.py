nums=[1,2,3,4,5] #This is a list of integers
print(nums) #This will print the entire list
print(nums[0]) #This will print the first element of the list, which is 1
print(nums[2]) #This will print the third element of the list, which is 3
print(nums[-1]) #This will print the last element of the list, which is 5
print(nums[1:4]) #This will print a slice of the list from index 1 to index 3 (not including index 4), which is [2, 3, 4]
names=['Alice', 'Bob', 'Charlie'] #This is a list of strings
print(names) #This will print the entire list of names
mix=[1, 'Hello', 3.14, True] #This is a list with mixed data types
print(mix) #This will print the entire list with mixed data types
mix=[nums, names] #This is a list that contains two other lists
print(mix) #This will print the list that contains the two other lists
print(mix[0]) #This will print the first element of the mix list, which is the nums list
print(mix[1]) #This will print the second element of the mix list, which is the names list
print(mix[0][0]) #This will print the first element of the nums list, which is 1
print(mix[1][0]) #This will print the first element of the names list
print(len(mix)) #This will return the length of the mix list, which is 2
mix2=nums + names #This will concatenate the nums and names lists into a new list called mix2
print(mix2) #This will print the concatenated list mix2, which contains all the elements from both nums and names lists
print(len(mix2)) #This will return the length of the mix2 list, which is 8 (5 from nums and 3 from names)
nums.append(6) #This will add the number 6 to the end of the nums list
print(nums) #This will print the updated nums list, which now includes 6
names.append('David') #This will add the name 'David' to the end of the names list
print(names) #This will print the updated names list, which now includes 'David'
mix.append('New Element') #This will add the string 'New Element' to the end of the mix list
print(mix) #This will print the updated mix list, which now includes 'New Element' at the end
nums.insert(0, 10) #This will insert the number 10 at index 0 of the nums list
print(nums) #This will print the updated nums list, which now has 10 at the beginning
nums.remove(3) #This will remove the first occurrence of the number 3 from the nums list
print(nums) #This will print the updated nums list, which no longer includes 3
nums.pop() #This will remove the last element from the nums list
print(nums) #This will print the updated nums list, which no longer includes the last element       
nums.pop(0) #This will remove the element at index 0 from the nums list
print(nums) #This will print the updated nums list, which no longer includes the first element
del nums[1] #This will delete the element at index 1 from the nums list
print(nums) #This will print the updated nums list, which no longer includes the element at index 1
del nums[1:3] #This will delete the elements from index 1 to index 2 (not including index 3) from the nums list
print(nums) #This will print the updated nums list, which no longer includes the elements from
nums.extend([7, 8, 9]) #This will extend the nums list by adding the elements 7, 8, and 9 to the end of the list
print(nums) #This will print the updated nums list, which now includes 7,
nums[2:4]=[10, 11] #This will replace the elements from index 2 to index 3 (not including index 4) in the nums list with the new values 10 and 11
print(nums) #This will print the updated nums list, which now includes 10 and 11 in place of the previous elements at index 2 and index 3
#list is mutable, which means we can change its contents after it has been created. We can add, remove, or modify elements in a list using various methods and operations.