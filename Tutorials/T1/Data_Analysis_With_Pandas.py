
# coding: utf-8

# # Tutorial 1 : Data Analysis with Pandas

# ### In this tutorial we will explore ['cars.csv'](https://forge.scilab.org/index.php/p/rdataset/source/file/master/csv/datasets/cars.csv) dataset using basic data manipulation and visualisation functions provided by pandas library
# 
# ## You will learn :
# - To reading dataset using pandas
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

# In[50]:

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

# In[3]:

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

# In[4]:

df.shape


# - #### df.columns 
# 
# Retrive the column names from data

# In[5]:

df.columns.tolist()


# - #### df.head(n) 
# 
# Retrieve some of the rows from the begining of the data.'n'is the number of rows to be retrived (default=6)

# In[6]:

df.head()


# - #### df.tail(n) 
# 
# Retrieve some of the rows from the end of the data.'n'is the number of rows to be retrived (default=6)

# In[7]:

df.tail()


# - #### df.describe()
# 
# Generate Summary statistics form the dataset

# In[8]:

df.describe()


# - **df.isnull()**
# 
# This function checks if there are any missing values in the dataset. Returns true if the value is missing. The missing values in the dataset need to be handled carefully in order to maintain consistancy in data 

# In[9]:

df.isnull()

# any() returns true if atleast one of the values is truthy 
df.isnull().any()


# ## Data Manipulation
# 
# Data manipulation is required to process the data in order to get hidden relationships beteen the features. Following are aome basic functions used for data manipulation in pandas
# 

# In[52]:

# Get Column Values
# Syntax: df[column_name]
# Return: Column values
df["Origin"][:10]


# In[11]:

# Get multiple columns
# Syntax: df[list of column_names]
# Return: dataframe of specified columns

df[["Car", "Model", "Origin"]]

# Another way 
col_list=["Car", "Model", "Origin"]
df[col_list]


# In[20]:

# Maths with data frame columns. The mathematical operation applies to all the rows of selected rows
# Multiplication
df["Weight"]*0.001
df[["MPG", "Displacement"]]*2

#Division
df["MPG"]/2
df[["MPG", "Displacement"]]/2

#Comparisons
df["MPG"][:10] >30 # returns True for if MPG value > 10 otherwise returns False



# In[13]:

#Indexing using comparison
df[df["MPG"]>40]

#Get the columns with condition on any column
df[df["MPG"]>40][["Weight","Car"]]


# In[14]:

# Slicing Dataframe
df[1:5]
df["MPG"][:5]


# In[15]:

# Group the data according to one of the categorical columns
# In cars data set Cylinders, Model, Origin are the categorical variables

data=df.groupby("Origin") # returns pandas object. Can use list of columns
list(data)

data=df.groupby("Origin")["MPG"].mean() # returns pandas object. Can use list of columns
list(data)


# In[16]:

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


# In[17]:

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

# ### Analysis

# In[51]:

df.groupby("Origin")["Model"].count().plot.pie()


# ## The above pie-chart shows that mejority of the models are originated in US

# In[35]:

df.groupby("Cylinders")["MPG"].mean().plot.bar()
plt.xlabel("Mean MPG")


# ## The above bar chart representation shows that cars having 4 and 5 cylinders gave the highest mean  MPG compared to others

# In[36]:

df.groupby("Cylinders")["Horsepower"].mean().plot.barh()
plt.xlabel("Mean Horsepower")


# ## The above chart clearly shows that the cars with 8 cylinders produced highest horspower compared to others

# In[37]:

df.groupby("Cylinders")["Acceleration"].median().plot.line()
plt.legend(["Mean Acceleration"])


# In[38]:

df.groupby("Cylinders")["Weight"].plot.kde()
plt.legend()
plt.xlabel("Weight")


# In[39]:

df.groupby("Cylinders")["Weight"].mean().plot.line()


# ## The above plots show relation ship between weight and the cylinders. It shows that the cars with higher number of cylinders will weigh more than the one with less number of cylinders

# In[40]:

df.plot.scatter(y="MPG" ,x="Weight")


# ## The above chart shows the relationship between MPG and Weight of the car. We can see that MPG tends to decrease as Weight of the vehicle increases 

# In[41]:

df.plot.scatter(x="Displacement" ,y="MPG")


# In[42]:

df.plot.scatter(y='MPG',x='Displacement')


# ## The above chart shows the relationship between MPG and Displacement. We can see that MPG tends to decrease with increase in Displacement

# - ***df.hist()***
# 
# histogram plot for all numerical features

# In[45]:

df.hist(xrot=30,figsize=(14,10))


# Histogram plots for all numerical variables grouped by categorical variable

# In[44]:

df.groupby("Origin").hist(xrot=30,figsize=(14,10))


# - ***pd.scatter_matrix(df)***
# 
# Combined representation of all the numerical features using scatter plots (one for each combination of 2 variables) and histogram plots individual variables

# In[47]:

pd.scatter_matrix(df,figsize=(14,10))

