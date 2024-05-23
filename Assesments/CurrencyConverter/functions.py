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
            return float(user_input)
            break
        else:
            print("Incorrect format, Please try again: ")
    pass

#this method check for non-string input
#and keeps looping till correct format is given
def str_check(user_input):
    while True:
        if user_input.isdigit():
            print("Wrong input format, try again: ")
        else:
            return (user_input)


#this method gets the rates from the passed url using the api keys accessed
def get_rates(user_currency, target_currency):
    api_key = load_api("Assesments/CurrencyConverter/apikeys")
    url = f'https://open.er-api.com/v6/latest/{user_currency}'

    #map app_id to api_key
    params = {'app_id':api_key}

    #make a http get request to the open exchange market using the passed url and the read api
    response = requests.get(url, params=params)

    #converts json content to python dictionarys
    data = response.json()

    #if error in recieved data
    if 'error' in data:
        print("Error:", data['description'])
        return None
    
    rates = data['rates']
    if target_currency in  rates:
        return rates[target_currency]
    else:
        print("conversion rate for {target_currency} not found")
        return None
    

#this method converts the current currenct to the target currency using the already gotten conversion
#rate from method 'get_rates'
def convert(amount, user_currency, target_currency):
    rate = get_rates(user_currency, target_currency)
    if rate is not None:
        converted_amount = rate * amount
        return converted_amount