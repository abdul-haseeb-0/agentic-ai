# 📊 Pandas: The Ultimate Data Analysis Library

![Python](https://img.shields.io/badge/Python-3.x-blue.svg) ![Pandas](https://img.shields.io/badge/Pandas-✔️-green) ![License](https://img.shields.io/badge/License-MIT-brightgreen.svg)

Pandas is a **powerful and flexible** Python library for data manipulation and analysis.

## 🔹 Installation
```bash
pip install pandas  # or conda install pandas
```

## 🍁 Core Data Structures
### 🔹 Series (1D Data)
```python
import pandas as pd
series = pd.Series([10, 20, 30], index=['a', 'b', 'c'])
print(series)
```
**Output:**
```
a    10
b    20
c    30
dtype: int64
```

### 🔹 DataFrame (2D Data)
```python
data = {"Name": ["Alice", "Bob"], "Age": [25, 30]}
df = pd.DataFrame(data)
print(df)
```
**Output:**
```
    Name  Age
0  Alice   25
1    Bob   30
```

## 📜 Common Operations

### 🔹 Loading Data:
```python
df = pd.read_csv("data.csv")  # Load CSV file
df = pd.read_excel("data.xlsx")  # Load Excel file
df = pd.read_json("data.json")  # Load JSON file
```

### 🔹 Saving Data:
```python
df.to_csv("output.csv", index=False)
df.to_excel("output.xlsx", index=False)
df.to_json("output.json")
```

### 🔹 Data Operations
```python
df.head()  # First 5 rows
df.info()  # Summary
df.describe()  # Stats summary
df["Age"]  # Select column
df.loc[df["Age"] > 25]  # Filter rows
df["Salary"] = df["Age"] * 2000  # Add column
df.drop("Salary", axis=1, inplace=True)  # Remove column
```

### 🔹 Missing Data Handling
```python
df.fillna(0, inplace=True)  # Replace NaN with 0
df.dropna(inplace=True)  # Drop NaN rows
```

### 🔹 Grouping & Aggregation
```python
df.groupby("Age")["Salary"].sum()
```

### 🔹 Merging DataFrames
```python
df1.merge(df2, on="ID", how="inner")
```

### 🔹 Concatenation
```python
pd.concat([df1, df2], ignore_index=True)
```

### 🔹 Sorting Data and Index
```python
df.sort_values("Salary", ascending=True, inplace=True)  # sort by Salary in ascending order
df.sort_values(["ID", "Salary"], ascending=[False, True])  # sort by ID in descending and Salary in ascending order
df.sort_index(inplace=True)  # sort by index
df.reset_index(drop=True, inplace=True)  # reset index
```

### 🔹 Aggregation
```python
df.agg({
    "ID": "max",  # max ID
    "Salary": ["mean", "max"]  # mean and max salary
})
```

### 🔹 Visualization 📊
```python
import matplotlib.pyplot as plt
df["Age"].plot(kind="bar")
plt.show()
```

### 🔹 Apply Functions
```python
df["Salary_after_Tax"] = df["Salary"].apply(lambda x: x * 0.6)
```

### 🔹 Chunking of Data
```python
chunk_size = 10000
for chunk in pd.read_csv("file.csv", chunksize=chunk_size):
    process(chunk)  # Process each chunk separately
```
---
---
---
🌟 **Follow for more Python skills!** 🚀
