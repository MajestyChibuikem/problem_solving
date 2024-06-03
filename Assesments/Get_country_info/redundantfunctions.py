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