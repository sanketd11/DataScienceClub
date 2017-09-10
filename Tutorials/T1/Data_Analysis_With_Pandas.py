
# coding: utf-8

# # Tutorial 1 : Data Analysis with Pandas

# ### In this tutorial we will explore ['cars.csv'](https://forge.scilab.org/index.php/p/rdataset/source/file/master/csv/datasets/cars.csv) dataset using basic data manipulation and visualisation functions provided by pandas library
# 
# ## You will learn :
# - To read dataset using pandas
# - To get quick summary of data
# - To manipulate dataset columns for data processing
# - To plot the porcessed data for insights
# 
# ## We assume you know:
# - Basic python
# - Basic understanding of plots
# 
# ## Resources:
# - [Pandas Documentation](https://pandas.pydata.org/pandas-docs/stable/)
# - [Cars Dataset](https://forge.scilab.org/index.php/p/rdataset/source/file/master/csv/datasets/cars.csv)
# - Find source code of this tutorial [here](https://github.com/sanketd11/DataScienceClub) 
# 

# # Let's Begin.....

# ### What is Pandas?
# 
# Pandas is one of the most powerfull libraries that are used for data analysis in python. Pandas provide two primary data structures Series (1- dimentional) and Dataframe( 2 dimensional) which can be used to express the data intuitively and perform fast operations. Pandas is built on top of [**numpy**](http://www.numpy.org/) which is another powerful and popular library used in python for scientific computations. 

# ### Import Library
# Import the pandas library. Here I renamed it to 'pd' just for the ease of use. Make sure you don't get errors in import 

# In[56]:

import pandas as pd

from matplotlib import pyplot as plt # required for plots
plt.style.use= 'default'# To display plots


# ## Read Dataset
# Following are some of the functions available in pandas for reading a dataset
# - **read_csv()** (Press 'Shift+tab' to see the function arguments )
#     - filepath
#     - sep
#     - names
#     - parse_dates
#     - index_col
# - read_excel()
# - read_json()
# - read_pickle()
# - read_sql()

# In[57]:

df=pd.read_csv('cars.csv', sep=';')


# ## Know Your Dataset
# We can use following functions to get basic understanding of the dataset: (Assume 'df' contains data)
# - ***df.shape*** 
# - ***df.columns***
# - ***df.head()***
# - ***df.tail()***
# - ***df.describe()***
# 
# Let's look at these one by one
# 
# - #### df.shape 
# 
# Retrieves Shape of the dataset

# In[58]:

df.shape


# - #### df.columns 
# 
# Retrive the column names from data

# In[59]:

df.columns.tolist()


# - #### df.head(n) 
# 
# Retrieve some of the rows from the begining of the data.'n'is the number of rows to be retrived (default=6)

# In[60]:

df.head()


# - #### df.tail(n) 
# 
# Retrieve some of the rows from the end of the data.'n'is the number of rows to be retrived (default=6)

# In[61]:

df.tail()


# - #### df.describe()
# 
# Generate Summary statistics form the dataset

# In[62]:

df.describe()


# - **df.isnull()**
# 
# This function checks if there are any missing values in the dataset. Returns true if the value is missing. The missing values in the dataset need to be handled carefully in order to maintain consistancy in data 

# In[63]:

df.isnull()

# any() returns true if atleast one of the values is truthy 
df.isnull().any()


# ## Data Manipulation
# 
# Data manipulation is required to process the data in order to get hidden relationships beteen the features. Following are some basic functions used for data manipulation in pandas
# 

# In[64]:

# Get Column Values
# Syntax: df[column_name]
# Return: Column values
df["Origin"][:10]


# In[65]:

# Get multiple columns
# Syntax: df[list of column_names]
# Return: dataframe of specified columns

df[["Car", "Model", "Origin"]]

# Another way 
col_list=["Car", "Model", "Origin"]
df[col_list]


# In[66]:

# Maths with data frame columns. The mathematical operation applies to all the rows of selected rows
# Multiplication
df["Weight"]*0.001
df[["MPG", "Displacement"]]*2

#Division
df["MPG"]/2
df[["MPG", "Displacement"]]/2

