# Programming-for-Data-Analysis-Project-2021

## Introduction
The purpose of this assessment is to demonstrate the learning outcomes using Numpy.random to create a data set by simulating a real-world phenomenon.

## Project Statement

- Create a Jupyter notebook
- Create a data set by simulating a real-world phenomenon of my choosing 
- Model and synthesise such data using Python (suggest to use the numpy.random package for this purpose)
- Choose a real-world phenomenon that can be measured and for which you could collect at least one-hundred data points across at least four different variables.
- Investigate the types of variables involved, their likely distributions, and their relationships with each other.
- Synthesise/simulate a data set as closely matching their properties as possible.
- Detail your research and implement the simulation in a Jupyter notebook – the data set itself can simply be displayed in an output cell within the notebook.

**README Table of Contents**

1. GitHub Repository
2. Project Notebook
    - 2.1 About the Project - Programming-for-Data-Analysis-Project-2021-V6.ipynb
    - 2.2 What does the Setup at the beginning do?
    - 2.3 Simulate the Framingham Dataset.
    - 2.4 Conclusion
    - 2.5 Biggest challenge
    - 2.6 Future Challanges
3. How to Use the Project
    - 3.1 Github
    - 3.2 NBViewer
    - 3.3 Binder
    - 3.4 Try at home
4. Acknowledgement
5. References 

***

# 1. GitHub Repository
GitHub repository contains the following

- 1.1 README.md 
    - This README.md file explains why the repository exists, what is in it, and how to run the notebooks
- 1.2 requirements.txt
    - A requirements.txt file is included to enable someone to quickly run this notebooks with minimal configuration.
- 1.3 Programming-for-Data-Analysis-Project-2021-V6.ipynb
    - Jupyter notebook for project notebook
- 1.4 Version Control
    - A Version control to keep track of changes made to the Jupyter notebooks and learning outcomes.
- 1.5 data
    - Pictures from notebook
    - CSV for input data and output of simulated data  

***
# 2. Project Notebook - Programming-for-Data-Analysis-Project-2021-V6.ipynb
This README contains an overview of the Project Notebook. The Jupyter notebook contains the main body of work and list all references used the in the assignment.

## 2.1 About the Project Notebook.

The challenge with the Project Notebook is to pick the real-world phenomenon, I decide to simulate the data from the Framingham Heart Study. After researching and developing the Notebook the simulated data should be based on Age, Systolic Blood Pressure, Hypertensive, Diastolic Blood Pressure, Glucose Levels and Diabetes. Age is the main reference point as the Framingham Heart Study, which followed patients for 30 years, that systolic blood pressure (SBP) shows a continuous increase between the ages of 30 and 84 years or over. [14]

To develop a futher understanding of the data I found the levels of over 180 of Systolic Blood Pressure and over 120 Diastolic Blood Pressure that caused Hypertension. Hypertension is serious because people with the condition have a higher risk for heart disease and other medical problems than people with normal blood pressure. [20] I was also informed of the glucose level may be an important predictor of mortality in patients with established cardiovascular disease. [19] 

## 2.2 What does the Setup at the beginning do?

- Imports the python modules to run the notebook
- Read the Framingham Heart Study Data
    - TenYearCHD (10-year risk of coronary heart disease) identify the variables and the strength of a relationship with the other variables.
    - Simulate 6 of 15 variables with the highest correlation of 10% and above
    - Descriptive Analysis of the 6 variable 4240 except glucose displayed a count of 3852
    - Remove row with missing values - Dataset size is 3852 rows
    - Rename the headers
- Create a Histogram and Boxplot on the data 
    - Identify the numpy.random distribution for the variables

