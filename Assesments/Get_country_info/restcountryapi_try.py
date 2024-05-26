import requests


# this restcountries is too slow!!
def get_country_info(country):
    
    url = f"https://restcountries.com/v3.1/name/{country}"

    
    response = requests.get(url)

    # Check if the request was successful 
    if response.status_code == 200:
        # Extract country details from the JSON response
        country_data = response.json()

        # Print country details
        print("Country Details:")
        print("----------------")
        print(f"Name: {country_data[0]['name']['common']}")
        print(f"Capital: {country_data[0]['capital'][0]}")
        print(f"Population: {country_data[0]['population']}")
        print(f"Area: {country_data[0]['area']} square kilometers")
        print(f"Region: {country_data[0]['region']}")
        print(f"Subregion: {country_data[0]['subregion']}")
        print(f"Languages: {', '.join(country_data[0]['languages'].keys())}")
    else:
        # Print error message if request fails
        print("Error: Unable to fetch country details.")

def main():
    country_name = input("Enter a country name: ")

    
    get_country_info(country_name)

if __name__ == "__main__":
    main()