#Comparisons
df["MPG"][:10] >30 # returns True for if MPG value > 10 otherwise returns False



# In[67]:

#Indexing using comparison
df[df["MPG"]>40]

#Get the columns with condition on any column
df[df["MPG"]>40][["Weight","Car"]]


# In[68]:

# Slicing Dataframe
df[1:5]
df["MPG"][:5]


# In[69]:

# Group the data according to one of the categorical columns
# In cars data set Cylinders, Model, Origin are the categorical variables

data=df.groupby("Origin") # returns pandas object. Can use list of columns
list(data)

data=df.groupby("Origin")["MPG"].mean() # returns pandas object. Can use list of columns
list(data)


# In[70]:

# Data Aggregation methods (Can be used independently or along with 'groupby')

#Mean
df.mean()  #Returns mean value of all the columns

#Max 
df.max()   #Returns max value of all the columns 

#Min
df.min()   #Returns min value of all the columns 

#Count
df.count() # Returns the count of column values 

#sum 
df.sum()  # Returns the sum of all the columns


# In[71]:

# Drop columns that are not required
dfNew=df.drop("Origin", axis=1)
print(df.columns.tolist())
print(dfNew.columns.tolist())


# ## Data Visualization
# 
# Pandas provide several plot options that we can use to visualize our dataset. Visualisations help to understand the relations between the various features from the dataset. Following are some of the plot options that we can use. 

# - ***df.plot.****
# 
# Following plot options are also available to be used with pandas dataframe
# 
# - df.plot.area
# - df.plot.barh 
# - df.plot.density
# - df.plot.hist
# - df.plot.line
# - df.plot.scatter
# - df.plot.bar
# - df.plot.box
# - df.plot.hexbin
# - df.plot.kde
# - df.plot.pie
# 

# #### For more details on plots visit: [ Pandas Visualization ]( https://pandas.pydata.org/pandas-docs/stable/visualization.html)   

# ## Analysis

# In[72]:

df.groupby("Origin")["Model"].count().plot.pie()


# ### The above pie-chart shows that mejority of the models are originated in US

# In[73]:

df.groupby("Cylinders")["MPG"].mean().plot.bar()
plt.xlabel("Mean MPG")


# ### The above bar chart representation shows that cars having 4 and 5 cylinders gave the highest mean  MPG compared to others

# In[74]:

df.groupby("Cylinders")["Horsepower"].mean().plot.barh()
plt.xlabel("Mean Horsepower")


# ### The above chart clearly shows that the cars with 8 cylinders produced highest horspower compared to others

# In[75]:

df.groupby("Cylinders")["Acceleration"].median().plot.line()
plt.legend(["Mean Acceleration"])


# In[76]:

df.groupby("Cylinders")["Weight"].plot.kde()
plt.legend()
plt.xlabel("Weight")


# In[77]:

df.groupby("Cylinders")["Weight"].mean().plot.line()


# ### The above plots show relation ship between weight and the cylinders. It shows that the cars with higher number of cylinders will weigh more than the one with less number of cylinders

# In[78]:

df.plot.scatter(y="MPG" ,x="Weight")


# ### The above chart shows the relationship between MPG and Weight of the car. We can see that MPG tends to decrease as Weight of the vehicle increases 

# In[79]:

df.plot.scatter(x="Displacement" ,y="MPG")


# In[80]:

df.plot.scatter(y='MPG',x='Displacement')


# ### The above chart shows the relationship between MPG and Displacement. We can see that MPG tends to decrease with increase in Displacement

# ## Some  more functions for visualization:

# ### histogram plot for all numerical features
# - ***df.hist()***
# 
# 

# In[81]:

df.hist(xrot=30,figsize=(14,10))


# ### Histogram plots for all numerical variables grouped by categorical variable "Origin": 

# In[82]:

df.groupby("Origin").hist(xrot=30,figsize=(14,10))


# ### Combined representation of all the numerical features using scatter plots (one for each combination of 2 variables) and histogram plots individual variables
# 
# - ***pd.scatter_matrix(df)***
# 
# 

# In[83]:

pd.scatter_matrix(df,figsize=(14,10))

