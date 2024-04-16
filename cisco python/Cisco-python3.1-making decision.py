# = is an assignment operator, e.g., a = b assigns a with the value of b;
# == is the question are these values equal? so a == b compares a and b.
# It is a binary operator with left-sided binding. It needs two arguments and checks if they are equal.

#var = 0  # Assigning 0 to var
#print(var == 0) #Equality: the equal to operator (==)
#var = 1  # Assigning 1 to var
#print(var == 0) #Equality: the equal to operator (==)

print()
#var = 0  # Assigning 0 to var
#print(var != 0)  #Inequality: the not equal to operator (!=)
#var = 1  # Assigning 1 to var
#print(var != 0)   #Inequality: the not equal to operator (!=)

print()
# black_sheep > white_sheep  # Greater than True confirms it; False denies it.
# centigrade_outside >= 0.0  # Greater than or equal to
# current_velocity_mph < 85  # Less than
# current_velocity_mph <= 85  # Less than or equal to

print()
# - Conditional execution: the if statement
#if sheep_counter >= 120: # Evaluate a test expression
#    sleep_and_dream() # Execute if test expression is True

# - Conditional execution: the if-else statement
#if the_weather_is_good:
#    go_for_a_walk()
#    have_fun()
#else:
#    go_to_a_theater()
#    enjoy_the_movie()
#have_lunch()

print()
# Nested if-else statements
#if the_weather_is_good:
#    if nice_restaurant_is_found:
#        have_lunch()
#    else:
#        eat_a_sandwich()
#else:
#    if tickets_are_available:
#        go_to_the_theater()
#    else:
#        go_shopping()

print()
# elif is used to check more than just one condition, and to stop when the first statement which is true is found.

print()
# Read two numbers
#number1 = int(input("Enter the first number: "))
#number2 = int(input("Enter the second number: ")) 
# Choose the larger number
#if number1 > number2:
#    larger_number = number1
#else:
#    larger_number = number2
# Print the result
#print("The larger number is:", larger_number)

print()
#income = float(input("Enter the annual income: "))
#if income < 85528:
#	tax = income * 0.18 - 556.02
#else:
#	tax = (income - 85528) * 0.32 + 14839.02
#if tax < 0.0:
#	tax = 0.0
#tax = round(tax, 0)
#print("The tax is:", tax, "thalers")

print()
#year = int(input("Enter a year: "))
#if year < 1582:
#	print("Not within the Gregorian calendar period")
#else:
#	if year % 4 != 0:
#		print("Common year")
#	elif year % 100 != 0:
#		print("Leap year")
#	elif year % 400 != 0:
#		print("Common year")
#	else:
#		print("Leap year")


# - 3.1SECTION SUMMARY
#x = 10 # - Each if statement is tested separately.
#if x > 5: # condition one
#    print("x is greater than 5")  # Executed if condition one is True.
#if x < 10: # condition two
#    print("x is less than 10")  # Executed if condition two is True.
#if x == 10: # condition three
#    print("x is equal to 10")  # Executed if condition three is True.
    
print()
#x = 10
#if x < 10: # condition
#    print("x is less than 10")  # Executed if the condition is True.
#else:
#    print("x is greater than or equal to 10")  # Executed if the condition is False.

print()
x = 11
if x == 10: # True
    print("x == 10")
if x > 15: # False
    print("x > 15")
elif x > 10: # False
    print("x > 10")
elif x > 5: # True
    print("x > 5")
else:
    print("else will not be executed")
# If the condition for if is False, the program checks the conditions of the subsequent elif blocks - the first elif block that is True is executed. 
# If all the conditions are False, the else block will be executed

print()
#x = 10
#if x > 5: # True
#    if x == 6: # False
#        print("nested: x == 6")
#    elif x == 10: # True
#        print("nested: x == 10")
#    else:
#        print("nested: else")
#else:
#    print("else")

print()
#QUIZ 
# 1.What is the output of the following snippet?
x = 5
y = 10
z = 8
print(x > y)
print(y > z)

print()
# 2.What is the output of the following snippet?
x, y, z = 5, 10, 8
print(x > z)
print((y - 5) == x)

print()
# 3.What is the output of the following snippet?
x, y, z = 5, 10, 8
x, y, z = z, y, x
print(x > z)
print((y - 5) == x)

print()
#4: What is the output of the following snippet?
#x = 10
#if x == 10:
#    print(x == 10)
#if x > 5:
#    print(x > 5)
#if x < 10:
#    print(x < 10)
#else:
#    print("else")

#5: What is the output of the following snippet?
print()
x = "1"
if x == 1:
    print("one")
elif x == "1":
    if int(x) > 1:
        print("two")
    elif int(x) < 1:
        print("three")
    else:
        print("four")
if int(x) == 1:
    print("five")
else:
    print("six")

#6: What is the output of the following snippet?
print()
x = 1
y = 1.0
z = "1"
if x == y:
    print("one")
if y == int(z):
    print("two")
elif x == y:
    print("three")
else:
    print("four")