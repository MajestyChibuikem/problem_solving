import functions

# List of Central Asian countries
central_asian_countries = ["kazakhstan", "kyrgyzstan", "tajikistan", "turkmenistan", "uzbekistan"]

# List of East Asian countries
east_asian_countries = ["china", "japan", "mongolia", "north korea", "south korea"]

# List of South Asian countries
south_asian_countries = ["afghanistan", "bangladesh", "bhutan", "india", "maldives", "nepal", "pakistan", "sri lanka"]

# List of Southeast Asian countries
southeast_asian_countries = ["brunei", "cambodia", "east timor", "indonesia", "laos", "malaysia", "myanmar", "philippines", "singapore", "thailand", "vietnam"]

# List of Western Asian countries
western_asian_countries = ["armenia", "azerbaijan", "bahrain", "cyprus", "georgia", "iraq", "israel", "jordan", "kuwait", "lebanon", "oman", "qatar", "saudi arabia", "syria", "turkey", "united arab emirates", "yemen"]


def switch_country(country):
    # Complete switch_country function for Central Asian countries
    if country.lower() in central_asian_countries:
        if country.lower() == "kazakhstan":
            url = KZ()
            return url
        elif country.lower() == "kyrgyzstan":
            url = KG()
            return url
        elif country.lower() == "tajikistan":
            url = TJ()
            return url
        elif country.lower() == "turkmenistan":
            url = TM()
            return url
        elif country.lower() == "uzbekistan":
            url = UZ()
            return url

    # Add more East Asian countries similarly...
    elif country.lower() in east_asian_countries:
        if country.lower() == "china":
            url = CN()
            return url
        elif country.lower() == "japan":
            url = JP()
            return url
        elif country.lower() == "mongolia":
            url = MN()
            return url
        elif country.lower() == "north korea":
            url = KP()
            return url
        elif country.lower() == "south korea":
            url = KR()
            return url

    # Add more South Asian countries similarly...
    elif country.lower() in south_asian_countries:
        if country.lower() == "afghanistan":
            url = AF()
            return url
        elif country.lower() == "bangladesh":
            url = BD()
            return url
        elif country.lower() == "bhutan":
            url = BT()
            return url
        elif country.lower() == "india":
            url = IN()
            return url
        elif country.lower() == "maldives":
            url = MV()
            return url
        elif country.lower() == "nepal":
            url = NP()
            return url
        elif country.lower() == "pakistan":
            url = PK()
            return url
        elif country.lower() == "sri lanka":
            url = LK()
            return url

    # Add more Southeast Asian countries similarly...
    elif country.lower() in southeast_asian_countries:
        if country.lower() == "brunei":
            url = BN()
            return url
        elif country.lower() == "cambodia":
            url = KH()
            return url
        elif country.lower() == "east timor":
            url = TL()
            return url
        elif country.lower() == "indonesia":
            url = ID()
            return url
        elif country.lower() == "laos":
            url = LA()
            return url
        elif country.lower() == "malaysia":
            url = MY()
            return url
        elif country.lower() == "myanmar":
            url = MM()
            return url
        elif country.lower() == "philippines":
            url = PH()
            return url
        elif country.lower() == "singapore":
            url = SG()
            return url
        elif country.lower() == "thailand":
            url = TH()
            return url
        elif country.lower() == "vietnam":
            url = VN()
            return url

        
    # Add more Western Asian countries similarly...
    elif country.lower() in western_asian_countries:
        if country.lower() == "armenia":
            url = AM()
            return url
        elif country.lower() == "azerbaijan":
            url = AZ()
            return url
        elif country.lower() == "bahrain":
            url = BH()
            return url
        elif country.lower() == "cyprus":
            url = CY()
            return url
        elif country.lower() == "georgia":
            url = GE()
            return url
        elif country.lower() == "iraq":
            url = IQ()
            return url
        elif country.lower() == "israel":
            url = IL()
            return url
        elif country.lower() == "jordan":
            url = JO()
            return url
        elif country.lower() == "kuwait":
            url = KW()
            return url
        elif country.lower() == "lebanon":
            url = LB()
            return url
        elif country.lower() == "oman":
            url = OM()
            return url
        elif country.lower() == "qatar":
            url = QA()
            return url
        elif country.lower() == "saudi arabia":
            url = SA()
            return url
        elif country.lower() == "syria":
            url = SY()
            return url
        elif country.lower() == "turkey":
            url = TR()
            return url
        elif country.lower() == "united arab emirates":
            url = AE()
            return url
        elif country.lower() == "yemen":
            url = YE()
            return url


    else:
        url = "URL not available for this country"
        return url
# Define functions to return URLs for each country

# Example functions:
# Central Asian countries
# Kazakhstan
def KZ():
    url = functions.load_url("Assesments/Get_country_info/country_urls/asia/KZ_details.txt")
    return url

# Kyrgyzstan
def KG():
    url = functions.load_url("Assesments/Get_country_info/country_urls/asia/KG_details.txt")
    return url

# Tajikistan
def TJ():
    url = functions.load_url("Assesments/Get_country_info/country_urls/asia/TJ_details.txt")
    return url

# Turkmenistan
def TM():
    url = functions.load_url("Assesments/Get_country_info/country_urls/asia/TM_details.txt")
    return url

# Uzbekistan
def UZ():
    url = functions.load_url("Assesments/Get_country_info/country_urls/asia/UZ_details.txt")
    return url

# China
def CN():
    url = functions.load_url("Assesments/Get_country_info/country_urls/asia/CN_details.txt")
    return url

# Japan
def JP():
    url = functions.load_url("Assesments/Get_country_info/country_urls/asia/JP_details.txt")
    return url