![FramDistribution](https://github.com/DPR-droid/Programming-for-Data-Analysis-Project-2021/blob/main/Data/FramDistribution.png)

![FramBoxplot](https://github.com/DPR-droid/Programming-for-Data-Analysis-Project-2021/blob/main/Data/FramBoxplot.png)

- Group the rows and columns by 'Age' groups
    - Mean and Standard deviation for each Group for 
        - Systolic Blood Pressure, Diastolic Blood Pressure, Glucose Levels
- Recreate the Age array
    - Identify the probabilities of occurrence for each element

## 2.3 Simulate the Framingham Dataset

- Create a New Dataframe
- Populate 'Age' in the New Dataframe using random.choice with size of 3852
- Random Normal to populate 'Systolic Blood Pressure' 'Diastolic Blood Pressure' 'Glucose Levels'
- Populate 'Hypertensive' from output 'Systolic Blood Pressure'
- Populate 'Diabetes' from output 'Glucose Levels'
- Round data to one decimal place to match output of Framingham 


## 2.4 Conclusion

## Conclusion

To conclude that the correct packages of NumPy.random (choice and normal) is the most suited to their likely distributions for selected variables. The output using the described function for both datasets demonstrate only minor changes in Mean and standard deviation. The outlier in Systolic Blood Pressure and Glucose Levels affect the outcome of Hypertensive and Diabetes respectively.

![Real-v-Sim](https://github.com/DPR-droid/Programming-for-Data-Analysis-Project-2021/blob/main/Data/Real-v-Sim.png)

The comparison of the both sets of data can be visualised with the plots

### The 4 x 4 Histogram overlay the Numpy.random simulated data over the real-world data.:

	Compare Systolic Blood Pressure
	This is a normal distribution, outliers are not accounted for in the simulated data

	Compare Diastolic Blood Pressure
	This is a normal distribution

	Compare Glucose Levels
	This is a normal distribution, outliers are not accounted for in the simulated data

	Compare Age:
	I could have used uniform data for this section, to replicate the 'Age' I decided to recreate using non-uniform and the probabilities associated with each entry.

![Comparedataframes](https://github.com/DPR-droid/Programming-for-Data-Analysis-Project-2021/blob/main/Data/Comparedataframes.png)


### A pair plot of both datasets:
	
	Scatter plots are used to observe relationships between variables. The four by four matrix illustrates the normal distribution of the data. The scatterplot clearly shows the simulated data does not account for the outliers in Systolic Blood Pressure and Glucose Levels.


![pairplotFram](https://github.com/DPR-droid/Programming-for-Data-Analysis-Project-2021/blob/main/Data/pairplotFram.png)

![pairplotNewFram](https://github.com/DPR-droid/Programming-for-Data-Analysis-Project-2021/blob/main/Data/pairplotNewFram.png)


### Conclusion:

Numpy.random is a useful tool for a data analyst to simulated data.  


## 2.5 What did I learn?

- How to use numpy.random to simulate real-world data
- How to use the describe function and plots to interpret data.
- How to use a correlation matrix investigates the dependence between multiple variables at the same time
- A valuable resource of using online research

## 2.6 Biggest challenge

- Find a real-world dataset
- Research on data that I am unfamiliar with
- Use a correlation matrix to investigate the dependence between multiple variables at the same time

## 2.7 Future Challenges

- Analysing original data, correlating of Systolic and Diastolic Blood Pressure for Hypertension. 
- What other factors caused the many outliers in the glucose levels?
- Other distribution to closely match Glucose levels and Systolic Blood Pressure
- Machine learning to allow the user to test 

***

# 3. How to Use the Project

How to run or review the Jupyter notebook.      

## 3.1 Github
Review the assignment [Click here Programming-for-Data-Analysis-Project-2021.ipynb](https://github.com/DPR-droid/Programming-for-Data-Analysis-Project-2021/blob/main/Programming-for-Data-Analysis-Project-2021-V6.ipynb)

## 3.2 NBViewer
NBViewer is another way to share Jupyter Notebook.

[![nbviewer](https://raw.githubusercontent.com/jupyter/design/master/logos/Badges/nbviewer_badge.svg)](http://nbviewer.org/github/DPR-droid/Programming-for-Data-Analysis-Project-2021/blob/main/Programming-for-Data-Analysis-Project-2021-V6.ipynb)

## 3.3 Binder
Try this assignment without installing by clicking the Binder badge below, this allows you to run the Jupyter notebook in an online virtual executable environment, making the code immediately reproducible by anyone, anywhere. 

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/DPR-droid/Programming-for-Data-Analysis-Project-2021/main?filepath=Programming-for-Data-Analysis-Project-2021-V6.ipynb)

**import warnings** not included in requirements.txt as it was causing an issue when building the online virtual executable environment.

## 3.4 Try at home

To try this on your own PC you require the following:
- Install Anaconda https://www.anaconda.com/products/individual this ditribution includes Python and serveral packages used in this Assignment including the numpy package. 
- 'requirments.txt' for other modules required. 
- Install Jupyter https://jupyter.org/ to run Programming-for-Data-Analysis-Project-2021.ipynb
- Install Github
- git clone git@github.com:DPR-droid/Programming-for-Data-Analysis-Project-2021.git

***

# 4. Acknowledgement
Lecturer Brian Mcginley Programming for Data Analysis GMIT

Family and friends for their support

***

# 5. References

[1] https://www.bbc.co.uk/bitesize/guides/zvxp34j/revision/3

[2] https://nfb.org//sites/default/files/images/nfb/publications/vodold/vspr9804.htm

[3] https://github.com/TarekDib03/Analytics/blob/master/Week3%20-%20Logistic%20Regression/Data/framingham.csv

[4] https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.describe.html

[5] https://www.geeksforgeeks.org/sort-correlation-matrix-in-python/

[6] https://cmdlinetips.com/2020/11/how-to-get-number-of-missing-values-in-each-column-in-pandas/

[7] https://statisticsglobe.com/drop-rows-blank-values-from-pandas-dataframe-python

[8] https://towardsdatascience.com/visualizing-data-with-pair-plots-in-python-f228cf529166

[9] https://www.kaggle.com/micahshull/python-heart-disease-framingham

[10] https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.describe.html

[11] https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.head.html

[12] https://cmdlinetips.com/2020/11/how-to-get-number-of-missing-values-in-each-column-in-pandas/

[13] https://statisticsglobe.com/drop-rows-blank-values-from-pandas-dataframe-python

[14] https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2805932/

[15] https://github.com/TarekDib03/Analytics/blob/master/Week3%20-%20Logistic%20Regression/Data/framingham.csv

[16] https://blog.softhints.com/pandas-count-percentage-value-column/

[17] https://www.webmd.com/hypertension-high-blood-pressure/guide/diastolic-and-systolic-blood-pressure-know-your-numbers

[18] https://academic.oup.com/aje/article/163/4/342/103626

[19] https://medlineplus.gov/bloodsugar.html

[20] https://medical-dictionary.thefreedictionary.com/hypertension