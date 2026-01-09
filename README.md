---

# Dental Clinic Data Management System

## Overview

The **Dental Clinic Data Management System** is a relational Database Management System (DBMS) developed to manage the core operational data of a dental clinic. The system focuses on **patient records, appointment scheduling, and billing**, ensuring data accuracy, integrity, and efficient retrieval.

The project is implemented using **MySQL** as the backend database and a **lightweight HTML-based frontend**, emphasizing strong database design principles rather than UI complexity.

---

## Problem Statement

Manual record-keeping in dental clinics often leads to:

* Data redundancy and inconsistency
* Difficulty in tracking patient history
* Errors in appointment scheduling and billing
* Inefficient data retrieval

This project addresses these issues by providing a **structured, normalized, and constraint-driven database system** tailored to real-world dental clinic workflows.

---

## System Objectives

* Design a **normalized relational database schema**
* Enforce **data integrity using constraints**
* Model real-world clinic operations accurately
* Enable efficient querying and reporting
* Keep the system simple, scalable, and maintainable

---

## Functional Modules

### 1. Patient Management

* Stores only essential patient details
* Enforces phone number validation at the database level
* Automatically records time of patient entry
* Avoids storing unnecessary personal data such as email or address

### 2. Appointment Management

* Appointments are strictly linked to registered patients
* Treatment types are managed directly within the appointment workflow
* Supports historical appointment tracking
* Ensures relational consistency through foreign keys

### 3. Billing Management

* Billing is generated based on treatments performed
* Automatically updates patient visit history
* Bills can be printed or downloaded as PDF directly from the browser
* No server-side PDF storage is used, ensuring a stateless design

### 4. Search and History Tracking

* Patient search using filters
* Complete appointment and billing history retrieval
* Optimized queries using indexed keys

---

## Technology Stack

| Component | Technology                  |
| --------- | --------------------------- |
| Database  | MySQL                       |
| Frontend  | HTML, CSS                   |
| Tools     | MySQL Workbench / MySQL CLI |
| Platform  | Localhost                   |

---

## Database Design

### Core Tables

* **Patients**
* **Appointments**
* **Billing**

### Design Principles

* Third Normal Form (3NF)
* Primary and Foreign Key constraints
* NOT NULL and CHECK constraints
* Referential integrity enforcement

---

## Project Structure

```
Dental-Clinic-Data-Management/
├── app.py
├── database/
│   ├── schema.sql
│   └── sample_data.sql
│
├── frontend/
│   ├── patients.html
│   ├── appointments.html
│   └── billing.html
│
├── screenshots/
└── README.md
```

---

## Setup and Execution

1. Clone the repository:

```bash
git clone https://github.com/Atharva013/Dental-Clinic-Data-Management.git
```

2. Open MySQL Workbench or MySQL CLI

3. Create and initialize the database:

```sql
SOURCE schema.sql;
```

4. (Optional) Load sample data:

```sql
SOURCE sample_data.sql;
```

5.Run the application loca

---

## Design Constraints and Assumptions

* No user authentication implemented
* Designed for a single-clinic environment
* Minimal patient data stored for privacy
* Focus on backend DBMS concepts over frontend design

---

## Future Scope

* Migration to PostgreSQL
* Role-based access control
* REST API integration (Flask / Node.js)
* Reporting and analytics dashboard
* Cloud deployment support

---

## Learning Outcomes

* Practical application of DBMS concepts
* Schema normalization and constraint design
* Real-world relational modeling
* SQL query optimization
* End-to-end data flow understanding

---

## Author

**Atharva Jadhav**

