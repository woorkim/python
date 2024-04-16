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
numbers = [10, 5, 7, 2, 1]
print("Original list contents:", numbers)  # Printing original list contents.
numbers[0] = 111
print("\nPrevious list contents:", numbers)  # Printing previous list contents.
numbers[1] = numbers[4]  # Copying value of the fifth element to the second.
print("New list contents:", numbers)  # Printing current list contents.
print()
print(numbers[0]) # Accessing the list's first element.
print("\nList length:", len(numbers))  # Printing the list's length.
print(numbers) # Printing the whole list.

#3.7 Functions vs. methods