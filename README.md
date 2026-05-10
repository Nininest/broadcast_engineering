# Broadcast Engineering Portal
### 5COSC021W – Software Development Group Project | University of Westminster 2025–26

A centralised web application for discovering, managing, and visualising engineering teams at Broadcast Company. Built with Django and SQLite, replacing a manually maintained Excel spreadsheet.

---

## Table of Contents

- [Project Overview](#project-overview)
- [Team Members & Feature Allocation](#team-members--feature-allocation)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [Installation & Setup](#installation--setup)
- [Running the Application](#running-the-application)
- [Importing Sample Data](#importing-sample-data)
- [Running Tests](#running-tests)
- [Admin Access](#admin-access)
- [Version Control](#version-control)

---

## Project Overview

The Broadcast Engineering Portal allows users to:
- Search for engineering teams, departments, and managers
- View team details including members, dependencies, repositories, and contact channels
- Visualise organisational structure and team relationships
- Send and receive internal messages
- Schedule meetings
- Generate reports (PDF/Excel)

---

## Team Members & Feature Allocation

| Student | Feature | App |
|---------|---------|-----|
| Student 1 | Teams – display, search, email, dependencies | `teams` |
| Student 2 | Organisation – departments, team types, org chart | `organization` |
| Student 3 | Messages – inbox, sent, drafts, new message | `messaging` |
| Student 4 | Schedule – meetings, calendar, upcoming events | `schedule` |
| Student 5 | Reports – PDF/Excel export, team summaries | `reports` |

Group tasks (shared): database, user authentication, admin panel — `accounts`, `core`

---

## Tech Stack

| Layer | Technology |
|-------|-----------|
| Backend | Python 3.12, Django 5.x |
| Database | SQLite |
| Frontend | HTML, Bootstrap 5, JavaScript |
| PDF Reports | ReportLab |
| Excel Reports | openpyxl |
| Version Control | Git / GitHub |

---

## Project Structure

```
broadcast_engineering/
├── manage.py
├── import_data.py              # One-time data seeding script (do not commit)
├── requirements.txt
├── README.md                   # This file
│
├── broadcast_engineering/      # Project config
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
│
├── accounts/                   # User auth, registration, login, profile (GROUP)
├── core/                       # Shared base templates, navbar (GROUP)
├── organization/               # Student 2 – Departments, org structure
├── teams/                      # Student 1 – Teams feature
├── messaging/                  # Student 3 – Internal messaging
├── schedule/                   # Student 4 – Meeting scheduler
└── reports/                    # Student 5 – PDF/Excel reports
```

---

## Installation & Setup

### 1. Clone the repository

```bash
git clone https://github.com/Nininest/broadcast_engineering.git
cd broadcast_engineering
```

### 2. Create and activate a virtual environment

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**Mac/Linux:**
```bash
python -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Apply migrations

```bash
python manage.py migrate
```

### 5. Create a superuser (admin)

```bash
python manage.py createsuperuser
```

---

## Running the Application

```bash
python manage.py runserver
```

Then open your browser at:

```
http://127.0.0.1:8000/
```

Admin panel:
```
http://127.0.0.1:8000/admin/
```

---

## Importing Sample Data

A seeding script is provided to populate the database with sample departments, teams, and users.

> **Note:** Do not commit `import_data.py` to the repository — it contains test credentials.

```bash
python import_data.py
```

This will create:
- 6 Departments
- 20 Teams
- 20 Team leader user accounts (password: `Test1234!`)

---

## Running Tests

Run all tests across the entire project:

```bash
python manage.py test
```

Run tests for a specific app:

```bash
python manage.py test accounts
python manage.py test teams
python manage.py test organization
python manage.py test messaging
python manage.py test schedule
python manage.py test reports
```

---

## Admin Access

Log in at `/admin/` with the superuser credentials you created.

The Django admin panel supports:
- Adding, editing, and deleting teams and departments
- Managing user accounts and permissions
- Viewing all messages and schedules
- Full audit trail of changes

---

## Requirements

All dependencies are listed in `requirements.txt`. Key packages:

```
Django>=5.0
reportlab
openpyxl
```

Generate/update requirements file:

```bash
pip freeze > requirements.txt
```

---

## Version Control

- Repository: [https://github.com/Nininest/broadcast_engineering](https://github.com/Nininest/broadcast_engineering)
- Main branch: `main`
- Each student worked on a feature branch (e.g. `feature/reports`, `feature/teams`)
- Pull requests were reviewed by at least one other team member before merging

---

*University of Westminster | School of Computer Science and Engineering | 2025–26*
