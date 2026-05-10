# Reports App – Student 5 (5COSC021W CWK2)

## Overview

This Django app implements the **Reports** menu item for the Broadcast Engineering Portal.  
It allows users to generate and download reports in **PDF** and **Excel** format, covering team statistics and organisational summaries.

---

## Functional Requirements Covered

- Generate a report showing the **total number of teams**
- Generate a **summary report** of all teams and their departments
- Generate a report of **teams without managers**
- Export reports as **PDF** and **Excel (.xlsx)**

---

## App Structure

```
reports/
├── __init__.py
├── apps.py
├── urls.py
├── views.py
├── templates/
│   └── reports/
│       ├── reports_home.html      # Reports dashboard page
│       └── reports_preview.html   # On-screen preview before download
└── README.md
```

---

## Installation & Dependencies

Install the required Python packages:

```bash
pip install reportlab openpyxl
```

Add the app to `INSTALLED_APPS` in `broadcast_engineering/settings.py`:

```python
INSTALLED_APPS = [
    ...
    'reports',
]
```

---

## URL Configuration

In `broadcast_engineering/urls.py`, include the reports URLs:

```python
from django.urls import path, include

urlpatterns = [
    ...
    path('reports/', include('reports.urls')),
]
```

In `reports/urls.py`:

```python
from django.urls import path
from . import views

app_name = 'reports'

urlpatterns = [
    path('',               views.reports_home,        name='home'),
    path('pdf/summary/',   views.export_pdf_summary,  name='pdf_summary'),
    path('pdf/no-manager/',views.export_pdf_no_manager, name='pdf_no_manager'),
    path('excel/summary/', views.export_excel_summary, name='excel_summary'),
    path('excel/no-manager/', views.export_excel_no_manager, name='excel_no_manager'),
]
```

---

## Views Summary (`reports/views.py`)

| View | Method | Description |
|------|--------|-------------|
| `reports_home` | GET | Dashboard listing all available reports |
| `export_pdf_summary` | GET | PDF: team count + summary table |
| `export_pdf_no_manager` | GET | PDF: teams with no manager assigned |
| `export_excel_summary` | GET | Excel: team summary with department info |
| `export_excel_no_manager` | GET | Excel: teams missing a manager |

---

## Libraries Used

| Library | Purpose |
|---------|---------|
| `reportlab` | PDF generation |
| `openpyxl` | Excel (.xlsx) generation |
| `django.http.HttpResponse` | Serving file downloads |

---

## How to Run

1. Make sure migrations are applied:
   ```bash
   python manage.py migrate
   ```

2. Run the development server:
   ```bash
   python manage.py runserver
   ```

3. Navigate to:
   ```
   http://127.0.0.1:8000/reports/
   ```

---

## Testing

Tests are located in `reports/tests.py`. Run with:

```bash
python manage.py test reports
```

Test cases cover:
- Reports home page loads (HTTP 200)
- PDF download returns correct content type (`application/pdf`)
- Excel download returns correct content type (`.xlsx` MIME type)
- Teams-without-managers report is accurate

---

## Security

- All report views require the user to be logged in (`@login_required`)
- No sensitive data is exposed in report filenames
- File downloads use `Content-Disposition: attachment` to prevent inline execution

---

## Integration Notes

- Reads from `teams.models.Team` and `organization.models.Department`
- No writes to the database — reports are read-only
- Designed to work alongside Student 1 (Teams), Student 2 (Organisation/Departments), and the shared authentication system (group task)

---

## Version Control

All commits pushed to the shared GitHub repository under branch `feature/reports`.  
Merged into `main` after peer review by team members.