# South Korea
def KR():
    url = functions.load_url("Assesments/Get_country_info/country_urls/asia/KR_details.txt")
    return url

# Mongolia
def MN():
    url = functions.load_url("Assesments/Get_country_info/country_urls/asia/MN_details.txt")
    return url

# North Korea
def KP():
    url = functions.load_url("Assesments/Get_country_info/country_urls/asia/KP_details.txt")
    return url

# Afghanistan
def AF():
    url = functions.load_url("Assesments/Get_country_info/country_urls/asia/AF_details.txt")
    return url

# Bangladesh
def BD():
    url = functions.load_url("Assesments/Get_country_info/country_urls/asia/BD_details.txt")
    return url

# Bhutan
def BT():
    url = functions.load_url("Assesments/Get_country_info/country_urls/asia/BT_details.txt")
    return url

# India
def IN():
    url = functions.load_url("Assesments/Get_country_info/country_urls/asia/IN_details.txt")
    return url

# Iran
def IR():
    url = functions.load_url("Assesments/Get_country_info/country_urls/asia/IR_details.txt")
    return url

# Sri Lanka
def LK():
    url = functions.load_url("Assesments/Get_country_info/country_urls/asia/LK_details.txt")
    return url

# Maldives
def MV():
    url = functions.load_url("Assesments/Get_country_info/country_urls/asia/MV_details.txt")
    return url

# Nepal
def NP():
    url = functions.load_url("Assesments/Get_country_info/country_urls/asia/NP_details.txt")
    return url

# Pakistan
def PK():
    url = functions.load_url("Assesments/Get_country_info/country_urls/asia/PK_details.txt")
    return url

# Palestine
def PN():
    url = functions.load_url("Assesments/Get_country_info/country_urls/asia/PN_details.txt")
    return url

# Brunei
def BN():
    url = functions.load_url("Assesments/Get_country_info/country_urls/asia/BN_details.txt")
    return url

# Cambodia
def KH():
    url = functions.load_url("Assesments/Get_country_info/country_urls/asia/KH_details.txt")
    return url

# Indonesia
def ID():
    url = functions.load_url("Assesments/Get_country_info/country_urls/asia/ID_details.txt")
    return url

# Laos
def LA():
    url = functions.load_url("Assesments/Get_country_info/country_urls/asia/LA_details.txt")
    return url

# Malaysia
def MY():
    url = functions.load_url("Assesments/Get_country_info/country_urls/asia/MY_details.txt")
    return url

# Myanmar
def MM():
    url = functions.load_url("Assesments/Get_country_info/country_urls/asia/MM_details.txt")
    return url

# Philippines
def PH():
    url = functions.load_url("Assesments/Get_country_info/country_urls/asia/PH_details.txt")
    return url

# Singapore
def SG():
    url = functions.load_url("Assesments/Get_country_info/country_urls/asia/SG_details.txt")
    return url

# Thailand
def TH():
    url = functions.load_url("Assesments/Get_country_info/country_urls/asia/TH_details.txt")
    return url

# Timor-Leste
def TL():
    url = functions.load_url("Assesments/Get_country_info/country_urls/asia/TL_details.txt")
    return url

# Vietnam
def VN():
    url = functions.load_url("Assesments/Get_country_info/country_urls/asia/VN_details.txt")
    return url

# Armenia
def AM():
    url = functions.load_url("Assesments/Get_country_info/country_urls/asia/AM_details.txt")
    return url

# Azerbaijan
def AZ():
    url = functions.load_url("Assesments/Get_country_info/country_urls/asia/AZ_details.txt")
    return url

# Bahrain
def BH():
    url = functions.load_url("Assesments/Get_country_info/country_urls/asia/BH_details.txt")
    return url

# Cyprus
def CY():
    url = functions.load_url("Assesments/Get_country_info/country_urls/asia/CY_details.txt")
    return url

# Georgia
def GE():
    url = functions.load_url("Assesments/Get_country_info/country_urls/asia/GE_details.txt")
    return url

# Iraq
def IQ():
    url = functions.load_url("Assesments/Get_country_info/country_urls/asia/IQ_details.txt")
    return url

# Israel
def IL():
    url = functions.load_url("Assesments/Get_country_info/country_urls/asia/IL_details.txt")
    return url

# Jordan
def JO():
    url = functions.load_url("Assesments/Get_country_info/country_urls/asia/JO_details.txt")
    return url

# Kuwait
def KW():
    url = functions.load_url("Assesments/Get_country_info/country_urls/asia/KW_details.txt")
    return url

# Lebanon
def LB():
    url = functions.load_url("Assesments/Get_country_info/country_urls/asia/LB_details.txt")
    return url

# Oman
def OM():
    url = functions.load_url("Assesments/Get_country_info/country_urls/asia/OM_details.txt")
    return url

# Qatar
def QA():
    url = functions.load_url("Assesments/Get_country_info/country_urls/asia/QA_details.txt")
    return url

# Saudi Arabia
def SA():
    url = functions.load_url("Assesments/Get_country_info/country_urls/asia/SA_details.txt")
    return url

# Syria
def SY():
    url = functions.load_url("Assesments/Get_country_info/country_urls/asia/SY_details.txt")
    return url

# Turkey
def TR():
    url = functions.load_url("Assesments/Get_country_info/country_urls/asia/TR_details.txt")
    return url

# United Arab Emirates
def AE():
    url = functions.load_url("Assesments/Get_country_info/country_urls/asia/AE_details.txt")
    return url

# Yemen
def YE():
    url = functions.load_url("Assesments/Get_country_info/country_urls/asia/YE_details.txt")
    return url
