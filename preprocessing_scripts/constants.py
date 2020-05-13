PROCESSED_DATE_FILE = 'data.json'

AFRICAN_COORD_FILE = 'africa_coordinates.csv'

FOOD_AVAIL_FILE = 'food_availability.json'

CROPS = ['apple', 'oilseednes', 'cerealnes', 'hemp', 'blueberry', 'peachetc', 'spicenes', 'pistachio', 'chilleetc', 'beetfor', 'citrusnes', 'pear', 'strawberry', 'linseed', 
    'sweetpotato', 'avocado', 'tropicalnes', 'sugarcane', 'jutelikefiber', 'brazil', 'kapokfiber', 'lemonlime', 'spinach', 'sisal', 'carob', 'abaca', 'soybean', 'lettuce', 
    'fig', 'tobacco', 'clover', 'hop', 'kiwi', 'mixedgrain', 'yam', 'mushroom', 'safflower', 'turnipfor', 'nutnes', 'okra', 'rice', 'cashewapple', 'tung', 'fruitnes', 'onion', 
    'pulsenes', 'cauliflower', 'groundnut', 'potato', 'quince', 'sugarbeet', 'bean', 'ryefor', 'castor', 'plantain', 'date', 'cotton', 'pimento', 'quinoa', 'alfalfa', 'rubber', 
    'aniseetc', 'fonio', 'kapokseed', 'nutmeg', 'chestnut', 'plum', 'cucumberetc', 'cherry', 'greencorn', 'hazelnut', 'tangetc', 'mustard', 'watermelon', 'sourcherry', 'stonefruitnes', 
    'rapeseed', 'rootnes', 'currant', 'chicory', 'tea', 'fornes', 'greenbean', 'wheat', 'oilseedfor', 'mango', 'flax', 'cocoa', 'millet', 'poppy', 'pea', 'cabbagefor', 'cabbage', 'coconut', 
    'oilpalm', 'stringbean', 'vetch', 'sorghum', 'almond', 'legumenes', 'oats', 'cinnamon', 'apricot', 'rasberry', 'cranberry', 'coffee', 'areca', 'eggplant', 'clove', 'karite', 'greenbroadbean', 
    'cassava', 'gooseberry', 'cowpea', 'triticale', 'jute', 'pyrethrum', 'lentil', 'lupin', 'chickpea', 'artichoke', 'pigeonpea', 'asparagus', 'banana', 'olive', 'sugarnes', 'canaryseed', 
    'ginger', 'sesame', 'grape', 'rye', 'swedefor', 'taro', 'fibrenes', 'papaya', 'vanilla', 'carrotfor', 'agave', 'garlic', 'greenonion', 'pepper', 'vegfor', 'melonetc', 'hempseed', 'walnut', 
    'broadbean', 'grassnes', 'grapefruitetc', 'ramie', 'pineapple', 'pumpkinetc', 'melonseed', 'greenpea', 'tomato', 'kolanut', 'yautia', 'cashew', 'persimmon', 'sorghumfor', 'peppermint', 'mate', 
    'orange', 'vegetablenes', 'carrot', 'barley', 'mixedgrass', 'sunflower', 'bambara', 'berrynes', 'maizefor', 'buckwheat', 'maize']

AFRICAN_COUNTRIES = ['Algeria', 'Angola', 'Benin', 'Botswana', 'Burkina Faso', 'Burundi', 'Cameroon', 'Cabo Verde', 'Central African Republic', 'Chad', 'Comoros', 
    'Congo, The Democratic Republic of the', 'Congo', 'Djibouti', 'Egypt', 'Equatorial Guinea', 'Eritrea', 'Ethiopia', 'Gabon', 'Gambia', 'Ghana', 'Guinea', 
    'Guinea-Bissau', 'Côte d\'Ivoire', 'Kenya', 'Lesotho', 'Liberia', 'Libya', 'Madagascar', 'Malawi', 'Mali', 'Mauritania', 'Mauritius', 'Morocco', 'Mozambique', 'Namibia', 
    'Niger', 'Nigeria', 'Rwanda', 'Sao Tome and Principe', 'Senegal', 'Seychelles', 'Sierra Leone', 'Somalia', 'South Africa', 'South Sudan', 'Sudan', 'Eswatini', 
    'Tanzania, United Republic of', 'Togo', 'Tunisia', 'Uganda', 'Zambia', 'Zimbabwe']

AFRICAN_COUNTRIES_ALT = ['Ivory Coast']

COUNTRIES_MISSING_DATA = ['Botswana', 'Comoros', 'Congo, The Democratic Republic of the', 'Djibouti', 'Equatorial Guinea', 'Gabon', 'Libya', 'Mauritius', 'Sao Tome and Principe', 'Seychelles', 
    'Somalia', 'South Africa', 'South Sudan']

AFRICAN_COUNTRY_CODES = ['DZ', 'AO', 'BJ', 'BW', 'BF', 'BI', 'CM', 'CV', 'CF', 'TD', 'KM', 'CD', 'CG', 'DJ', 'EG', 'GQ', 'ER', 'ET', 'GA', 'GM', 'GH', 'GN', 'GW', 'CI', 'KE', 'LS', 
    'LR', 'LY', 'MG', 'MW', 'ML', 'MR', 'MU', 'MA', 'MZ', 'NA', 'NE', 'NG', 'RW', 'ST', 'SN', 'SC', 'SL', 'SO', 'ZA', 'SS', 'SD', 'SZ', 'TZ', 'TG', 'TN', 'UG', 'ZM', 'ZW']

COMPLETE_COUNTRIES = ['DZ', 'EG', 'MA', 'TN', 'CM', 'CF', 'BI', 'ER', 'ET', 'KE', 'RW', 'SD', 'TZ', 'UG', 'AO', 'LS', 'MG', 'MW', 'MZ', 'SZ', 'ZM', 'ZW', 'BJ', 'BF', 'CV', 'TD', 
    'CI', 'GM', 'GH', 'GN', 'GW', 'LR', 'ML', 'MR', 'NE', 'NG', 'SN', 'SL', 'TG', 'NA', 'CG']

GEOTIFF_DIRECTORY = '../data/HarvestedAreaYield175Crops_Geotiff/GeoTiff/'

GEOTIFF_SUBDIRECTORIES = ['_DataQuality_HarvestedArea.tif', '_DataQuality_Yield.tif', '_HarvestedAreaFraction.tif', '_HarvestedAreaHectares.tif', '_Production.tif', '_YieldPerHectare.tif']