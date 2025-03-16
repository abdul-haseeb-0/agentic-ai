# 📊 Pandas: A Comprehensive Guide

![Python](https://img.shields.io/badge/Python-3.x-blue?style=flat&logo=python)
![Pandas](https://img.shields.io/badge/Pandas-1.x-red?style=flat&logo=pandas)
![License](https://img.shields.io/badge/License-MIT-green)

## 📌 Overview
Pandas is a **powerful and flexible** Python library for **data analysis and manipulation**. It provides intuitive **data structures** and **functions** to make working with structured data easier. 🏆

---

## 🚀 Installation

Install Pandas using pip:
```bash
pip install pandas
```
Or for conda users:
```bash
conda install pandas
```

---

## 🔑 Key Features
✔ **Fast and efficient DataFrame manipulation**
✔ **Handling missing data seamlessly**
✔ **Powerful group-by and aggregation functions**
✔ **Easy merging and joining of datasets**
✔ **Built-in visualization with Matplotlib**
✔ **Time series support**

---

## 📂 Core Data Structures

### 🔹 1. Series (1D Data)
A **one-dimensional labeled array** holding any data type.
```python
import pandas as pd

data = [10, 20, 30, 40]
series = pd.Series(data, index=['a', 'b', 'c', 'd'])
print(series)
```
**Output:**
```
a    10
b    20
c    30
d    40
dtype: int64
```

### 🔹 2. DataFrame (2D Data)
A **two-dimensional labeled table-like structure**.
```python
data = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [25, 30, 35],
    "Salary": [50000, 60000, 70000]
}
df = pd.DataFrame(data)
print(df)
```
**Output:**
```
     Name  Age  Salary
0   Alice   25  50000
1     Bob   30  60000
2  Charlie   35  70000
```

---

## 📜 Common Operations
### 📥 Loading and Saving Data
```python
df = pd.read_csv("data.csv")  # Load CSV file
df.to_csv("output.csv", index=False)  # Save CSV file
```

### 🔍 Data Inspection
```python
df.head()       # First 5 rows
df.tail()       # Last 5 rows
df.info()       # Summary
df.describe()   # Statistical summary
df.shape        # Rows & Columns count
df.columns      # Column names
df.dtypes       # Data types
```

### 🎯 Selecting Data
```python
df["Name"]       # Single column as Series
df[["Name", "Age"]]  # Multiple columns as DataFrame

df.iloc[0]       # First row (Index-based)
df.loc[1]        # Row by label/index
df.loc[df["Age"] > 30]  # Filtering rows
```

### 🛠️ Data Manipulation
```python
df["Bonus"] = df["Salary"] * 0.10  # Add new column
df.drop("Bonus", axis=1, inplace=True)  # Remove column

df.loc[3] = ["David", 40, 80000]  # Add new row
df.drop(3, axis=0, inplace=True)  # Remove row
```

### 🚫 Handling Missing Data
```python
df.isnull().sum()  # Count missing values
df.fillna(0, inplace=True)  # Replace NaN with 0
df.dropna(inplace=True)  # Drop rows with NaN values
```

### 🔄 Merging and Joining Data
```python
df1 = pd.DataFrame({"ID": [1, 2, 3], "Salary": [1000, 2000, 3000]})
df2 = pd.DataFrame({"ID": [1, 2, 4], "Bonus": [100, 200, 400]})

merged_df = df1.merge(df2, on="ID", how="inner")  # Inner join
```

---

## 📊 Visualization
```python
import matplotlib.pyplot as plt

df["Salary"].plot(kind="bar")  # Bar chart
df.plot(x="Age", y="Salary", kind="line")  # Line chart
plt.show()
```

---

## 📜 License
This project is licensed under the **MIT License**.

---

## 💡 Resources & Documentation
📖 Official Pandas Docs: [https://pandas.pydata.org/docs/](https://pandas.pydata.org/docs/)

📌 **Follow for more Python skills!** 🚀
