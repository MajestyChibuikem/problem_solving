#mapping keys to the respective names
import Assesments.Get_country_info.country_switching.africa as africa
import Assesments.Get_country_info.country_switching.asia as asia
import Assesments.Get_country_info.country_switching.north_america as north_america
import Assesments.Get_country_info.country_switching.south_america as south_america
import Assesments.Get_country_info.country_switching.australia as australia
import Assesments.Get_country_info.country_switching.antarctica as antarctica
import Assesments.Get_country_info.country_switching.europe as europe
country_names = {
    "Benin": africa.BJ,
    "BJ": africa.BJ,
    "Botswana": africa.BW,
    "BW": africa.BW,
    "Burkina Faso": africa.BF,
    "BF": africa.BF,
    "Burundi": africa.BI,
    "BI": africa.BI,
    "Cabo Verde": africa.CV,
    "CV": africa.CV,
    "Cameroon": africa.CM,
    "CM": africa.CM,
    "Central African Republic": africa.CF,
    "CF": africa.CF,
    "Chad": africa.TD,
    "TD": africa.TD,
    "Comoros": africa.KM,
    "KM": africa.KM,
    "Democratic Republic of the Congo": africa.CD,
    "CD": africa.CD,
    "Republic of the Congo": africa.CG,
    "CG": africa.CG,
    "Djibouti": africa.DJ,
    "DJ": africa.DJ,
    "Egypt": africa.EG,
    "EG": africa.EG,
    "Equatorial Guinea": africa.GQ,
    "GQ": africa.GQ,
    "Eritrea": africa.ER,
    "ER": africa.ER,
    "Eswatini": africa.SZ,
    "SZ": africa.SZ,
    "Ethiopia": africa.ET,
    "ET": africa.ET,
    "Gabon": africa.GA,
    "GA": africa.GA,
    "Gambia": africa.GM,
    "GM": africa.GM,
    "Ghana": africa.GH,
    "GH": africa.GH,
    "Guinea": africa.GN,
    "GN": africa.GN,
    "Guinea-Bissau": africa.GW,
    "GW": africa.GW,
    "Ivory Coast": africa.CI,
    "CI": africa.CI,
    "Kenya": africa.KE,
    "KE": africa.KE,
    "Lesotho": africa.LS,
    "LS": africa.LS,
    "Liberia": africa.LR,
    "LR": africa.LR,
    "Libya": africa.LY,
    "LY": africa.LY,
    "Madagascar": africa.MG,
    "MG": africa.MG,
    "Malawi": africa.MW,
    "MW": africa.MW,
    "Mali": africa.ML,
    "ML": africa.ML,
    "Mauritania": africa.MR,
    "MR": africa.MR,
    "Mauritius": africa.MU,
    "MU": africa.MU,
    "Morocco": africa.MA,
    "MA": africa.MA,
    "Mozambique": africa.MZ,
    "MZ": africa.MZ,
    "Namibia": africa.NA,
    "NA": africa.NA,
    "Niger": africa.NE,
    "NE": africa.NE,
    "Nigeria": africa.NG,
    "NG": africa.NG,
    "Rwanda": africa.RW,
    "RW": africa.RW,
    "Sao Tome and Principe": africa.ST,
    "ST": africa.ST,
    "Senegal": africa.SN,
    "SN": africa.SN,
    "Seychelles": africa.SC,
    "SC": africa.SC,
    "Sierra Leone": africa.SL,
    "SL": africa.SL,
    "Somalia": africa.SO,
    "SO": africa.SO,
    "South Africa": africa.ZA,
    "ZA": africa.ZA,
    "South Sudan": africa.SS,
    "SS": africa.SS,
    "Sudan": africa.SD,
    "SD": africa.SD,
    "Tanzania": africa.TZ,
    "TZ": africa.TZ,
    "Togo": africa.TG,
    "TG": africa.TG,
    "Tunisia": africa.TN,
    "TN": africa.TN,
    "Uganda": africa.UG,
    "UG": africa.UG,
    "Zambia": africa.ZM,
    "ZM": africa.ZM,
    "Zimbabwe": africa.ZW,
    "ZW": africa.ZW,
    #asian countries
    "Afghanistan": asia.AF,
    "AF": asia.AF,
    "Armenia": asia.AM,
    "AM": asia.AM,
    "Azerbaijan": asia.AZ,
    "AZ": asia.AZ,
    "Bahrain": asia.BH,
    "BH": asia.BH,
    "Bangladesh": asia.BD,
    "BD": asia.BD,
    "Bhutan": asia.BT,
    "BT": asia.BT,
    "Brunei": asia.BN,
    "BN": asia.BN,
    "Cambodia": asia.KH,
    "KH": asia.KH,
    "China": asia.CN,
    "CN": asia.CN,
    "Cyprus": asia.CY,
    "CY": asia.CY,
    "Georgia": asia.GE,
    "GE": asia.GE,
    "India": asia.IN,
    "IN": asia.IN,
    "Indonesia": asia.ID,
    "ID": asia.ID,
    "Iran": asia.IR,
    "IR": asia.IR,
    "Iraq": asia.IQ,
    "IQ": asia.IQ,
    "Israel": asia.IL,
    "IL": asia.IL,
    "Japan": asia.JP,
    "JP": asia.JP,
    "Jordan": asia.JO,
    "JO": asia.JO,
    "Kazakhstan": asia.KZ,
    "KZ": asia.KZ,
    "Kuwait": asia.KW,
    "KW": asia.KW,
    "Kyrgyzstan": asia.KG,
    "KG": asia.KG,
    "Laos": asia.LA,
    "LA": asia.LA,
    "Lebanon": asia.LB,
    "LB": asia.LB,
    "Malaysia": asia.MY,
    "MY": asia.MY,
    "Maldives": asia.MV,
    "MV": asia.MV,
    "Mongolia": asia.MN,
    "MN": asia.MN,
    "Myanmar": asia.MM,
    "MM": asia.MM,
    "Nepal": asia.NP,
    "NP": asia.NP,
    "North Korea": asia.KP,
    "KP": asia.KP,
    "Oman": asia.OM,
    "OM": asia.OM,
    "Pakistan": asia.PK,
    "PK": asia.PK,
    "Palestine": asia.PS,
    "PS": asia.PS,
    "Philippines": asia.PH,
    "PH": asia.PH,
    "Qatar": asia.QA,
    "QA": asia.QA,
    "Saudi Arabia": asia.SA,
    "SA": asia.SA,
    "Singapore": asia.SG,
    "SG": asia.SG,
    "South Korea": asia.KR,
    "KR": asia.KR,
    "Sri Lanka": asia.LK,
    "LK": asia.LK,
    "Syria": asia.SY,
    "SY": asia.SY,
    "Taiwan": asia.TW,
    "TW": asia.TW,
    "Tajikistan": asia.TJ,
    "TJ": asia.TJ,
    "Thailand": asia.TH,
    "TH": asia.TH,
    "Timor-Leste": asia.TL,
    "TL": asia.TL,
    "Turkey": asia.TR,
    "TR": asia.TR,
    "Turkmenistan": asia.TM,
    "TM": asia.TM,
    "United Arab Emirates": asia.AE,
    "AE": asia.AE,
    "Uzbekistan": asia.UZ,
    "UZ": asia.UZ,
    "Vietnam": asia.VN,
    "VN": asia.VN,
    "Yemen": asia.YE,
    "YE": asia.YE,
    #north america
    "US": north_america.US,
    "united states" : north_america.US,
    "CA": north_america.CA,

    "MX": north_america.MX,
    "GT": north_america.GT,
    "CU": north_america.CU,
    "HT": north_america.HT,
    "DO": north_america.DO,
    "JM": north_america.JM,
    "BZ": north_america.BZ,
    "CR": north_america.CR,
    "PA": north_america.PA,
    "BS": north_america.BS,
    "NI": north_america.NI,
    "HN": north_america.HN,
    "SV": north_america.SV,
    "BB": north_america.BB,
    "GD": north_america.GD,
    "DM": north_america.DM,
    "TT": north_america.TT,
    "KN": north_america.KN,
    "LC": north_america.LC,
    "VC": north_america.VC,
    "AG": north_america.AG,
    #south american countries
    "AR": south_america.AR,
    "BO": south_america.BO,
    "BR": south_america.BR,
    "CL": south_america.CL,
    "CO": south_america.CO,
    "EC": south_america.EC,
    "GY": south_america.GY,
    "PY": south_america.PY,
    "PE": south_america.PE,
    "SR": south_america.SR,
    "UY": south_america.UY,
    "VE": south_america.VE,
    #australian countries
    "AU": australia.AU,
    "FJ": australia.FJ,
    "KI": australia.KI,
    "MH": australia.MH,
    "FM": australia.FM,
    "NR": australia.NR,
    "NZ": australia.NZ,
    "PW": australia.PW,
    "PG": australia.PG,
    "WS": australia.WS,
    "SB": australia.SB,
    "TO": australia.TO,
    "TV": australia.TV,
    "VU": australia.VU,
    #european countries
    "AL": europe.AL,
    "albania" : europe.AL,
    "AD": europe.AD,
    "andorra" : europe.AD,
    "AM": europe.AM,
    "AT": europe.AT,
    "AZ": europe.AZ,
    "BY": europe.BY,
    "BE": europe.BE,
    "BA": europe.BA,
    "BG": europe.BG,
    "HR": europe.HR,
    "CY": europe.CY,
    "CZ": europe.CZ,
    "DK": europe.DK,
    "EE": europe.EE,
    "FI": europe.FI,
    "FR": europe.FR,
    "GE": europe.GE,
    "DE": europe.DE,
    "GR": europe.GR,
    "HU": europe.HU,
    "IS": europe.IS,
    "IE": europe.IE,
    "IT": europe.IT,
    "KZ": europe.KZ,
    "LV": europe.LV,
    "LT": europe.LT,
    "LU": europe.LU,
    "MK": europe.MK,
    "MT": europe.MT,
    "MD": europe.MD,
    "MC": europe.MC,
    "ME": europe.ME,
    "NL": europe.NL,
    "NO": europe.NO,
    "PL": europe.PL,
    "PT": europe.PT,
    "RO": europe.RO,
    "RU": europe.RU,
    "SM": europe.SM,
    "RS": europe.RS,
    "SK": europe.SK,
    "SI": europe.SI,
    "ES": europe.ES,
    "SE": europe.SE,
    "CH": europe.CH,
    "TR": europe.TR,
    "UA": europe.UA,
    "GB": europe.GB,
    "VA": europe.VA
}





north_american_keys = {
    
}

australian_country_urls = {
   
}

antarctica_countries = {
    "antarctica" : antarctica.whatitis
}
south_america_country_urls = {
    
}

europe_country_urls = {
    
}