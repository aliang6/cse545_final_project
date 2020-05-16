# cse545_final_project
Final Project Repository for CSE 545 Big Data Analytics

The preprocessing scripts can be found in the preprocessing_scripts folder.

The pyspark and tensorflow scripts can be found in the mapper_script folder.

The display code can be found in the results folder.

Data was retrieved from the following sources:

http://www.earthstat.org/

https://data.nal.usda.gov/dataset/international-food-security-0

Display code uses data set 'results.csv' to generate a map of Africa, with markers that, when clicked, display relevant data (i.e. correlation and the correlated crop most highly correlated with food availability). To run properly, the csv file should have the following columns: 'Country', 'Crop', 'Correlation'.
