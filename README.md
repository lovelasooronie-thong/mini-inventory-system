# Mini Inventory Management System

A console-based backend inventory management system built with Python and PostgreSQL.

This project was created to practice backend fundamentals, database design, CRUD operations, validation logic, and backend data flow before learning web frameworks.

---

## Tech Stack

* Python
* PostgreSQL
* psycopg2

---

## Features

### Authentication System

* User login
* Username/password validation
* Database authentication

### Product Management

* Add product
* View products
* Update stock
* Delete product
* Search products

### Search System

* Dynamic product search
* Case-insensitive search using SQL `ILIKE`

### Stock System

* Add stock
* Reduce stock
* Replace stock
* Prevent negative stock validation

### Report System

* Daily update reports
* Product summary
* Category stock summary
* GROUP BY analytics queries
* JOIN between tables

---

## Database Concepts Practiced

* Primary Key
* Foreign Key
* Table Relationships
* Normalization
* JOIN
* GROUP BY
* Aggregate Functions
* Data Validation

---

## Project Structure

```text
inventory_project/

main.py

database/
    DB.py

auth/
    login.py

product/
    product.py

report/
    report.py
```

---

## Concepts Learned

### Backend Fundamentals

* Program flow
* Validation flow
* Error handling
* Separation of responsibility
* Business logic structure

### Python

* Functions
* Loops and conditions
* Modules and packages
* Exception handling
* Import system

### PostgreSQL

* CRUD operations
* SQL queries
* Relation design
* Aggregation queries
* Reporting queries

---

## Future Improvements

* Refactor project structure
* Add transaction/history system
* Add role-based access
* Learn OOP structure
* Build REST API with Flask/FastAPI
* Convert system into web backend

---

## Purpose of This Project

This project was built for learning backend development fundamentals and preparing for software development internships by focusing on:

* Database thinking
* Backend logic
* Data flow
* Debugging skills
* System structure
