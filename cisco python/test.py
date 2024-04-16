#def devnet():
#    """prints simple function""" # ''' is same as """
#    print('Simple function')
#devnet()

def sub(arg1, arg2):
    result = arg1 - arg2
    return result

sub(arg2=15, arg1=10)

def hello(*args):
    for arg in args:
        print("Hello", arg, "!")

hello('Caleb', 'Sydney', 'Savannah')