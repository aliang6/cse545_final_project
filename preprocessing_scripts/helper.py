import json
import rasterio
import rasterio.features
import rasterio.warp
import pycountry
import constants

# Format the key based off the row and col
def getKey(row, col):
    return str(row) + "," + str(col)

# Retrieve the key name, which is the crop and its associated feature, based off the directory folder's name
def retrieve_key_from_dir(dir):
    return (dir.split('/')[-1]).split('.')[0]

# Retrieve the tuple (row, col) from the key
def retrieve_row_col(key):
    row_col = key.split(',')
    return (int(row_col[0]), int(row_col[1]))

# Script to retrieve country code of African countries
def retrieve_african_country_codes():
    african_country_code = []
    for country in constants.AFRICAN_COUNTRIES:
        print(country)
        temp = pycountry.countries.get(name=country)
        african_country_code.append(temp.alpha_2.upper())
    print(african_country_code)

# Update the file with new data
def update_data_file(processed_data, processed_data_file):
    processed_data_file.seek(0)
    # json.dump(processed_data, processed_data_file, indent = 4, separators = (',', ':')) # Pretty print
    json.dump(processed_data, processed_data_file)
    processed_data_file.truncate()

# Initialize the data file
# Percentage indicates the percentage of coordinates to use
def initialize_data(coordinates, output_file, percentage):
    data = {}
    scale = int(1/percentage)
    count = 0
    num_lines = 0
    for line in coordinates:
        if count % scale != 0:
            count += 1
            continue
        row = int(line[0])
        col = int(line[1])
        country_code = str(line[2])
        country = str(line[3])
        key = getKey(row, col) # Keys are of the form "row,col"
        if country_code in constants.COMPLETE_COUNTRIES:
            # Populate the entries with their corresponding countries and country codes
            data[key] = {
                'country': country,
                'country_code': country_code,
            }
        count += 1
        num_lines += 1
    with open(output_file, 'w') as outfile:
        json.dump(data, outfile)
    print('Data initialized')
    print('%d lines' % num_lines)

# Populate the data file with the food availability data based off their country code
def populate_food_availability(data_file):
    with open(constants.FOOD_AVAIL_FILE) as f, open(data_file, 'r+') as processed_data_file:
        food_avail = json.loads(f.read())
        processed_data = json.loads(processed_data_file.read())
        for k, v in processed_data.items(): 
            country_code = v['country_code'].upper()
            food_avail_value = food_avail[country_code]
            v.update({
                'food_availability_per_capita': food_avail_value
            })

        update_data_file(processed_data, processed_data_file)
    print('Food availability data populated')

# Retrieve the list of filenames corresponding to the geotiffs for the crops
def generateFileNames(crop):
    dirs = []
    for file_name in constants.GEOTIFF_SUBDIRECTORIES:
        directory = constants.GEOTIFF_DIRECTORY + str(crop) + '/' + str(crop) + file_name
        dirs.append(directory)
    return dirs

# Populate the data for all crops and their respective features
def populate_crop_data(crop_list, data_file):
    with open(data_file, 'r+') as processed_data_file:
        processed_data = json.loads(processed_data_file.read())
        for crop in crop_list:
            print('Populating %s data' % crop)
            dirs = generateFileNames(crop)

            for dir in dirs:
                with rasterio.open(dir) as dataset:
                    band1 = dataset.read(1)
                    value_key = retrieve_key_from_dir(dir)
                    
                    for k in processed_data.keys(): 
                        (row, col) = retrieve_row_col(k)
                        processed_data[k].update({
                            value_key: float(band1[row][col])
                        })

        update_data_file(processed_data, processed_data_file)
   