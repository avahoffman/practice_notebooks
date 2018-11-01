# Some ways to visualize data!
# Also known as EDA - "Exploratory Data Analysis"

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

# We want to eventually predict the AGE of the abalone (ring value + 1.5)
# Sex is categorical, everything else is continuous either in mm or grams except for ring value which is an integer (whole number)

# Get summary statistics for our numeric variables
data.describe()

# Get summary statistics on our categorical variables
data['sex'].value_counts()
# This is good to know, because we know we have more males than females. The data is not too different that we have imbalanced data though.
# The ratio for imbalanced data is usually 1 to 10, around there!

# We want to predict the number of rings. Reasoning stolen from here (https://towardsdatascience.com/bayesian-linear-regression-in-python-using-machine-learning-to-predict-student-grades-part-1-7d0ad817fca5):
# "The ring column is our target variable (also known as the response), which makes this a supervised, regression machine learning task.
# It’s supervised because we have a set of training data with known targets and, during training, we want our model to learn to predict the rings from the
# other variables. We will treat the ring as continuous which makes this a regression problem (technically the ring # only takes on integer values so
# it is a nominal variable)""

# Make a histogram for each numeric variable
data.hist(bins=50, figsize=(20,15))
# If you want to save this
# plt.savefig("attribute_histogram_plots")
plt.show()

# We are interested in predicting RINGS, so let's look specifically at a histogram of that to check for SKEW
plt.hist(data['rings'], bins = 29) # Bin number reflects how many rings we are looking at -- I used the .describe min and max to assess this part
plt.xlabel('Rings')
plt.ylabel('Count')
plt.title('Distribution of Number of Rings')

# We can see from this graph that we are pretty close to a NORMAL distribution.

# Let's look at the effect of categorical variables on our abalone ring size
# We can use DENSITY plots of the ring size distribution colored by the value of the categorical variable (sex) using Seaborn
# Make one plot for each different location
sns.kdeplot(data.loc[data['sex'] == 'F', 'rings'],
            label = 'Female', shade = True)
sns.kdeplot(data.loc[data['sex'] == 'M', 'rings'],
            label = 'Male', shade = True)
sns.kdeplot(data.loc[data['sex'] == 'I', 'rings'],
            label = 'Infant', shade = True)
# Add labeling
plt.xlabel('No. of Rings')
plt.ylabel('Density')
plt.title('Density Plot of Ring Number by Sex')

# What does this tell us? Not too much but it is still helpful. We see that infancy does seem to be a good indicatory of a range of rings
# (which is a bit of a DUH because obviously the younger you are, the younger you are).
# We can say that we'll have a DEFINITE correlation between infancy and ring number.
# However GENDER doesn't seem to influence ring size that much. Maybe females live longer slightly slightly?
# "Plots such as these can inform our modeling because they tell us if knowing the gender or age of the abalone might be helpful for predicting ring number
# Of course, we want to use a more rigorous than a single plot to make these conclusions, and later we'll use statistics to back up our intuition!"
# Above quote modified from here: https://towardsdatascience.com/bayesian-linear-regression-in-python-using-machine-learning-to-predict-student-grades-part-1-7d0ad817fca5

# Check out correlations of things. "We don't expect every variable to be related to the rings, so we might need to do feature selection or
# dimensionality reduction. Because we are using a linear regression (note Gaussian distribution) we can use a Correlation Coefficient!"
# Correlation Coefficient is a value between -1 to 1 that shows direction and strength of linear relationship between two variables
# Find correlations and sort
data.corr()['rings'].sort_values()
# Ok, shell weight seems to be the biggest potential predictor -- of course rings are 1, because rings are the thing we are predicting!

# This tutorial says to pick the top 6 variables as a good rule of thumb, but there are other ways to select features (feature selection).
# You could do PCA, autoencoders, L1 regularization ("Lasso" -- removes features all together!), feature engineering (PCA or sum or mean).

# Look at correlations with categorical variables (sex)
# Select only categorical variables
category_df = data.select_dtypes('object')
# One hot encode the variables
dummy_df = pd.get_dummies(category_df)
# Put the grade back in the dataframe
dummy_df['rings'] = data['rings']
# Find correlations with grade
dummy_df.corr()['rings'].sort_values()

 # Again, Male and Female are not THAT different -- but Infant does seem to really have a relationship. The younger the abalone, the less rings it has.

 # Now let's do a PAIRS PLOT!
 # "A pairs plot allows us to see both distribution of single variables and relationships between two variables"
 # Create the default pairplot
sns.pairplot(data)
# What this shows you is relationship between all of your variables. You can use this too to evaluate what features are good ones to keep in your model
# and ones that might not be that helpful. (E.g. shucked weight continues to show us that it isn't that great of a predictor)

# We can even incorporate categories in our pair plots!
sns.pairplot(data, hue = 'sex')

# "This graph is more informative, but there are still some issues: I tend not to find stacked histograms, as on the diagonals, to be very interpretable.
# A better method for showing univariate (single variable) distributions from multiple categories is the density plot. We can exchange the histogram for
# a density plot in the function call. While we are at it, we will pass in some keywords to the scatter plots to change the transparency, size, and edgecolor
# of the points."
# From here: https://towardsdatascience.com/visualizing-data-with-pair-plots-in-python-f228cf529166
# Create a pair plot colored by continent with a density plot of the # diagonal and format the scatter plots.
sns.pairplot(data, hue = 'sex', diag_kind = 'kde',
             plot_kws = {'alpha': 0.6, 's': 80, 'edgecolor': 'k'},
             size = 4)

# Much better!

# For CATEGORICAL DATA
# Box plots
bplot=sns.boxplot(y='rings', x='sex',
                 data=data,
                 width=0.5,
                 palette="colorblind")

# Frequency Distribution
sex_count = data['sex'].value_counts()
sns.set(style="darkgrid")
sns.barplot(sex_count.index, sex_count.values, alpha=0.9)
plt.title('Frequency Distribution of Sexes')
plt.ylabel('Number of Occurrences', fontsize=12)
plt.xlabel('Sex', fontsize=12)
plt.show()
