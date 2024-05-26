def check_leap_year(user_input):
    if user_input % 4 == 0:  
        if user_input % 100 == 0:  
            if user_input % 400 == 0:  
                return True
            else:
                return False
        else:
            return True
    else:
        return False
    
def int_check(user_input):
    while True:
        if user_input.isdigit():
            user_input = int(user_input)
            return user_input
            break
        else:
            print("Incorrect format, Please try again: ")
            user_input = input("Try again: ")
    pass