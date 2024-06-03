import functions
import map_names


def switch_country(country):
    url = map_names.country_names()
    """
    this if-else statement doesn't really seem useful since there
    is already a mapped diction
    """
    if country.lower() == "nigeria" or country.lower() == "ng":
        url = NG()
        return url
    elif country.lower() == "algeria" or country.lower() == "dz":
        url = DZ()
    elif country.lower() == "angola" or country.lower() == "ao":
        url = AO()
        return url
    elif country.lower() == "benin" or country.lower() == "bj":
        url = BJ()
        return url
    elif country.lower() == "botswana" or country.lower() == "bw":
        url = BW()
        return url
    elif country.lower() == "burkina faso" or country.lower() == "bf":
        url = BF()
        return url
    elif country.lower() == "burundi" or country.lower() == "bi":
        url = BI()
        return url
    elif country.lower() == "cabo verde" or country.lower() == "cv":
        url = CV()
        return url
    elif country.lower() == "cameroon" or country.lower() == "cm":
        url = CM()
        return url
    
    elif country.lower() == "central african republic" or country.lower() == "cf":
        url = CF()
        return url
    
    elif country.lower() == "chad" or country.lower() == "td":
        url = TD()
        return url
    
    elif country.lower() == "comoros" or country.lower() == "km":
        url = CD()
        return url
    
    elif country.lower() == "democratic republic of the congo" or country.lower() == "cd":
        url = CD()
        return url
    
    elif country.lower() == "republic of the congo" or country.lower() == "cg":
        url = CG()
        return url
    
    elif country.lower() == "djibouti" or country.lower() == "dj":
        url = DJ()
        return url
    
    elif country.lower() == "egypt" or country.lower() == "eg":
        url = EG()
        return url
    
    elif country.lower() == "equatorial guinea" or country.lower() == "gq":
        url = GQ()
        return url
    
    elif country.lower() == "eritrea" or country.lower() == "er":
        url = ER()
        return url
    
    elif country.lower() == "Eswatini" or country.lower() == "sz":
        url = SZ()
        return url
    
    elif country.lower() == "ethiopia" or country.lower() == "et":
        url = ET()
        return url
    
    elif country.lower() == "gabon" or country.lower() == "ga":
        url = GA()
        return url
    
    elif country.lower() == "gambia" or country.lower() == "gm":
        url = GM()
        return url
    elif country.lower() == "ghana" or country.lower() == "gh":
        url = GH()
        return url
    elif country.lower() == "guinea" or country.lower() == "gn":
        url = GN()
        return url
    elif country.lower() == "guinea-bissau" or country.lower() == "gw":
        url = GN()
        return url
    elif country.lower() == "ivory coast" or country.lower() == "ci":
        url = CI()
        return url
    elif country.lower() == "kenya" or country.lower() == "ke":
        url = KE()
        return url
    elif country.lower() == "lesotho" or country.lower() == "ls":
        url = LS()
        return url
    elif country.lower() == "liberia" or country.lower() == "lr":
        url = LR()
        return url
    elif country.lower() == "libya" or country.lower() == "ly":
        url = LY()
        return url
    elif country.lower() == "madagascar" or country.lower() == "mg":
        url = MG()
        return url
    elif country.lower() == "malawi" or country.lower() == "mw":
        url = MW()
        return url
    elif country.lower() == "mali" or country.lower() == "ml":
        url = ML()
        return url
    elif country.lower() == "mauritania" or country.lower() == "mr":
        url = MR()
        return url
    elif country.lower() == "mauritius" or country.lower() == "mu":
        url = MU()
        return url
    elif country.lower() == "morcco" or country.lower() == "ma":
        url = MA()
        return url
    elif country.lower() == "mozambique" or country.lower() == "mz":
        url = MZ()
        return url
    elif country.lower() == "namibia" or country.lower() == "na":
        url = NA()
        return url
    elif country.lower() == "niger" or country.lower() == "ne":
        url = NE()
        return url

    elif country.lower() == "nigeria" or country.lower() == "ng":
        url = NG()
        return url

    elif country.lower() == "rwanda" or country.lower() == "rw":
        url = RW()
        return url

    elif country.lower() == "sao tome and principe" or country.lower() == "st":
        url = ST()
        return url

    elif country.lower() == "senegal" or country.lower() == "sn":
        url = SN()
        return url

    elif country.lower() == "seychelles" or country.lower() == "sc":
        url = SC()
        return url

    elif country.lower() == "sierra leone" or country.lower() == "sl":
        url = SL()
        return url

    elif country.lower() == "somalia" or country.lower() == "so":
        url = SO()
        return url

    elif country.lower() == "south africa" or country.lower() == "za":
        url = ZA()
        return url

    elif country.lower() == "south sudan" or country.lower() == "ss":
        url = SS()
        return url

    elif country.lower() == "sudan" or country.lower() == "sd":
        url = SD()
        return url

    elif country.lower() == "tanzania" or country.lower() == "tz":
        url = TZ()
        return url

    elif country.lower() == "togo" or country.lower() == "tg":
        url = TG()
        return url

    elif country.lower() == "tunisia" or country.lower() == "tn":
        url = TN()
        return url

    elif country.lower() == "uganda" or country.lower() == "ug":
        url = UG()
        return url

    elif country.lower() == "zambia" or country.lower() == "zm":
        url = ZM()
        return url

    elif country.lower() == "zimbabwe" or country.lower() == "zw":
        url = ZW()
        return url

    elif country.lower() == "ethiopia" or country.lower() == "et":
        url = ET()
        return url
