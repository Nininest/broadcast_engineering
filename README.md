# Scheduling App — Swekchhya Thapa Magar
**Student ID:** W2083982  
**Module:** 5COSC021W Group Project  
**Branch:** features/swekchya_scheduling

---

## Overview
This module handles all meeting scheduling functionality for the Broadcast Engineering Teams Portal. It allows users to schedule, view, and manage meetings with team members across the platform.

---

## Files Created

### Models
- `scheduling/models.py` — Meeting model with attendees, platform and date time fields

### App Configuration
- `scheduling/apps.py` — SchedulingConfig app configuration

### URLs
- `scheduling/urls.py` — URL paths for schedule list, new meeting, meeting detail and delete

### Views
- `scheduling/views.py` — Schedule list, schedule meeting, meeting detail and delete meeting views with audit logging

### Admin
- `scheduling/admin.py` — Registered Meeting model in admin

### Templates
- `templates/scheduling/schedule_list.html` — Schedule list template with upcoming, weekly and monthly toggle
- `templates/scheduling/schedule_meeting.html` — Schedule meeting template with date time picker, platform and attendees
- `templates/scheduling/meeting_detail.html` — Meeting detail template showing platform, agenda and attendees

---

## Features
- View upcoming, weekly and monthly meetings
- Schedule a new meeting with title, date/time, platform, agenda and attendees
- Supports multiple platforms: Zoom, Teams, Google Meet, In-Person
- View full meeting details including attendees and agenda
- Delete meetings (organiser only)
- Audit logging for all scheduling actions
- Login required for all views

---

## How to Use
1. Navigate to `http://127.0.0.1:8000/schedule/`
2. Click **+ Schedule Meeting** to create a new meeting
3. Fill in the title, date/time, platform, agenda and attendees
4. Click **Save** to schedule the meeting
5. Click on a meeting to view its details
6. Meetings can be deleted by the organiser only

---

## Commit History

| Date | File | Description |
|------|------|-------------|
| April 10, 2026 | scheduling/apps.py | Added SchedulingConfig app configuration |
| April 12, 2026 | scheduling/urls.py | Added URL paths for schedule list, new meeting, meeting detail and delete |
| April 14, 2026 | scheduling/views.py | Wrote schedule list, schedule meeting, meeting detail and delete meeting views with audit logging |
| April 17, 2026 | templates/scheduling/schedule_list.html | Created schedule list template with upcoming, weekly and monthly toggle |
| April 19, 2026 | templates/scheduling/schedule_meeting.html | Created schedule meeting template with date time picker, platform and attendees |
| April 21, 2026 | templates/scheduling/meeting_detail.html | Created meeting detail template showing platform, agenda and attendees |

---

## Dependencies
- Django 6.0.2
- Shared models: `Meeting` (scheduling), `Team` (teams), `AuditLog` (core)
- Bootstrap 5 (via base template)
- Login required for all views (accounts app)
