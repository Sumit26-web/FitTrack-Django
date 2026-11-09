# FitTrack — Django Fitness Tracker

FitTrack is a responsive full-stack fitness tracking web application built with Django. Users can create an account, log workouts and meals, set personal goals, and view an activity dashboard.

## Features

- User registration, login and logout (Django authentication)
- Personal dashboard with weekly workout minutes, calories burned and today's nutrition
- Workout journal: activity, duration, calories, distance, date and notes
- Nutrition journal: meal type, calories and protein
- Personal goals with editable targets and progress
- Per-user data isolation and Django admin
- Responsive dark UI with interactive Chart.js activity chart
- SQLite for local development; PostgreSQL supported for deployment

## Tech stack

- Python 3.12+
- Django 5.x
- SQLite / PostgreSQL
- HTML, CSS, JavaScript
- Chart.js, Lucide icons

## Run locally (Windows PowerShell)

```powershell
# 1. Extract the ZIP and open this folder in VS Code
cd fittrack_django

# 2. Create and activate a virtual environment
py -m venv .venv
.venv\Scripts\Activate.ps1

# If PowerShell blocks activation, run:
# Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass

# 3. Install dependencies
python -m pip install -r requirements.txt

# 4. Create database tables
python manage.py migrate

# 5. (Optional) Create an admin account
python manage.py createsuperuser

# 6. Start the development server
python manage.py runserver
```

Open http://127.0.0.1:8000/ in your browser. Register a new account to begin.

## Run locally (macOS / Linux)

```bash
cd fittrack_django
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

## Push to GitHub

Create an empty repository on GitHub, then run:

```bash
git init
git add .
git commit -m "Initial FitTrack Django application"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/fittrack-django.git
git push -u origin main
```

Replace `YOUR_USERNAME` with your GitHub username.

## Deploy the Django app publicly

**Important:** GitHub Pages only hosts static sites. It cannot run Django/Python server code. Keep the code on GitHub and deploy the Django application using a Python host such as Render.

1. Push this project to GitHub.
2. Sign in to Render and choose **New → Blueprint**.
3. Connect the GitHub repository containing `render.yaml`.
4. Render will provision the web service and PostgreSQL database from the blueprint.
5. Wait for the first deploy, then open the `.onrender.com` URL.
6. Register an account and test the deployed application.

The `build.sh` script installs dependencies, collects static assets and runs migrations. `render.yaml` configures a PostgreSQL database and a web service.

### Deployment notes

- The Render free instance/database availability and sleep/expiry policies can change. Check the current plan details before relying on free hosting.
- Set a strong `SECRET_KEY`; never commit real secrets or `.env` files.
- If using a custom domain, update `ALLOWED_HOSTS` and configure CSRF trusted origins as appropriate.
- Create an admin user on the deployed service using the host's shell: `python manage.py createsuperuser`.
- Use HTTPS in production. `DEBUG=False` is configured by the Render blueprint.

## Project structure

```text
fittrack_django/
├── fittrack/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── tracker/
│   ├── migrations/
│   ├── models.py
│   ├── forms.py
│   ├── views.py
│   ├── urls.py
│   └── admin.py
├── templates/
│   ├── registration/
│   └── tracker/
├── static/css/style.css
├── manage.py
├── requirements.txt
├── build.sh
├── render.yaml
└── Procfile
```

## Notes

- Workout and nutrition data are entered manually; this starter project does not connect to wearable devices or provide medical advice.
- Goal progress is user-entered and is not automatically calculated from activity logs.
- The dashboard's weekly activity chart is populated from the signed-in user's saved workout records.