"""
African Countries
"""
#Nigeria
def NG():
    url = functions.load_url("Assesments/Get_country_info/country_urls/africa/NG_details.txt")
    return url

#Algeria
def DZ():
    url = functions.load_url("Assesments/Get_country_info/country_urls/africa/DZ_details.txt")
    return url

#Angola
def AO():
    url = functions.load_url("Assesments/Get_country_info/country_urls/africa/AO_details.txt")
    return url

#Benin
def BJ():
    url = functions.load_url("Assesments/Get_country_info/country_urls/africa/BJ_details.txt")
    return url

#botswana
def BW():
    url = functions.load_url("Assesments/Get_country_info/country_urls/africa/BW_details.txts")
    return url
#burkina faso
def BF():
    url = functions.load_url("Assesments/Get_country_info/country_urls/africa/BF_details.txt")
    return url
#burundi
def BI():
    url = functions.load_url("Assesments/Get_country_info/country_urls/africa/BI_details.txt")
    return url

#Cabo Verde
def CV():
    url = functions.load_url("Assesments/Get_country_info/country_urls/africa/CV_details.txt")
    return url

#Cameroon
def CM():
    url = functions.load_url("Assesments/Get_country_info/country_urls/africa/CM_details.txt")
    return url

#Central African Republic
def CF():
    url = functions.load_url("Assesments/Get_country_info/country_urls/africa/CF_details.txt")
    return url
#chad
def TD():
    url = functions.load_url("Assesments/Get_country_info/country_urls/africa/TD_details.txt")
    return url

#Comoros
def KM():
    url = functions.load_url("Assesments/Get_country_info/country_urls/africa/KM_details.txt")
    return url
#Democratic Republic of the Congo
def CD():
    url = functions.load_url("Assesments/Get_country_info/country_urls/africa/CD_details.txt")
    return url
#Republic of the Congo
def CG():
    url = functions.load_url("Assesments/Get_country_info/country_urls/africa/CG_details.txt")
    return url
#Djibouti
def DJ():
    url = functions.load_url("Assesments/Get_country_info/country_urls/africa/DJ_details.txt")
    return url
#Egypt
def EG():
    url = functions.load_url("Assesments/Get_country_info/country_urls/africa/EG_details.txt")
    return url
#Equatorial Guinea
def GQ():
    url = functions.load_url("Assesments/Get_country_info/country_urls/africa/GQ_details.txt")
    return url
#Eritrea
def ER():
    url = functions.load_url("Assesments/Get_country_info/country_urls/africa/ER_details.txt")
    return url
#Eswatini
def SZ():
    url = functions.load_url("Assesments/Get_country_info/country_urls/africa/SZ_details.txt")
    return url
#Ethiopia
def ET():
    url = functions.load_url("Assesments/Get_country_info/country_urls/africa/ET_details.txt")
    return url
#Gabon
def GA():
    url = functions.load_url("Assesments/Get_country_info/country_urls/africa/GA_details.txt")
    return url
#Gambia
def GM():
    url = functions.load_url("Assesments/Get_country_info/country_urls/africa/GM_details.txt")
    return url
#Ghana
def GH():
    url = functions.load_url("Assesments/Get_country_info/country_urls/africa/GH_details.txt")
    return url
