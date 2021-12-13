########################################################################
# GMIT Project for Programming for Data Analysis
# Programming-for-Data-Analysis-Project-2021
# Due: last commit on or before 03/01/2021
# Programming-for-Data-Analysis-Project-2021.py
# Author David
# The project submitted is in a Jupyter notebook
# This python script is a reference and testing 
########################################################################
# Global settings
# Importing all the modules required for the juypter Notbook
# All imports are listed in the requirments.txt
########################################################################


# Imports

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


import warnings

warnings.filterwarnings('ignore')

print('\n\n########################################################################')

# import data from data folder
# https://github.com/TarekDib03/Analytics/blob/master/Week3%20-%20Logistic%20Regression/Data/framingham.csv
df = pd.read_csv("data/framingham.csv")

# Print first 10 entries
print('Print head 10 \n\n')
print(df.head(10))

print('\n\n########################################################################')

# Print the count, mean, std, min, max as well as lower, 50 and upper percentiles. 
# The lower (25) and upper (75) percentiles. The 50 percentile is the same as the median.
# This is to give an overview of the dataframe including missing values
print('Count, mean, std, min, max \n\n')
print(df.describe())

print('\n\n########################################################################')

# To select the variables required for the project A correlation matrix investigates the dependence 
# between multiple variables at the same time. It shows symmetric tabular data where each row and column 
# represent a variable, and the corresponding value is the correlation coefficient denoting the strength of a 
# relationship between these two variables. 
# https://www.geeksforgeeks.org/sort-correlation-matrix-in-python/

print('Get correlation of variables with TenYearCHD \n\n')
FHS_correlation = df.corr()['TenYearCHD']
corr_FHS = FHS_correlation.abs().sort_values(ascending=False)[1:]
print(round(corr_FHS,2))

print('\n\n########################################################################')

# Create a new dataframe with variables with the highest correlation
# Cut-off rate is 10% and above

print('New dataframe with values with highest correlation \n\n')
High_corr = df[['TenYearCHD','age','sysBP','prevalentHyp','diaBP','glucose', 'diabetes']] 

print(High_corr.describe() ) 

print('\n\n########################################################################')

# Count missing values in rows
# https://cmdlinetips.com/2020/11/how-to-get-number-of-missing-values-in-each-column-in-pandas/
print('Count Missing values in dataframe \n\n')
print(High_corr.isna().sum())


print('\n\n########################################################################')

# Drop rows with blank values
# https://statisticsglobe.com/drop-rows-blank-values-from-pandas-dataframe-python
print('Check cleaned data \n\n')
High_corr.dropna(inplace = True)                   
print(High_corr.describe())    

print('Verify missing values are removed from dataframe \n\n')
print(High_corr.isna().sum())

print('\n\n########################################################################')

#Plot a histogram of Age
print('Get histogram of Age \n\n')
df.hist(column='age')
plt.show()

print('\n\n########################################################################')

# Investigate with Seaborn
# Plot colored
sns.pairplot(High_corr, 
             vars = ['TenYearCHD','age','sysBP','prevalentHyp','diaBP','glucose', 'diabetes'], 
             hue="TenYearCHD", diag_kind = 'kde', 
             plot_kws = {'alpha': 0.6, 's': 80, 'edgecolor': 'k'},
             size = 4);# Title 
plt.suptitle('Pair Plot of Farmington Data', size = 28)
plt.show()

