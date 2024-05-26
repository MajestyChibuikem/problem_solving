#to import the requests module and allow requests in the script
import requests

#this method loads the api keys from the api file
def load_api(file_path):
    with open(file_path, "r") as f:
        return f.read().strip()


#this method checks for non-int input 
#but in this case i want to make the return value to be float not int
#and keeps looping till correct format is given
def int_check(user_input):
    while True:
        if user_input.isdigit():
            user_input = float(user_input)
            return user_input
            break
        else:
            print("Incorrect format, Please try again: ")
            user_input = input("Try again: ")
    pass

# this method check for non-string input
# and keeps looping till correct format is given
def str_check(user_input):
    while True:
        # Check if the input consists only of digits
        if user_input.isdigit():
            print("Wrong input format ")
            user_input = input("Try again: ")
        else:
            return (user_input)

def get_rates(user_currency, target_currency):
    # Load the API key from the specified file path
    api_key = load_api("Assesments/CurrencyConverter/apikeys.txt")
    
    # Construct the URL for the API request
    url = f'https://open.er-api.com/v6/latest/{user_currency}'
    
    # Define the parameters for the API request, including the API key
    params = {'app_id': api_key}
    
    # Send a GET request to the API endpoint
    response = requests.get(url, params=params)
    
    # Parse the JSON response
    data = response.json()
    
    # Check if there's an error in the response
    if 'error' in data:
        print("Error:", data['description'])
        return None

    # Check if the 'rates' key exists in the response data
    if 'rates' in data:
        # Extract the rates dictionary from the response data
        rates = data['rates']
        
        # Check if the target currency is present in the rates dictionary
        if target_currency in rates:
            # Return the conversion rate for the target currency
            return rates[target_currency]
        else:
            # Print an error message if the conversion rate for the target currency is not found
            print(f"Conversion rate for {target_currency} not found")
            return None
    else:
        # Print an error message if the 'rates' key is not found in the API response
        print("Rates not found in API response")
        return None

#this method converts the current currency to the target currency using the already gotten conversion
#rate from method 'get_rates'
def convert(amount, user_currency, target_currency):
    rate = get_rates(user_currency, target_currency)
    if rate is not None:
        rate = float(rate) #explicit conversion to float
        # the next line is now obsolete
        # amount = float(amount) #explicit conversion cause it seems it is being treated as a str
        converted_amount = rate * amount
        return converted_amount
    else:
        print("Error: Converion rate not found!")
        return None

