var=1
print(var)
print()
var = 1
account_balance = 1000.0
client_name = 'John Doe'
print(var, account_balance, client_name)
print(var)
print()
#print(Var) #var = 1 # not allowed to use a variable which doesn't exist

print()
var = "3.8.5"
print("Python version: " + var)
print()
var = 1
print(var)
var = var + 1
print(var)

print()
var = 100
var = 200 + 300 #
print(var) #he var variable is created and assigned a value of 100. Then, the same variable is assigned a new value: the result of adding 200 to 300, which is 500.

print()
a = 3.0
b = 4.0
c = (a ** 2 + b ** 2) ** 0.5
print("c =", c) #c = √ a2 + b2 = 5

print()
john = 3
mary = 5
adam = 6
print(john, mary, adam, sep=',')
total_apples = john + mary + adam
print(total_apples)

print()
#x *= 2 #x = x * 2
#sheep += 1 #sheep = sheep + 1

print()
kilometers = 12.25
miles = 7.38
miles_to_kilometers = miles * 1.61
kilometers_to_miles = kilometers / 1.61
print(miles, "miles is", round(miles_to_kilometers, 2), "kilometers") 
print(kilometers, "kilometers is", round(kilometers_to_miles, 2), "miles")
#round(3.141592 ,2) = 3.14 
#round(3.141592 ,3) = 3.14
#round(3.141592) = 3

print()
var = 2
print(var) 
var = 3
print(var)
var += 1
print(var)
print()
var = "007"
print("Agent " + var)

#2.4 SECTION SUMMARY
#A variable is a named location reserved to store values in the memory. A variable is created or initialized automatically when you assign a value to it for the first time. (2.1.4.1)
#Each variable must have a unique name ‒ an identifier. A legal identifier name must be a non-empty sequence of characters, must begin with the underscore(_), or a letter, and it cannot be a Python keyword. The first character may be followed by underscores, letters, and digits. Identifiers in Python are case-sensitive.
#Python is a dynamically-typed language, which means you don't need to declare variables in it. (2.1.4.3) To assign values to variables, you can use a simple assignment operator in the form of the equal (=) sign, i.e., var = 1.
#You can also use compound assignment operators (shortcut operators) to modify values assigned to variables, for example: var += 1, or var /= 5 * 2.
#You can assign new values to already existing variables using the assignment operator or one of the compound operators, for example:

#Incorrect vatiable names
# 10t (does not begin with a letter)
# !important (does not begin with a letter)
# xchange rate (contains a space).

