
### 1. Prerequisites
- **Python 3.11+** (tested on 3.14)

### 2. Setup

```bash
# from the project folder: UniversityManagementSystem/

# (recommended) create a virtual environment
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS / Linux
source .venv/bin/activate

# install dependencies
pip install -r requirements.txt

# apply database migrations
python manage.py migrate

# load demo data (students, faculty, courses, attendance, fees, events...)
python manage.py seed_demo

# start the server
python manage.py runserver
```

Now open **http://127.0.0.1:8000/** 🎉

> Tip: on Windows PowerShell, if port 8000 is stuck from a previous run, start on another
> port: `python manage.py runserver 8001`.

---

## 🔑 Demo logins

All demo accounts use the password **`demo1234`**.

| Role | Username | Password |
|------|----------|----------|
| 🛡️ Admin | `admin` | `demo1234` |
| 🧑‍🏫 Faculty | `prof.rao` | `demo1234` |
| 🎓 Student | `stu.aarav` | `demo1234` |

After logging in you're routed to the dashboard for that role automatically.
(`admin` is also a Django superuser, so `/django-admin/` works too.)

---

## 🌱 Re-seeding data

```bash
python manage.py seed_demo         # wipes demo data and re-creates it
python manage.py seed_demo --keep  # adds data without wiping
```

The seeder creates ~45 students, 10 faculty, 18 courses, 200+ enrollments and
thousands of attendance/exam/fee records so every chart looks populated.

---

## 🗂️ Project structure

```
UniversityManagementSystem/
├── manage.py
├── requirements.txt
├── config/                 # project settings, urls, wsgi/asgi
├── accounts/               # custom User + roles + Student/Faculty profiles + auth
├── university/             # domain models, dashboards, services, AI, seeder
│   ├── ai.py               # local AI: predictor, assistant, at-risk, recommendations
│   ├── services.py         # analytics & chart-data builders
│   ├── context_processors.py  # per-role theming
│   └── management/commands/seed_demo.py
├── templates/
│   ├── base_public.html    # public navbar + footer
│   ├── base_dashboard.html # themed sidebar + topbar shell
│   ├── public/  accounts/  dashboard/
├── static/css/ums.css, static/js/ums.js
├── docs/screenshots/       # screenshots used in this README
└── report/                 # 50+ page project report (.docx) with all diagrams
```
