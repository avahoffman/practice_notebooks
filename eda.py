# Exploratory data analysis!
# Load in and label our data
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Read in data (from here: http://archive.ics.uci.edu/ml/datasets/Abalone?pagewanted=all)
# Make sure to fix column names too
# We want to have it say Sex, Length, Diameter, Height, Whole Weight, Shucked Weight, Viscera Weight, Shell Weight and Rings
data = pd.read_csv('/Users/katelyons/Documents/Insight/practice/ml/abalone.csv', names = ["sex", "length", "diameter", "height", "whole_weight", "shucked_weight", "viscera_weight", "shell_weight", "rings"])
# Take a peek
# data.head()
# Get information about the data
# data.info()

# "Exploratory Data Analysis (EDA) is used on the one hand to answer questions, test business assumptions, generate hypotheses for further analysis.
# On the other hand, you can also use it to prepare the data for modeling. The thing that these two probably have in common is a good knowledge of your
# data to either get the answers that you need or to develop an intuition for interpreting the results of future modeling.
#
# There are a lot of ways to reach these goals: you can get a basic description of the data, visualize it, identify patterns in it,
# identify challenges of using the data, etc."
# From: https://www.datacamp.com/community/tutorials/exploratory-data-analysis-python

# .describe is a very important function!
data.describe()

# To get a feel for your dataset if it is a HUGE dataset, you can use sample to get a random sample
data.sample(10)

# You can also query the data. You can test some simple hypotheses about the data:
data.query('diameter < height') # Compare things -- see cases in which diameter is less than height and vise versa
# E.g. not too many cases in which abalone heights are more than the diameter

# CHECK FOR MISSING VALUES
data.isnull().values.any()

# How to deal with missing values:
# "Besides deletion, there are also methods that you can use to fill up cells if they contain missing
# values with so-called 'imputation methods'. If you already have a lot of experience with statistics, you’ll know that imputation is the
# process of replacing missing data with substituted values. You can either fill in the mean, the mode or the median. Of course, here you need
# to think about whether you want to take, for example, the mean or median for all missing values of a variable, or whether you want to
# replace the missing values based on another variable. For example, for data in which you have records that have features with
# categorical variables such as 'male' or 'female', you might also want to consider those before replacing the missing values, as the observations might
# differ from males and females. If this is the case, you might just calculate the average of the female observations and then fill out the missing values
# for other 'female' records with this average."

# "Estimate the value with the help of regression, ANOVA, logistic regression or another modelling technique. This is by far the most
# complex way to fill in the values."

# "You fill in the cells with values of records that are most similar to the one that has missing values. You can use KNN or K-Nearest Neighbors in
# cases such as these."

# Let's pretend we have missing information on abalone shell height

# Imputation
# Import NumPy
import numpy as np

# Calculate the mean
mean = np.mean(data.height)

# Replace missing values with the mean
data. = data.height.fillna(mean)

# You can also fill values forward or backward -- method depends on the DATA

# Drop rows with missing values
data.dropna(axis=0)

# Drop columns with missing values
data.dropna(axis=1)

# Interpolate -- have it use linear interpolation to 'guess' what value might be:
data.interpolate() # You can use method argument to do fancier interpolations


# OUTLIERS
