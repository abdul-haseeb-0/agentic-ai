import pandas as pd
import matplotlib.pyplot as plt



# Creating Series
# ----------------
# Creating series from list
data = [10, 30, 20, 40]
series = pd.Series(data, index=["a", "b", "c", "d"])
print(series)
print(series["a"])  # 10
print(series[0])    # 10

# Creating series from dictionary
data = {"a": 10, "b": 30, "c": 20, "d": 40}
series = pd.Series(data)
print(series)



# Creating DataFrame
# ------------------
# Example Data
data = {
    "ID": [121, 122, 123],
    "Name": ["ALI", "Hamza", "Hussan"],
    "Salary": [50000, 50000, 60000]
}

# Creating DataFrame
df = pd.DataFrame(data)
print(df)



# Selecting Data
# --------------
# Selecting Columns from data
print(data["Name"])  # select Column
print(pd.Series(data["Name"]))  # select & print Column as Series

# Selecting data from DataFrame
print(df["Name"])  # select Name Column
print(df[["ID", "Salary"]])  # select ID and Salary Column

print(df.iloc[0])  # select first row. iloc -> index location
print(df.loc[1])  # select second row of index 1. loc -> location
print(df.loc[df["Salary"] < 55000])  # select rows where salary is less than 55000



# Data Manipulation
# -----------------
df["Bonus"] = df["Salary"] * (10 / 100)  # Create new column -> Bonus
df["Net Salary"] = df["Bonus"] + df["Salary"]
df.drop("Bonus", axis=1, inplace=True)   # Drop Bonus Column, axis=1 for column, inplace -> True for permanent change

df.loc[2] = [124, "Ahmad", 6000]  # Replace index 2 entry and remove original
df.loc[3] = [214, "ALI", 60000]   # Add new entry(row) to index 3
df.drop(3, axis=0, inplace=True)  # drop row, axis=0 for row



# Merge DataFrames
# ----------------
df1 = pd.DataFrame({"ID": [1, 2, 3], "Salary": [10000, 20000, 30000]})
df2 = pd.DataFrame({"ID": [1, 2, 4], "Bonus": [1000, 2000, 4000]})

merged_df = df1.merge(df2, on="ID", how="inner")  # print only common rows by merging both dataframes
print(merged_df)

merged_df = df1.merge(df2, on="ID", how="outer")  # print all rows by merging both dataframes
print(merged_df)



# Concatenation
# -----------------------
print(pd.concat([df1, df2], ignore_index=True))  # concatenate both dataframes

# Visualizing Data
# ----------------
df["Salary"].plot(kind="bar")  # Bar of Salary
df["Salary"].plot(kind="hist", bins=20, color="red", alpha=0.5, edgecolor="black")  # histogram of Salary
df.plot(kind="scatter", x="ID", y="Salary")  # Scatter plot of ID vs Salary
plt.show()



# Handling Missing Data
# ---------------------
print(df.isnull().sum())  # sum of null cells
df.fillna(0, inplace=True)  # replace NaN value with 0 in rows
df.fillna(df.mean(), inplace=True)  # replace NaN value with mean values in rows
df.dropna(inplace=True)  # delete rows with missing values
df.dropna(axis=1, inplace=True)  # delete columns having missing values



# Sorting Data
# -----------------------
df.sort_values("Salary", ascending=True, inplace=True)  # sort by Salary in ascending order
df.sort_values(["ID", "Salary"], ascending=[False, True])  # sort by ID in descending and Salary in ascending order
df.sort_index(inplace=True)  # sort by index
df.reset_index(drop=True, inplace=True)  # reset index



# Grouping Data
# -----------------------
grouped = df.groupby("Department")
print(grouped["Salary"].mean())  # Average salary in each department
print(grouped["Salary"].sum())  # Total salary in each department
print(grouped["Salary"].max())  # Maximum salary in each department
print(grouped["Salary"].min())  # Minimum salary in each department



# Aggregation
# -----------------------
print(df.agg({
    "ID": "max",  # max ID
    "Salary": ["mean", "max"]  # mean and max salary
}
))



# Loading and Saving Data
# -----------------------
df = pd.read_csv("Employee.csv")
df.to_csv("Employee.csv", index=False)



# Data Inspection
# ---------------
df = pd.read_csv("Employee.csv")
print(df.head())                    # First 5 rows
print(df.head(10))                  # First 10 rows
print(df.tail())                    # Last 5 rows
print(df.info())                    # Data types and non-null values
print(df.describe())                # Summary statistics (mean, std, min, max, etc.)

print(df.shape)                     # (rows, columns)
print(df.columns)                   # Column names
print(df.index)                     # Index range
print(df.dtypes)                    # Data types of columns



# Apply Functions
df["Salary_after_Tax"] = df["Salary"].apply(lambda x: x * 0.6)



# Chunking
chunk_size = 10000
for chunk in pd.read_csv("file.csv", chunksize=chunk_size):
    process(chunk)  # Process each chunk separately