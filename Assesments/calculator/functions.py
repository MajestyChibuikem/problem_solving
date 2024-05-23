#check for non-int input and loops back if true
def int_check(user_input):
    while True:
        if user_input.isdigit():
            return float(user_input)
            break
        else:
            print("Incorrect format, Please try again: ")
    pass

#checks if the input is a string and loops back if not
def str_check(user_input):
    while True:
        if user_input.isdigit():
            print("Wrong input format, try again: ")
        else:
            return (user_input)

#addition
def add(num1, num2):
    return num1 + num2

#substraction
def sub(num1, num2):
    return num2 - num1

def sub2(num1, num2):
    return num1 - num2

#division
def div(num1, num2):
    return num1 / num2

#multiplication
def mult(num1, num2):
    return num1 * num2

#square
def sq(num):
    return num**2
#cube
def cube(num):
    return num**3


#mapping keys to the functions: add, sub, mult, div
functions = {
    "+" : add,
    "add" : add,
    "-" : sub,
    "sub" : sub,
    "/" : div,
    "div" : div,
    "*" : mult,
    "mult" : mult
}