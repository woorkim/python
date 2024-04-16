#####Parameterized functions#####
print()
#def message(number):
#    print("Enter a number:", number)
#message()

print()
#def message(number):
#    print("Enter a number:", number)
#message(1)

print()# shadowing:The parameter named number is a completely different entity from the variable named number.
#def message(number):
#    print("Enter a number:", number)
#number = 1234
#message(1)
#print(number)
 
print()
def message(what, number):
    print("Enter", what, "number", number)
message("telephone", 11)
message("price", 5)
message("number", "number")

#####Positional parameter passing#####
print()
def introduction(first_name, last_name):
    print("Hello, my name is", first_name, last_name)
 
introduction("Luke", "Skywalker")
introduction("Jesse", "Quick")
introduction("Clark", "Kent")

#####Keyword argument passing#####
print()
def introduction(first_name, last_name):
    print("Hello, my name is", first_name, last_name)
 
introduction(first_name = "James", last_name = "Bond")
introduction(last_name = "Skywalker", first_name = "Luke")

print()
#def introduction(first_name, last_name):
#    print("Hello, my name is", first_name, last_name)

#introduction(surname="Skywalker", first_name="Luke")

#####Mixing positional and keyword#####
print() # you have to put positional arguments before keyword arguments.
def adding(a, b, c):
    print(a, "+", b, "+", c, "=", a + b + c)

adding(1, 2, 3) #positional argument passing
adding(c = 1, a = 2, b = 3) #keyword argument passing
adding(3, c = 1, b = 2) #mixing argument passing
#adding(3, a = 1, b = 2) # error
adding(4, 3, c = 2)

print()
def introduction(first_name, last_name="Smith"):
     print("Hello, my name is", first_name, last_name)
introduction("James", "Doe") # invoking function
introduction("Henry")
introduction(first_name="William")

print()
def introduction(first_name="John", last_name="Smith"):
    print("Hello, my name is", first_name, last_name)
introduction()
introduction(last_name="Hopkins")
print()

#####4.2 SUMMARY#### 
#1. can pass information to functions by using parameters.
def hi(name):
    print("Hi,", name) #one-parameter function
hi("Greg")

print()
def hi_all(name_1, name_2):
    print("Hi,", name_2) #two-parameter function:
    print("Hi,", name_1) #
hi_all("Sebastian", "Konrad")

print()
def address(street, city, postal_code):
    print("Your address is:", street, "St.,", city, postal_code)
 
s = input("Street: ") #three-parameter function:
p_c = input("Postal Code: ")#
c = input("City: ")#
address(s, c, p_c)

#2.pass arguments to a function using
# *positional argument passing in which the order of arguments passed matters (Ex. 1)
# *keyword (named) argument passing in which the order of arguments passed doesn't matter (Ex. 2)
# *a mix of positional and keyword argument passing (Ex. 3.)
print()
#Ex. 1
def subtra(a, b):
    print(a - b)
 
subtra(5, 2) # outputs: 3
subtra(2, 5) # outputs: -3

print()
#Ex. 2
def subtra(a, b):
    print(a - b)
 
subtra(a=5, b=2) # outputs: 3
subtra(b=2, a=5) # outputs: 3

print() 
#Ex. 3
def subtra(a, b):
    print(a - b)
 
subtra(5, b=2) # outputs: 3
subtra(5, 2) # outputs: 3
print()

#Remember that positional arguments mustn't follow keyword arguments. 
def subtra(a, b):
    print(a - b)
 
subtra(5, b=2) # outputs: 3
#subtra(a=5, 2) # Syntax Error

print()
def name(first_name, last_name="Smith"):
    print(first_name, last_name)
 
name("Andy") # outputs: Andy Smith
name("Betty", "Johnson") # outputs: Betty Johnson (the keyword argument replaced by "Johnson")
print()

#Q1: What is the output of the following snippet?
def intro(a="James Bond", b="Bond"):
     print("My name is", b + ".", a + ".")
 
intro()

print()
#Q2: What is the output of the following snippet?
def intro(a="James Bond", b="Bond"):
    print("My name is", b + ".", a + ".")
 
intro(b="Sean Connery")

#Q3: What is the output of the following snippet?
def intro(a, b="Bond"):
    print("My name is", b + ".", a + ".")
 
intro("Susan")

#Q4: What is the output of the following snippet?
def add_numbers(a, b=2, c):
    print(a + b + c)
add_numbers(a=1, c=3)