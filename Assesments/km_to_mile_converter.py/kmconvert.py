import functions
def main():
    choice = input("1 for kilometer - mile \n2 for mile to kilometer: ")
    while True:

        if choice == "1":
            km = input("Enter the kilometer value: ")
            km = functions.float_check(km)
            mile = functions.convert_to_mile(km)

            print(f"{km} kilometer is roughly equal to {mile} miles")
    
        elif choice == "2":
            mile = input("Enter the mile value: ")
            mile = functions.float_check(mile)
            km = functions.convert_to_km(mile)
            print(f"{mile} miles is roughly equal to {km} kilometer")

        else:
            choice = input("Invalid input, try again\n1 for kilometer to mile\n2 for mile to kilometer: ")


if __name__ == "__main__":
    main()
        