import pandas as pd
import numpy as np

#--------------------------------------- DATASET-----------------------------------------------------------
 
data = {
    "name":       ["Alice", "Bob", "Charlie", "Diana", "Ethan",
                   "Fiona", "George", "Hannah", "Ivan", "Julia"],
    "age":        [20, 22, 21, 23, 20, 22, 24, 21, 23, 20],
    "gender":     ["F", "M", "M", "F", "M", "F", "M", "F", "M", "F"],
    "city":       ["Mumbai", "Delhi", "Mumbai", "Chennai", "Delhi",
                   "Mumbai", "Chennai", "Delhi", "Mumbai", "Chennai"],
    "math":       [88, 72, 95, 60, 85, 78, 90, 55, 70, 92],
    "science":    [75, 68, 90, 72, 80, 85, 88, 60, 65, 95],
    "english":    [82, 74, 78, 88, 70, 90, 65, 72, 80, 85],
    "passed":     [True, True, True, False, True, True, True, False, True, True],
}
 
df = pd.DataFrame(data)
print(df.shape)

#----------------------------------------------SECTION 1 — CREATING A DATAFRAME-----------------------------------------------
# Using Dictionary
simple = pd.DataFrame({
    "products" : ["Apple","Cherry", "Watermelon"],
    "price": [50, 60, 40],
    "Stock": [100, 20, 60]
})
print("Data Frame", simple)

# Single Labeled Dataset
marks = pd.Series([54,62,84,58,94], name = "math_marks",
         index = ["Arjun","Karan","Ekta","Shreya","Riya"])
print("Series \n",marks)

#-----------------------------------Viewing And Inspecting the Data---------------------------------
print("First four\n ",df.head(4))
print("Last Row", df.tail(4))
print("Shape",df.shape)
print("Columns Names", df.columns.tolist())
print("Data Types", df.dtypes)
print("Basic Statistics",df.describe())
print("Null Value Count",df.isnull().sum())
print("Unique Cities", df["city"].unique())
print("City Value Count",df["city"].value_counts())
df.info()

# ----------------------------SELECTING DATA---------------------
print("\n Math Col", df["math"])  # Single Col ---> Series
print("\n Name and Math: \n",df[["name","math"]]) # Multiple Col --> Dataframe

# Row by position - iloc
print("\n Row at position 0: ", df.iloc[0])
print("\n Rows 0 to 2", df.iloc[0:3])

# Row by Label - iloc
print("\n Row with label 2: ",df.loc[2])
print("\n Row 1-3:, selected col:", df.loc[1:3,["name","math","city"]])

# Single cell value
print("Cell [0,math]", df.at[0, "math"])

#---------------------------------Aggregation and groupby----------------

print("Mean",df["math"].mean())
print("Max",df["math"].max())
print("Min", df["math"].min())
print("Sum", df["math"].sum())
print("Count", df["math"].count())

# Groupby - average math per city
print("Average math by City \n",df.groupby("city")["math"].mean().round(2))

# Group by - count student per city
print("Student count \n",df.groupby("city")["math"].count())

# Groupby - multiple col
print("Avg math and science by city \n",df.groupby("city")[["math","science"]].mean().round(2))

# REMOVING MISSING DATA COMMAND
df_drop = df.dropna() # Removes rows with missing value
print(df_drop)

df.dropna(axis=1) # Removes columns with misiing values

# Filling Missing data
# fill missing values with constant
df_fill = df.fillna(0)
print(df_fill)

# fill missing values with column mean 
df["math"].fillna(df["math"].mean,inplace = "True")
print(df)