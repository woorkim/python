#Return without an expression
def happy_new_year(wishes = True):
    print("Three...")
    print("Two...")
    print("One...")
    if not wishes:
        return #immediate termination of the function's execution
    print("Happy New Year!")
print()
happy_new_year()
print()    
happy_new_year(True) #
print()
happy_new_year(False) # return instruction will cause its termination just before the wishes
print()

#Return with an expression
def boring_function():
    return 123
x = boring_function()
print("The boring_function has returned its result. It's:", x)

print()
def boring_function():
    print("'Boredom Mode' ON.")
    return 123 
print("This lesson is interesting!")
boring_function()
print("This lesson is boring...")
print()

#None
#print(None + 2) #TypeError: unsupported operand type(s) for +: 'NoneType' and 'int'

value = None
if value is None:
    print("Sorry, you don't carry any value")
print()

def strange_function(n):
    if(n % 2 == 0):
        return True
print(strange_function(2))
print(strange_function(1)) # return None!!!!
print()

#Effects and results: lists and functions, pass a list to a function, the function has to handle it like a list.
def list_sum(lst):
    s = 0
    for elem in lst:
        s += elem
 
    return s
print(list_sum([5, 4, 3]))
#print(list_sum(5))# single integer value mustn't be iterated through by the for loop!
print()

def strange_list_fun(n):
    strange_list = []
    
    for i in range(0, n):
        strange_list.insert(0, i)
    
    return strange_list

print(strange_list_fun(5))

