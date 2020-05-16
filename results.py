import folium
import pandas as pd

df = pd.read_csv('C://Users/dorot/Desktop/african_countries.csv')
data = pd.read_csv('C://Users/dorot/Desktop/example_data.csv')

coordinates = (8.7832, 34.5085) # starting position of map: African continent
map = folium.Map(location=coordinates, zoom_start=3)

#df = df.dropna(how='all', axis='columns').dropna(axis=0)

comb = df.join(data.set_index('CountryCode'), on='CountryCode') # join on key=CountryCode

african_countries = {'Algeria', 'Angola', 'Benin', 'Botswana', 'Burkina Faso', 'Burundi', 'Cameroon', 'Cape Verde', 'Central African Republic', 'Chad', 'Comoros', 
    'Congo, The Democratic Republic of the', 'Congo', 'Djibouti', 'Egypt', 'Equatorial Guinea', 'Eritrea', 'Ethiopia', 'Gabon', 'Gambia', 'Ghana', 'Guinea', 
    'Guinea-Bissau', 'Cote d\'Ivoire', 'Kenya', 'Lesotho', 'Liberia', 'Libya', 'Madagascar', 'Malawi', 'Mali', 'Mauritania', 'Mauritius', 'Morocco', 'Mozambique', 'Namibia', 
    'Niger', 'Nigeria', 'Rwanda', 'Sao Tome and Principe', 'Senegal', 'Seychelles', 'Sierra Leone', 'Somalia', 'South Africa', 'South Sudan', 'Sudan', 'Eswatini', 
    'Tanzania', 'Togo', 'Tunisia', 'Uganda', 'Zambia', 'Zimbabwe'}

remove = {'Botswana', 'Comoros', 'Congo, The Democratic Republic of the', 'Djibouti', 'Equatorial Guinea', 'Gabon', 'Libya', 'Mauritius', 'Sao Tome and Principe', 'Seychelles', 'Somalia', 'South Africa', 'South Sudan'}

keep = african_countries.difference(remove)
df = comb[comb['Country'].isin(keep)]

for i in df.index:
	country = df['Country'][i]
	loc = (df['Latitude'][i], df['Longitude'][i])
	info = '<i>' + country + '</i><br><br>Most correlated crop: ' + df['Crop'][i] + '<br><br>Correlation: ' + str(df['Correlation'][i])
	folium.Marker(location=loc, popup=info, tooltip=country).add_to(map)

# hover over countries to see most highly correlated crop
# with respect to country's food availability

map.save('index.html')
