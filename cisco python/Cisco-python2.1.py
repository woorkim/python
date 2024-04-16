print("Hello, world!")
print()#
print("The itsy bitsy spider climbed up the waterspout.")
print("Down came the rain and washed the spider out.")
print()#
print("The itsy bitsy spider\nclimbed up the waterspout.")
print()#
print("Down came the rain\nand washed the spider out.")
print()#
print("The itsy bitsy spider" , "climbed up" , "the waterspout.")

print()#---positional argument!
print("My name is", "Python.")
print("Monty Python.")

print()#---Keyword arguments = end="\n"
print("My name is", "Python.", end=" ")
print("Monty Python.")

print()#---Keyword arguments = end="\n"
print("My name is ", end="")
print("Monty Python.")

print()#---Keyword arguments = sep
#print("My", "name", "is", "Monty", "Python.", sep="-")

print()#---Keyword arguments = sep & sep
print("My", "name", "is", sep="_", end="$")
print("Monty", "Python.", sep="*", end="&\n")

print()#---Lab1
print("Programming","Essentials","in", sep="***", end="...")
print("Python")

print()#--- quiz1
print("My\nname\nis\nBond.", end=" ")
print("James Bond.")

print()#--- quiz
#print(sep="&", "fish", "chips")
print("fish", "chips", sep="&") 

print()#--- quiz2
print('Greg\'s book.')
print("'Greg's book.'")
print('"Greg\'s book."') #
print("Greg\'s book.") 
print('"Greg\'s book."') #
#print('"Greg's book."') # SyntaxError, escape character.
      
print()#--- quiz3
print('I\'m learning to become a Python developer!\nI\'m so excited!')

#2.1 SECTION SUMMARY
#1. The print() function is a built-in function. It prints/outputs a specified message to the screen/console window.
#2. Built-in functions, contrary to user-defined functions, are always available and don't have to be imported. Python 3.8 comes with 69 built-in functions. You can find their full list provided in alphabetical order in the Python Standard Library.
#3. To call a function (this process is known as function invocation or function call), you need to use the function name followed by parentheses. You can pass arguments into a function by placing them inside the parentheses. You must separate arguments with a comma, e.g., print("Hello,", "world!"). An "empty" print() function outputs an empty line to the screen.
#4. Python strings are delimited with quotes, e.g., "I am a string" (double quotes), or 'I am a string, too' (single quotes).
#5. Computer programs are collections of instructions. An instruction is a command to perform a specific task when executed, e.g., to print a certain message to the screen.
#6. In Python strings the backslash (\) is a special character which announces that the next character has a different meaning, e.g., \n (the newline character) starts a new output line.
#7. Positional arguments are the ones whose meaning is dictated by their position, e.g., the second argument is outputted after the first, the third is outputted after the second, etc.
#8. Keyword arguments are the ones whose meaning is not dictated by their location, but by a special word (keyword) used to identify them.
#9. The end and sep parameters can be used for formatting the output of the print() function. The sep parameter specifies the separator between the outputted arguments, e.g., print("H", "E", "L", "L", "O", sep="-"), whereas the end parameter specifies what to print at the end of the print statement.
