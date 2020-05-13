import csv
import constants
import helper
import os

if __name__ == "__main__":
    # Retrieve coordinates of Africa, preprocessed using retrieve_coordinates
    coordinates = csv.reader(open(constants.AFRICAN_COORD_FILE), delimiter=',') 

    # Initialize the data file
    helper.initialize_data(coordinates, constants.PROCESSED_DATE_FILE, 0.007) # 1 for all ~ 3GB; .001 for ~ 5MB 

    # Populate food availability into the specified data file
    helper.populate_food_availability(constants.PROCESSED_DATE_FILE)

    # Retrieve crop folder names and populate the data file with crop data
    crop_dirs = [d for d in os.listdir(constants.GEOTIFF_DIRECTORY) if os.path.isdir(os.path.join(constants.GEOTIFF_DIRECTORY, d))]
    helper.populate_crop_data(crop_dirs, constants.PROCESSED_DATE_FILE)

    print('Data file complete')