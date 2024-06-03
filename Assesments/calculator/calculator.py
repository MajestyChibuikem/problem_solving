def main():
    #program will take two parameters\
    import functions
    """
    num1@ First parameter
    num2@ second parameter
    op@ operator 
    return 1
    """
    #input 
    num1 = input("enter your number: ")
    #input check
    num1 = functions.int_check(num1)
    #input -- add lower() incase of capitalised letters
    op = input("Enter operation: ").lower()
    #input check
    op = functions.str_check(op)
    #input
    num2 = input("Enter second number: ")
    #input check
    num2 = functions.int_check(num2)

    """
    the header.functions[op] takes symbol or string andcalls the inteded functions
    """
    op = functions.diction[op]
    result = op(num1, num2)
    print(result)

if __name__ == "__main__":
    main()