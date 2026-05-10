COSC021W Coursework 2 – Student 2 Contribution
Student Information
FieldDetails
Surname:Pokhrel
name:Sushma
student id:W2083968
Module5COSC021WCourseworkCoursework 2 – Group Project

Project Overview
This is a Django + SQLite web application developed as part of a group project for module 5COSC021W. The project is a full-stack web application with a database backend, admin dashboard, login system, and a structured front-end built using Django templates and Bootstrap.

Student 2 – Sushma Pokhrel (W2083968)
Section Ownership
SectionRoleApplication Front End (HCI / UI-UX)Section LeaderApplication Front End (Security)ContributorProfessional Conduct – Legal & EthicalContributor

My Part – Application Front End (HCI)
Features Implemented

Designed and implemented the UI/UX for the following pages:

[Page Name 1] – e.g. Team Dashboard
[Page Name 2] – e.g. Dependency Graph View
[Page Name 3] – e.g. Organization Overview


Applied consistent Bootstrap 5 styling across all pages
Implemented responsive layout using Bootstrap grid system
Created reusable Django template components (e.g. base.html, navbar, cards)
Integrated vis.js interactive dependency graph (dependency_graph.html)

UI/UX Principles Applied

Consistency – All pages extend base.html ensuring uniform navigation, fonts, and colour palette
Feedback – Empty state messages shown when no data is available (e.g. "No dependencies recorded")
Visibility – Status badges (bg-success, bg-info) used to distinguish upstream vs downstream dependencies at a glance
Affordance – Clickable nodes in the dependency graph with drag and zoom interactions
Accessibility – Semantic HTML elements, contrast-compliant text colours, and descriptive link text


Technologies Used
TechnologyPurposePython 3.xBackend languageDjango 4.xWeb frameworkSQLiteDatabaseBootstrap 5Front-end stylingvis.js 4.21Interactive dependency graphFont AwesomeIconsHTML5 / CSS3Markup and stylingJavaScript (ES5)Client-side interactivity

Project Setup & Installation
Prerequisites

Python 3.10 or above
pip
Git

Steps to Run
bash# 1. Clone the repository
git clone [your-repo-url]
cd [project-folder]

# 2. Create and activate a virtual environment
python -m venv venv
 On Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Apply database migrations
python manage.py migrate

# 5. (Optional) Load sample data
python manage.py loaddata fixtures/sample_data.json

# 6. Run the development server
python manage.py runserver
Then open your browser at: http://127.0.0.1:8000

Login Credentials
RoleUsernamePasswordAdminadminadmin123Test Usertestusertest123

These credentials are for testing purposes only.


Project Structure
project/
│
├── manage.py
├── requirements.txt
├── db.sqlite3
│
├── [app_name]/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── admin.py
│   └── templates/
│       ├── base.html
│       ├── dashboard.html
│       ├── organization/
│       │   └── dependency_graph.html   ← Sushma Pokhrel (W2083968)
│       └── ...
│
└── static/
    ├── css/
    └── js/

Key Files – Sushma Pokhrel (W2083968)
FileDescriptiontemplates/organization/dependency_graph.htmlInteractive vis.js dependency graph with JSON data island patterntemplates/base.htmlBase template with navbar and Bootstrap setuptemplates/dashboard.htmlMain dashboard UIviews.py (HCI-related views)View functions for front-end pages

Security Considerations (Contribution)

Django CSRF protection enabled on all forms
User authentication required to access dashboard pages (@login_required)
No raw SQL used – all queries use Django ORM to prevent SQL injection
XSS prevention via Django's auto-escaping in templates (|escapejs filter applied in JS contexts)
Sensitive data not exposed in client-side JavaScript (JSON data island pattern used)


References

Django Documentation – https://docs.djangoproject.com/
vis.js Network Documentation – https://visjs.github.io/vis-network/docs/network/
Bootstrap 5 Documentation – https://getbootstrap.com/docs/5.0/
Nielsen, J. (1994) 10 Usability Heuristics for User Interface Design. Nielsen Norman Group. Available at: https://www.nngroup.com/articles/ten-usability-heuristics/
University of Westminster (2025) 5COSC021W Coursework 2 Brief. Internal document.

