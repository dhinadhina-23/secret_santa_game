# 🎁Secret Santa Assignment System
# 📌 Introduction

The Secret Santa Assignment System is a web-based application designed to automate the process of assigning Secret Santa pairs among employees in an organization. The system ensures fairness, anonymity, and adherence to business constraints such as avoiding self-assignments and preventing repetition of last year’s assignments.

This project was developed as a production-ready, modular solution using Django and Python, following Object-Oriented Programming (OOP) principles and best software engineering practices. It supports CSV-based inputs and outputs, making it easy to integrate with existing organizational workflows.

🏢 Background

Company Acme organizes a Secret Santa event every year where each employee is assigned exactly one “secret child” to whom they anonymously give a gift. To streamline and standardize this process, Acme required an automated system that:

Reads employee data from a CSV file

Avoids assigning the same Secret Santa pair as the previous year

Generates a new CSV file with valid assignments

🎯 Project Objectives

Automate Secret Santa assignments

Prevent self-assignments

Prevent repetition of previous year’s assignments

Ensure one-to-one mapping between giver and receiver

Produce downloadable CSV output

Maintain modular, extensible, and testable code

# ✨ Features

📂 Upload employee list via CSV

🔁 Avoid previous year’s Secret Santa pairings

❌ Prevent self-assignment

🔐 One-to-one unique assignment

📄 Download generated Secret Santa assignments as CSV

🧱 Modular service-based architecture

🗃️ Database-backed yearly assignment tracking

🎨 Christmas-themed UI (HTML & CSS)

# 🛠️ Tech Stack
Layer	Technology
Backend	Python 3, Django
Frontend	HTML5, CSS3
Database	MySQL
File Handling	CSV
Architecture	MVC (Django), OOP
Version Control	Git & GitHub
# 📥 Input Format (CSV)

The employee list must be provided in the following format:

Employee_Name,Employee_EmailID
John Doe,john.doe@example.com
Jane Smith,jane.smith@example.com

Previous Year Assignment CSV (Optional)
Employee_Name,Employee_EmailID,Secret_Child_Name,Secret_Child_EmailID
John Doe,john.doe@example.com,Jane Smith,jane.smith@example.com

# 📤 Output Format (CSV)
Employee_Name,Employee_EmailID,Secret_Child_Name,Secret_Child_EmailID
Jane Smith,jane.smith@example.com,John Doe,john.doe@example.com

# ⚙️ Setup & Installation
1️⃣ Clone the Repository
git clone https://github.com/your-username/secret-santa-project.git
cd secret-santa-project

2️⃣ Create Virtual Environment
python -m venv .venv
.venv\Scripts\activate   # Windows

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Apply Migrations
python manage.py makemigrations
python manage.py migrate

5️⃣ Run Server
python manage.py runserver

🚀 How to Use

 Open the application in the browser

 Upload the employee CSV file

 System reads previous year’s assignments (if available)

 Generates valid Secret Santa pairs

 Download the generated CSV file


📁 Django Project Folder Structure
secret_santa_project/
│
├── manage.py
│
├── secret_santa/                 # Project settings folder
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── santa_app/                    # Main application
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── forms.py
│   ├── tests.py
│   │
│   ├── services/                 # Business logic layer
│   │   ├── __init__.py
│   │   ├── secret_santa_service.py
│   │   ├── previous_year_assignment.py
│   │   └── csv_export_service.py
│   │
│   ├── templates/
│   │   └── santa_app/
│   │       ├── upload.html
│   │       └── result.html
│   │
│   └── migrations/
│       ├── __init__.py
│
├── static/                       # CSS, images, animations
│   └── santa_app/
│       └── style.css
│
├── media/                        # Uploaded & generated CSV files
│   └── secret_santa_2025.csv
│
├── requirements.txt
└── README.md