#Guinea
def GN():
    url = functions.load_url("Assesments/Get_country_info/country_urls/africa/GN_details.txt")
    return url
#Guinea-Bissau
def GW():
    url = functions.load_url("Assesments/Get_country_info/country_urls/africa/GW_details.txt")
    return url
#Ivory Coast
def CI():
    url = functions.load_url("Assesments/Get_country_info/country_urls/africa/CI_details.txt")
    return url
#Kenya
def KE():
    url = functions.load_url("Assesments/Get_country_info/country_urls/africa/KE_details.txt")
    return url
#Lesotho
def LS():
    url  = functions.load_url("Assesments/Get_country_info/country_urls/africa/LS_details.txt")
    return url
#Liberia
def LR():
    url = functions.load_url("Assesments/Get_country_info/country_urls/africa/LR_details.txt")
    return url
#Libya
def LY():
    url = functions.load_url("Assesments/Get_country_info/country_urls/africa/LY_details.txt")
    return url
#Madagascar
def MG():
    url = functions.load_url("Assesments/Get_country_info/country_urls/africa/MG_details.txt")
    return url
#Malawi
def MW():
    url = functions.load_url("Assesments/Get_country_info/country_urls/africa/MW_details.txt")
    return url
#Mali
def ML():
    url = functions.load_url("Assesments/Get_country_info/country_urls/africa/ML_details.txt")
    return url
#Mauritania
def MR():
    url = functions.load_url("Assesments/Get_country_info/country_urls/africa/MR_details.txt")
    return url
#Mauritius
def MU():
    url = functions.load_url("Assesments/Get_country_info/country_urls/africa/MU_details.txt")
    return url
#Morocco
def MA():
    url = functions.load_url("Assesments/Get_country_info/country_urls/africa/MA_details.txt")
    return url
#Mozambique
def MZ():
    url = functions.load_url("Assesments/Get_country_info/country_urls/africa/MZ_details.txt")
    return url
#Namibia
def NA():
    url = functions.load_url("Assesments/Get_country_info/country_urls/africa/NA_details.txt")
    return url
# Niger
def NE():
    url = functions.load_url("Assesments/Get_country_info/country_urls/africa/NE_details.txt")
    return url

# Nigeria
def NG():
    url = functions.load_url("Assesments/Get_country_info/country_urls/africa/NG_details.txt")
    return url

# Rwanda
def RW():
    url = functions.load_url("Assesments/Get_country_info/country_urls/africa/RW_details.txt")
    return url

# Sao Tome and Principe
def ST():
    url = functions.load_url("Assesments/Get_country_info/country_urls/africa/ST_details.txt")
    return url

# Senegal
def SN():
    url = functions.load_url("Assesments/Get_country_info/country_urls/africa/SN_details.txt")
    return url

# Seychelles
def SC():
    url = functions.load_url("Assesments/Get_country_info/country_urls/africa/SC_details.txt")
    return url

# Sierra Leone
def SL():
    url = functions.load_url("Assesments/Get_country_info/country_urls/africa/SL_details.txt")
    return url

# Somalia
def SO():
    url = functions.load_url("Assesments/Get_country_info/country_urls/africa/SO_details.txt")
    return url

# South Africa
def ZA():
    url = functions.load_url("Assesments/Get_country_info/country_urls/africa/ZA_details.txt")
    return url

# South Sudan
def SS():
    url = functions.load_url("Assesments/Get_country_info/country_urls/africa/SS_details.txt")
    return url

# Sudan
def SD():
    url = functions.load_url("Assesments/Get_country_info/country_urls/africa/SD_details.txt")
    return url

# Tanzania
def TZ():
    url = functions.load_url("Assesments/Get_country_info/country_urls/africa/TZ_details.txt")
    return url

# Togo
def TG():
    url = functions.load_url("Assesments/Get_country_info/country_urls/africa/TG_details.txt")
    return url

# Tunisia
def TN():
    url = functions.load_url("Assesments/Get_country_info/country_urls/africa/TN_details.txt")
    return url

# Uganda
def UG():
    url = functions.load_url("Assesments/Get_country_info/country_urls/africa/UG_details.txt")
    return url

# Zambia
def ZM():
    url = functions.load_url("Assesments/Get_country_info/country_urls/africa/ZM_details.txt")
    return url

# Zimbabwe
def ZW():
    url = functions.load_url("Assesments/Get_country_info/country_urls/africa/ZW_details.txt")
    return url