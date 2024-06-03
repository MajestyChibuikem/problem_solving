#check for non-int input and loops back if true
def int_check(user_input):
    while True:
        if user_input.isdigit():
            return float(user_input)
        else:
            user_input = input("Incorrect format, Please try again: ")
    pass

#area calculation
def area(base, height):
    return 0.5 * base * height
