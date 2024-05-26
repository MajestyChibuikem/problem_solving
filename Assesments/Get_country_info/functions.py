#to import the requests module and allow requests in the script
import requests
import json

#this method loads the api keys from the api file
def load_api_keys(file_path):
    with open(file_path, "r") as f:
        return json.load(f)
    

def load_url(file_path):
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

# Load API keys from JSON file
api_keys = load_api_keys("Assesments/Get_country_info/apikey.json")
url = load_url("Assesments/Get_country_info/details_url.txt")
# details_url = load_url("Assesments/Get_country_info/details_url.txt")
# Extract RapidAPI keys
rapidapi_keys = api_keys.get("rapidapi",{})

# Extract RapidAPI key and host
rapidapi_key = rapidapi_keys.get("X-RapidAPI-Key")
rapidapi_host = rapidapi_keys.get("X-RapidAPI-Host")

def get_country_info(country):
    api_url = f"{url}?country={country}"

    querystring = {"namePrefix":"N"}
    headers = {
        "X-RapidAPI-Key": rapidapi_key,
        "X-RapidAPI-Host": rapidapi_host
    }


    response = requests.get(api_url, headers=headers)
    # response = requests.get(api_url, headers=headers, params=querystring)

    print(response.json())