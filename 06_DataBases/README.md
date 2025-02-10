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

## 🚀 MongoDB + PyMongo CRUD Operations  
MongoDB is a **NoSQL document-based database**, and **PyMongo** is a Python library for interacting with MongoDB.  

### ⚙ 1. Install PyMongo  
```bash
pip install pymongo
