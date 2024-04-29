#Python has adopted a convention stating that the elements in a list are 
# always numbered starting from zero

#numbers = [10, 5, 7, 2, 1] # list
#print(numbers)

print()
#indexing lists
#numbers = [10, 5, 7, 2, 1]
#print("Original list contents:", numbers)  # Printing original list contents.
#numbers[0] = 111 # list 0 
#print("New list contents: ", numbers)  # Current list contents.

print()
#numbers = [10, 5, 7, 2, 1]
#print("Original list contents:", numbers)  # Printing original list contents.
#numbers[0] = 111
#print("\nPrevious list contents:", numbers)  # Printing previous list contents.
#numbers[1] = numbers[4]  # Copying value of the fifth element to the second.
#print("New list contents:", numbers)  # Printing current list contents.
#print()
#print(numbers[0]) # Accessing the list's first element.
#print("\nList length:", len(numbers))  # Printing the list's length.
#print(numbers) # Printing the whole list.

#3.4 SUMMARY
#1. The list is a type of data in Python used to store multiple objects. It is an ordered and mutable collection of comma-separated items between square brackets, 

print()
my_list = [1, None, True, "I am a string", 256, 0]
my_list = [1, None, True, 'I am a string', 256, 0]
print(my_list[3])  # outputs: I am a string
print(my_list[-1])  # outputs: 0
 
my_list[1] = '?'
print(my_list)  # outputs: [1, '?', True, 'I am a string', 256, 0]
 
my_list.insert(0, "first")
my_list.append("last")
print(my_list)  # outputs: ['first', 1, '?', True, 'I am a string', 256, 0, 'last']

#Question 1: What is the output of the following snippet?
lst = [1, 2, 3, 4, 5]
lst.insert(1, 6)
del lst[0]
lst.append(1)
print(lst)

#Question 2: What is the output of the following snippet?
lst = [1, 2, 3, 4, 5]
lst_2 = []
add = 0
for number in lst:
    add += number
    lst_2.append(add)
print(lst_2)

#Question 3: What is the output of the following snippet?
lst = []
del lst
#print(lst) #NameError: name 'lst' is not defined

print()
#Question 4: What is the output of the following snippet?
lst = [1, [2, 3], 4]
print(lst[1])
print(len(lst))