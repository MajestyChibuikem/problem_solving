import os

# Function to create folder structure
def create_folders():
    #put in your desired continent
    continents = ['south_america']
    countries = {
        'AR': "Argentina",
        'BO': "Bolivia",
        'BR': "Brazil",
        'CL': "Chile",
        'CO': "Colombia",
        'EC': "Ecuador",
        'GY': "Guyana",
        'PY': "Paraguay",
        'PE': "Peru",
        'SR': "Suriname",
        'UY': "Uruguay",
        'VE': "Venezuela",
    }


    for continent in continents:
        continent_path = os.path.join("Assesments/Get_country_info/country_urls", continent)
        if not os.path.exists(continent_path):
            os.makedirs(continent_path)
        for code, country in countries.items():
            file_path = os.path.join(continent_path, f"{code}_details.txt")
            with open(file_path, 'w') as f:
                f.write(f"https://wft-geo-db.p.rapidapi.com/v1/geo/countries/{code}\n")

# Create folders and files
create_folders()
print(os.getcwd())
print("ello")
