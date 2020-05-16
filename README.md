# cse545_final_project
Final Project Repository for CSE 545 Big Data Analytics
Team Undecided: Andy Liang, Dorothy Shek, Ling Xu, Saketh Chintapalli

The preprocessing scripts can be found in the preprocessing_scripts folder.

The pyspark and tensorflow framework can be found in the mapper_script folder.
Multiple linear regression and multiple hypotheses testing code can also be in this folder.

The display code can be found in the results folder.

Code was run on Google Cloud DataProc instances with image version 1.4.26-debian9.

Data was retrieved from the following sources:

http://www.earthstat.org/

https://data.nal.usda.gov/dataset/international-food-security-0

Display code uses data set 'results.csv' to generate a map of Africa, with markers that, when clicked, display relevant data (i.e. correlation and the correlated crop most highly correlated with food availability). To run properly, the csv file should have the following columns: 'Country', 'Crop', 'p-value'.
