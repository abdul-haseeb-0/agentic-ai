# 📚 Introduction to Databases  
A **database** is a structured collection of data that allows **efficient storage, retrieval, and management**.  

---

## 📂 Types of Databases  

### 🔹 Relational Databases (SQL)  
✅ **Structured Schema** (Tables: Rows & Columns)  
✅ **ACID Compliance** (Atomicity, Consistency, Isolation, Durability)  
✅ **Best for Structured Data** (Banking, ERP)  
💡 **Examples:** MySQL, PostgreSQL, SQLite, SQL Server  

### 🔹 Non-Relational Databases (NoSQL)  
✅ **Flexible Schema** (Documents, Key-Value, Graphs)  
✅ **Highly Scalable & Distributed**  
✅ **Best for Big Data & Real-Time Apps**  
💡 **Examples:** MongoDB, Firebase, Cassandra, Redis  

---

## ⚖ SQL vs NoSQL  

| 🔥 **Feature** | 🏛 **SQL (Relational)** | 🚀 **NoSQL (Non-Relational)** |
|--------------|--------------------|--------------------------|
| **🔎 Structure** | Tables (Rows/Cols) | Documents, Key-Value, Graphs |
| **📜 Schema** | Fixed | Dynamic |
| **📈 Scalability** | Vertical (Scale Up) | Horizontal (Scale Out) |
| **🔄 Transactions** | ACID | BASE (Eventual Consistency) |
| **🔠 Query Language** | SQL | Custom (MQL, etc.) |
| **📌 Best For** | Structured Data, Banking | Big Data, JSON-based Apps |

---

# 🐍 MongoDB + PyMongo CRUD

## 🔌 Connect to MongoDB

```python
from pymongo import MongoClient  

client = MongoClient("mongodb://localhost:27017/")  
db = client["students_db"]  
collection = db["students"]  
🛠️ CRUD Operations
```

## ➕ Create
```python
# Insert One  
collection.insert_one({"name": "Ali", "age": 22, "course": "Database"})  

# Insert Many  
collection.insert_many([  
    {"name": "Sara", "age": 21, "course": "AI"},  
    {"name": "Ahmed", "age": 23, "course": "Web Dev"}  
])
```

## 📖 Read
``` python
# Find One  
print(collection.find_one({"name": "Ali"}))  

# Find All  
for student in collection.find():  
    print(student)  

# Find with Condition  
for student in collection.find({"course": "AI"}):  
    print(student)  
```

## 🔄 Update
```python
# Update One  
collection.update_one({"name": "Ali"}, {"$set": {"age": 23}})  

# Update Many  
collection.update_many({"course": "AI"}, {"$set": {"course": "Machine Learning"}})  
```
## 🗑️ Delete
```python
# Delete One  
collection.delete_one({"name": "Ali"})  

# Delete Many  
collection.delete_many({"course": "Machine Learning"})  
🚀 Bonus: Advanced MongoDB Queries
🔹 Sorting: collection.find().sort("age", -1) (Descending)
🔹 Limit Results: collection.find().limit(5)
🔹 Projection: collection.find({}, {"_id": 0, "name": 1})
```