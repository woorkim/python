#print("Tell me anything...")
#anything = input() #anything=User Input!!! 
#print("Hmm...", anything, "... Really?")

print()
#anything = input("Tell me anything...") #input w arguments! 
#print("Hmm...", anything, "...Really?")

print()
#anything = input("Enter a number: ")
#something = anything ** 2.0 # ** operator to 'str' (string) accompanied with 'float'.This is prohibited
#print(anything, "to the power of 2 is", something) 

print()
#anything = float(input("Enter a number: "))
#something = anything ** 2.0
#print(anything, "to the power of 2 is", something)

print()
#leg_a = float(input("Input first leg length: "))
#leg_b = float(input("Input second leg length: "))
#hypo = (leg_a**2 + leg_b**2) ** .5
#print("Hypotenuse length is", hypo)

print()
#leg_a = float(input("Input first leg length: "))
#leg_b = float(input("Input second leg length: "))
#print("Hypotenuse length is", (leg_a**2 + leg_b**2) ** .5)

print()
#fnam = input("May I have your first name, please? ")
#lnam = input("May I have your last name, please? ")
#print("Thank you.")
#print("\nYour name is " + fnam + " " + lnam + ".")

print()
#print("+" + 9 * "-" + "+")# string * number, "James" * 3 gives "JamesJamesJames"
#print(("|" + " " * 8 + "|\n") * 5, end="") #5 * "2" (or "2" * 5) gives "22222" (not 10!)
#print("+" + 11 * "-" + "+")

print() #str(number)
#leg_a = float(input("Input first leg length: "))
#leg_b = float(input("Input second leg length: "))
#print("Hypotenuse length is " + str((leg_a**2 + leg_b**2) ** .5))#

print() # Simple input and output
#a = float(input("Enter first value: "))
#b = float(input("Enter second value: "))
#print("Addition:", a + b)
#print("Subtraction:", a - b)
#print("Multiplication:", a * b)
#print("Division:", a / b)
#print("\nThat's all, folks!")

print() # Operators and expressions
#x = float(input("Enter value for x: "))
#y = 1./(x + 1./(x + 1./(x + 1./x)))
#print("y =", y)
print()
#hour = int(input("Starting time (hours): "))
#mins = int(input("Starting time (minutes): "))
#dura = int(input("Event duration (minutes): "))
#mins = mins + dura # find a total of all minutes
#hour = hour + mins // 60 # find a number of hours hidden in minutes and update the hour
#mins = mins % 60 # correct minutes to fall in the (0..59) range
#hour = hour % 24 # correct hours to fall in the (0..23) range
#print(hour, ":", mins, sep='')

#2.6 SECTION SUMMARY
#1. The print() function sends data to the console, while the input() function gets data from the console.
#2. The input() function comes with an optional parameter: the prompt string. It allows you to write a message before the user input,

#name = input("Enter your name: ")
#print("Hello, " + name + ". Nice to meet you!")

#3.When the input() function is called, the program's flow is stopped, the prompt symbol keeps blinking 
# it prompts the user to take action when the console is switched to input mode) until the user has entered an input and/or pressed the Enter key. 
print()
#name = input("Enter your name: ")
#print("Hello, " + name + ". Nice to meet you!")
#print("\nPress Enter to end the program.")
#input()
#print("THE END.")

print()
#name = input("Enter your name: ")
#print("Hello, " + name + ". Nice to meet you!")
#print("\nPress Enter to end the program.")
#input()
#print("THE END.")

#4.The result of the input() function is a string. You can add strings to each other using the concatenation (+) 
# operator. Check out this code:

print() # add strings to each other using the concatenation (+) operator.
#num_1 = input("Enter the first number: ") # Enter 12
#num_2 = input("Enter the second number: ") # Enter 21 
#print(num_1 + num_2) # the program returns 1221

print()# multiply (* ‒ replication) strings
#my_input = input("Enter something: ") # Example input: hello
#print(my_input * 3) # Expected output: hellohellohello

#2.6 SECTION SUMMARY
print()
#what is output?
#x = int(input("Enter a number: ")) #The user enters 2
#print(x * "5") # = 2ea 5, not 2*5=10

print()
#what is output?
#x = input("Enter a number: ") # The user enters 2
#print(type(x))

x = int(input())
y = int(input())
x = x / y
y = y / x
print(y)

