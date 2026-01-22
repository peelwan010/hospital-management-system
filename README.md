# Hospital Management System

A locally hosted hospital management system built using Python and Flask, designed to manage patient records through a clean admin dashboard.

The system is intended for internal hospital use on localhost or a local network (LAN) and is not designed for public internet deployment.

--------------------------------------------------

FEATURES

- Admin dashboard
- Patient management with full CRUD functionality
  - Add patients
  - View patient records
  - Edit patient details
  - Delete patient records
- Persistent local database storage
- Clean, server-rendered user interface
- Modular and readable backend architecture

--------------------------------------------------

TECH STACK

- Python
- Flask
- Flask-SQLAlchemy
- SQLite (local database)
- HTML & CSS (server-rendered templates)

--------------------------------------------------

PROJECT STRUCTURE

hospital-management-system
│
├── app
│   ├── __init__.py        # App factory & database initialization
│   ├── auth.py            # Authentication routes
│   ├── models.py          # Database models
│   ├── routes.py          # Main application routes
│   │
│   └── templates
│       ├── base.html
│       ├── dashboard.html
│       ├── patients.html
│       └── edit_patient.html
│
├── static
│   └── style.css          # Global styles
│
├── run.py                 # Application entry point
├── requirements.txt       # Dependencies
└── README.md

--------------------------------------------------

HOW TO RUN LOCALLY

1. Clone the repository

   git clone https://github.com/peelwan010/hospital-management-system.git

   cd hospital-management-system

2. Create and activate a virtual environment

   python -m venv venv

   source venv/Scripts/activate

3. Install dependencies

   pip install -r requirements.txt

4. Run the application

   python run.py

5. Open in browser

   http://127.0.0.1:5000


--------------------------------------------------

BACKGROUND

This project was originally inspired by the need for simple, local-first hospital record management systems, particularly in environments where internet-based solutions are impractical.

It was later rebuilt with a cleaner backend architecture and a presentable UI to serve as a structured backend-focused project demonstrating CRUD operations, routing, and database integration.

--------------------------------------------------

STATUS

Core functionality completed.

Potential future improvements:
- Doctor and staff management
- Appointment scheduling
- Session-based authentication and access control
- UI refinements

--------------------------------------------------

NOTES

- The application runs entirely on localhost.
- No cloud services or external hosting are used.
- Designed to be simple, reliable, and easy to understand.
