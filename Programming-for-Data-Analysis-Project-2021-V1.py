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
import matplotlib.pyplot as plt
import warnings

warnings.filterwarnings('ignore')



# import data from data folder
# https://github.com/TarekDib03/Analytics/blob/master/Week3%20-%20Logistic%20Regression/Data/framingham.csv
df = pd.read_csv("data/framingham.csv")

# Print first 5 entries
print(df.head(5))

# Print the count, mean, std, min, max as well as lower, 50 and upper percentiles. 
# The lower (25) and upper (75) percentiles. The 50 percentile is the same as the median.
# This is to give an overview of the dataset including missing values
print(df.describe())

# Plot a histogram of Age
df.hist(column='age')
plt.show()