#decide password length
import functions

def main():
    psswd_len = input("Enter the length of the password: ")
    psswd_len = functions.int_check(psswd_len)
    psswd = functions.generate_password(psswd_len)
    print("Generated Password:", psswd)

if __name__ == "__main__":
    main()