# Django Authentication System

## Overview
This Django application provides a complete user authentication system, including:

- User signup and login using email or username.
- Password reset functionality.
- Password change functionality.

## Features
- **User Registration:** Allows users to sign up with a username, email, and password.
- **User Login & Logout:** Secure authentication using Django’s built-in authentication system.
- **Forgot Password:** Users can request a password reset via email.
- **Change Password:** Authenticated users can update their passwords.
- **Dashboard:** Restricted to logged-in users, displaying a personalized greeting.
- **Profile Page:** Displays user details.


## Installation
### 1. Clone the Repository
```bash
git clone https://github.com/Aakash47/Django-user-authentication.git
cd Django-user-authentication
```

### 2. Create a Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure the Database
Apply migrations:
```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Create a Superuser
```bash
python manage.py createsuperuser
```
Follow the prompts to set up an admin account.

### 6. Run the Development Server
```bash
python manage.py runserver
```

## Usage
- Visit `http://127.0.0.1:8000/signup/` to create an account.
- Log in at `http://127.0.0.1:8000/login/`.
- Access the dashboard at `http://127.0.0.1:8000/dashboard/`.
- View your profile at `http://127.0.0.1:8000/profile/`.
- Reset password using `http://127.0.0.1:8000/password_reset/`.
---