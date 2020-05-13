import json
import pycountry
import csv
import numpy as np
import constants

# Retrieve alternate names of countries with characters that are not in utf-8
def alt_country_names(country): 
    alt_names = {
        'Ivory Coast': 'Côte d\'Ivoire'
    }
    return alt_names.get(country, "Invalid")

# Retrieve the average food availability from 1997 - 2003 for African countries that have sufficient data
if __name__ == "__main__":
    data = {}
    other_countries = set()
    with open('../data/gfa25.csv') as food_avail_file: # gfa25.csv contains the raw data
        next(food_avail_file) # Skip the first line

        reader = csv.reader(food_avail_file, delimiter=',')
        for line in reader:
            country = line[0]
            temp = pycountry.countries.get(name=country) # Use pycountry to retrieve the alpha_2 country code
            if temp is None and \
                country in constants.AFRICAN_COUNTRIES_ALT:
                country = alt_country_names(country)
                temp = pycountry.countries.get(name=country)
            try: 
                country_code = temp.alpha_2.upper()            
            except:
                other_countries.add(country)
                continue

            if country_code in constants.AFRICAN_COUNTRY_CODES:
                commodity = str(line[1])
                item = str(line[2])
                year = int(line[4])
                amount = float(line[5])
                if year >= 1997 and \
                    year <= 2003 and \
                    commodity == 'Total Grains/Cereals and Root Crops (R&T)' and \
                    item == 'Food Availability per capita': 
                    if country_code not in data:
                        data[country_code] = []
                    data[country_code].append(amount) 
            else:
                other_countries.add(country)

        for entry in data:
            arr = data[entry]
            data[entry] = np.mean(arr) # Calculate the average of the food availabilities throughout the years 1997 - 2003
        
        # Food availability data is stored in constants.FOOD_AVAIL_FILE
        with open(constants.FOOD_AVAIL_FILE, 'w') as outfile:
            json.dump(data, outfile)

        # Other countries or African countries with insufficient data are put in country_names.txt file
        # Mainly used for debugging
        with open('country_names.txt', 'w') as outfile:
            json.dump(list(other_countries), outfile)

        # Missing African countries are printed onto the console (also used for debugging)
        missing = []
        for c in constants.AFRICAN_COUNTRIES:
            if c not in data.keys():
                missing.append(c)


        print('\nCountries with Insufficient Data:')
        print(missing)