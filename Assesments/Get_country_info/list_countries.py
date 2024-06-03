def list_continent(continent):
    #africa
    if continent.lower() == "africa":
        african_countries = [
            "Algeria", "Angola", "Benin", "Botswana", "Burkina Faso", "Burundi", "Cabo Verde",
            "Cameroon", "Central African Republic", "Chad", "Comoros", "Democratic Republic of the Congo",
            "Republic of the Congo", "Djibouti", "Egypt", "Equatorial Guinea", "Eritrea", "Eswatini",
            "Ethiopia", "Gabon", "Gambia", "Ghana", "Guinea", "Guinea-Bissau", "Ivory Coast", "Kenya",
            "Lesotho", "Liberia", "Libya", "Madagascar", "Malawi", "Mali", "Mauritania", "Mauritius",
            "Morocco", "Mozambique", "Namibia", "Niger", "Nigeria", "Rwanda", "Sao Tome and Principe",
            "Senegal", "Seychelles", "Sierra Leone", "Somalia", "South Africa", "South Sudan", "Sudan",
            "Tanzania", "Togo", "Tunisia", "Uganda", "Zambia", "Zimbabwe"
        ]
        for index, country in enumerate(african_countries, start=1):
            print(f"{index}: {country}")
    #antarctica
    elif continent.lower() == "antarctica":
        antarctica_countries = [
            "Antarctica"
        ]
        for index, country in enumerate(antarctica_countries,start=1):
            print(f"{index}: {country}")
    #south america
    elif continent.lower() == "south america":
        south_american_countries = [
            "Argentina", "Bolivia", "Brazil", "Chile", "Colombia", "Ecuador", "Guyana", 
            "Paraguay", "Peru", "Suriname", "Uruguay", "Venezuela"
        ]
        for index, country in enumerate(south_american_countries, start=1):
            print(f"{index}: {country}")
    #asia
    elif continent.lower() == "asia":
        asian_countries = [
            "Afghanistan", "Armenia", "Azerbaijan", "Bahrain", "Bangladesh", "Bhutan", "Brunei",
            "Cambodia", "China", "Cyprus", "Georgia", "India", "Indonesia", "Iran", "Iraq",
            "Israel", "Japan", "Jordan", "Kazakhstan", "Kuwait", "Kyrgyzstan", "Laos", "Lebanon",
            "Malaysia", "Maldives", "Mongolia", "Myanmar", "Nepal", "North Korea", "Oman", "Pakistan",
            "Palestine", "Philippines", "Qatar", "Russia", "Saudi Arabia", "Singapore", "South Korea",
            "Sri Lanka", "Syria", "Taiwan", "Tajikistan", "Thailand", "Timor-Leste", "Turkey", "Turkmenistan",
            "United Arab Emirates", "Uzbekistan", "Vietnam", "Yemen"
        ]   
        for index, country in enumerate(asian_countries, start=1):
            print(f"{index}: {country}")
    #europe
    elif continent.lower() == "europe":
        european_countries = [
            "Albania", "Andorra", "Austria", "Belarus", "Belgium", "Bosnia and Herzegovina",
            "Bulgaria", "Croatia", "Czech Republic", "Denmark", "Estonia", "Finland", "France",
            "Germany", "Greece", "Hungary", "Iceland", "Ireland", "Italy", "Kosovo", "Latvia",
            "Liechtenstein", "Lithuania", "Luxembourg", "Malta", "Moldova", "Monaco", "Montenegro",
            "Netherlands", "North Macedonia", "Norway", "Poland", "Portugal", "Romania", "San Marino",
            "Serbia", "Slovakia", "Slovenia", "Spain", "Sweden", "Switzerland", "Ukraine", "United Kingdom",
            "Vatican City"
        ]

        for index, country in enumerate(european_countries, start=1):
            print(f"{index}: {country}")
    #north america
    elif continent.lower() == "north america":
        north_american_countries = [
            "Antigua and Barbuda", "Bahamas", "Barbados", "Belize", "Canada", "Costa Rica", "Cuba",
            "Dominica", "Dominican Republic", "El Salvador", "Grenada", "Guatemala", "Haiti", "Honduras",
            "Jamaica", "Mexico", "Nicaragua", "Panama", "Saint Kitts and Nevis", "Saint Lucia", 
            "Saint Vincent and the Grenadines", "Trinidad and Tobago", "United States"
        ]

        for index, country in enumerate(north_american_countries, start=1):
            print(f"{index}: {country}")
    #oceania or australlia
    elif continent.lower() == "oceania" or continent.lower()  == "australia":
        oceania_countries = [
            "Australia", "Fiji", "Kiribati", "Marshall Islands", "Micronesia", "Nauru", "New Zealand",
            "Palau", "Papua New Guinea", "Samoa", "Solomon Islands", "Tonga", "Tuvalu", "Vanuatu"
        ]

        for index, country in enumerate(oceania_countries, start=1):
            print(f"{index}: {country}")




    
