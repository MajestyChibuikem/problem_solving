def float_check(user_input):
    while True:
        if user_input.isdigit():
            return float(user_input)
            break
        else:
            user_input = input("Incorrect format, Please try again: ")
    pass

def convert_to_mile(km):
    mile = km / 1.60934
    return mile

def convert_to_km(mile):
    km = mile * 1.60934
    return km

