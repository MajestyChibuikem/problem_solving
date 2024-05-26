def main():
    import functions

    amount = input("enter the amount you want to convert: ")
    """
    issue: i needed to manually assign amount to the returned value
    seems it treats both as different variables
    """
    amount = functions.int_check(amount)

    user_currency = input("enter the currency you want to convert: ")
    # functions.str_check(amount)
    functions.str_check(user_currency)

    target_currency = input("enter the currency you want to convert to: ")
    # functions.str_check(amount)
    functions.str_check(target_currency)

    final_amount = functions.convert(amount, user_currency, target_currency)

    if final_amount is not None:
        print(f"{amount} {user_currency} is equal to {final_amount:.2f} {target_currency}")
        print("lets go!! cause Im tired")



if __name__ == "__main__":
    main()