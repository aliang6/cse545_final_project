import rasterio
import rasterio.features
import rasterio.warp
import pycountry
import reverse_geocoder as rg
import time
import csv
import constants

# Retrieve the array rows and cols in the geotiff files that are associated with African countries
# Store the values in the 
if __name__ == "__main__":
    data = {}

    with rasterio.open('../data/HarvestedAreaYield175Crops_Geotiff/GeoTiff/apple/apple_DataQuality_HarvestedArea.tif') as dataset:
        with open(constants.AFRICAN_COORD_FILE, mode='w') as coordinate_file:
            writer = csv.writer(coordinate_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

        band1 = dataset.read(1) # Retrieve geotiff 2D array

        # Longitude and latitude values for the corners of Africa's bounding rectangle
        # Used to find the corresponding row and col values in the 2D array
        '''top_left_x = -26.367188
        top_left_y = 37.373431
        bottom_right_x = 60.117187
        bottom_right_y = -37.786996
        x1, y1 = dataset.index(top_left_x, top_left_y)
        x2, y2 = dataset.index(bottom_right_x, bottom_right_y)'''

        # Tighter bounds on rows and columns found using the latitude and longitude from the above values
        top_row = 625
        bottom_row = 1500
        left_col = 1880
        right_col = 2860

        # If row_scale * col_scale = n, then we only take every nth data point
        row_scale = 2
        col_scale = 3

        # Traverse the 2D array and record all data points, with respect to the scale, that reside within the African continent
        for row in range(int(top_row/row_scale), int(bottom_row/row_scale)):
            for col in range(int(left_col/col_scale), int(right_col/col_scale)):
                count += 1
                print(count)
                coordinates = dataset.xy(row*row_scale, col*col_scale)
                coordinates = (coordinates[1], coordinates[0])
                results = rg.search(coordinates)
                country_code = results[0]['cc'].upper()
                country = pycountry.countries.get(alpha_2=country_code).name
                if country_code in constants.AFRICAN_COUNTRY_CODES:
                    writer.writerow([row, col, country_code, country])