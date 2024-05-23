import functions
amount = input("enter the amount you want to convert: ")
functions.int_check(amount)

user_currency = input("enter the amount you want to convert: ")
functions.str_check(amount)

target_currency = input("enter the amount you want to convert: ")
functions.str_check(amount)

final_amount = functions.convert(amount, user_currency, target_currency)

if final_amount is not None:
    print(f"{amount} {user_currency} is equal to {final_amount:.2f} {target_currency}")
    print("lets go!! cause Im tired")

