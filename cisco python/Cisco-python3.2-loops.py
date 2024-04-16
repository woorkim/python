print("while")
#while conditional_expression:
#    instruction_one
#    instruction_two
#    instruction_three
#    :
#    :
#    instruction_n

# infinite, endless loop: 
# While = The semantic difference is more important: when the condition is met, 
# if performs its statements only once; while repeats the execution as long as the condition evaluates to True.\
# infinite loop
# Store the current largest number here.
#largest_number = -999999999
# Input the first value.
#number = int(input("Enter a number or type -1 to stop: "))
# If the number is not equal to -1, continue
#while number != -1: # ! is not!
    # Is number larger than largest_number?
#    if number > largest_number:
        # Yes, update largest_number.
#        largest_number = number
    # Input the next number.
#    number = int(input("Enter a number or type -1 to stop: "))
# Print the largest number.
#print("The largest number is:", largest_number)
#print()

# The while loop: more examples
# A program that reads a sequence of numbers
# and counts how many numbers are even and how many are odd.
# The program terminates when zero is entered.
#odd_numbers = 0
#even_numbers = 0
# Read the first number.
#number = int(input("Enter a number or type 0 to stop: "))
# 0 terminates execution.
#while number != 0:
    # Check if the number is odd.
#    if number % 2 == 1:
        # Increase the odd_numbers counter.
#        odd_numbers += 1
#    else:
        # Increase the even_numbers counter.
#        even_numbers += 1
    # Read the next number.
#    number = int(input("Enter a number or type 0 to stop: "))
# Print results.
#print("Odd numbers count:", odd_numbers)
#print("Even numbers count:", even_numbers)
# while number != 0: and while number:

print()
# Loop with counter variable to exit a loop
#counter = 5
#while counter != 0:
#    print("Inside the loop.", counter)
#    counter -= 1
#print("Outside the loop.", counter)

#print()
#counter = 5 # same as above result
#while counter:
#    print("Inside the loop.", counter)
#    counter -= 1
#print("Outside the loop.", counter)
#print()


#power = 1
#for expo in range(16):
#    print("2 to the power of", expo, "is", power)
#    power *= 2

print()
#3.2 break & continue
# *break – exits the loop immediately, and unconditionally ends the loop's operation; the program begins to execute the nearest instruction after the loop's body;
# *continue – behaves as if the program has suddenly reached the end of the body; the next turn is started and the condition expression is tested immediately.
# break - example
print("The break instruction:")
for i in range(1, 6):
    if i == 3:
        break
    print("Inside the loop.", i)
print("Outside the loop.")

# continue - example
print("\nThe continue instruction:")
for i in range(1, 6):
    if i == 3:
        continue
    print("Inside the loop.", i)
print("Outside the loop.")

print()
#3.2.12 while loop and the else branch
i = 1
while i < 5:
    print(i)
    i += 1
else:
    print("else:", i)
print()

i = 5
while i < 5:
    print(i)
    i += 1
else:
    print("else:", i)

print()
#3.2.13 for loop and the else branch
for i in range(5):
    print(i)
else:
    print("else:", i)

print()
i = 111
for i in range(2, 1):
    print(i)
else:
    print("else:", i)

#3.2 SECTION SUMMARY
print()
#the while loop executes a statement or a set of statements as long as a specified 
# boolean condition is true, e.g.:
# Example 1
while True:
    print("Stuck in an infinite loop.")
# Example 2
counter = 5
while counter > 2:
    print(counter)
    counter -= 1

print()
#the for loop executes a set of statements many times; it's used to iterate over a sequence 
# (e.g., a list, a dictionary, a tuple, or a set – you will learn about them soon) or other 
# iterable objects (e.g., strings). You can use the for loop to iterate over a sequence of numbers using the built-in range function. Look at the examples below:
# Example 1
word = "Python"
for letter in word:
    print(letter, end="*")
 
# Example 2
for i in range(1, 10):
    if i % 2 == 0:
        print(i)