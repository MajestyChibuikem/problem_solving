def main():
    import functions
    import Assesments.Get_country_info.map_names as map_names 
    continent = input("enter continent: Africa, antarctica, Asia, Europe, North America, Australia, South America")


    country = input("country: ")
    country = map_names.country_names(country)
    functions.get_country_info(country)
    
if __name__ == "__main__":
    main()