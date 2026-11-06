"# CSIT327-G5-Olivar-EdenAgnes-FirstDjango" 
# CSIT327 Lab: Creating Your First Django Application – Lab Challenge

**Student Name:** Eden Agnes Olivar  
**Section:** G5  
**Course Code:** CSIT327  
**Repository Name:** `CSIT327-G5-Olivar-EdenAgnes-FirstDjango`  

---

## Project Overview

This project is a Django application updated to include full authentication features, a user profile management system, messaging alerts, and modern UI styling. 

### Key Features & Requirements Implemented
1. **User Authentication & Profile Management:**
   - User Sign-Up and Login workflows.
   - Profile page allowing logged-in users to view and update their own details.
   - Built using Django’s class-based `UpdateView`.
2. **Security & Access Control:**
   - Profile routes require authentication using the `LoginRequiredMixin`.
   - Access restriction logic ensuring users can only view and edit their own profiles.
   - Full CSRF protection enabled across all forms.
3. **User Feedback:**
   - Django’s messages framework integrated to display success feedback upon user registration.
4. **UI/UX & Responsive Layout:**
   - Integrated Bootstrap 5 loaded via CDN.
   - Base layout template (`base.html`) featuring a shared responsive navigation bar.
   - Styled forms using Bootstrap classes (`form-control`, `btn`, etc.).
   - Registration success messages displayed cleanly as dismissible Bootstrap alerts.

---

## Setup and Running Instructions

Follow these steps to set up and run the application locally on your machine.

### 1. Prerequisites
- Python 3.10+ installed on your system.
- Git installed on your system.

### 2. Clone the Repository
```bash
git clone https://github.com/agnes-eden/CSIT327-G5-Olivar-EdenAgnes-FirstDjango.git
cd CSIT327-G5-Olivar-EdenAgnes-FirstDjango
```

### 3. Set Up a Virtual Environment
**On Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**On macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 4. Install Dependencies
```bash
pip install -r requirements.txt
```
*(If no `requirements.txt` is present, install Django directly: `pip install django`)*

### 5. Apply Database Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Create a Superuser (Optional)
To access the Django admin panel:
```bash
python manage.py createsuperuser
```

### 7. Run the Development Server
```bash
python manage.py runserver
```

Open your browser and navigate to `http://127.0.0.1:8000/` to test the application.
