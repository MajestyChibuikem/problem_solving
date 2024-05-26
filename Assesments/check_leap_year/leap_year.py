import functions
def main():
    year = input("Enter a year: ")
    year = functions.int_check(year)
    if functions.check_leap_year(year):
        print(year, "is a leap year.")
    else:
        print(year, "is not a leap year.")

if __name__ == "__main__":
    main()
