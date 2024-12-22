# Campus Parking Organizer

A web application designed to help students, faculty, and staff easily find and reserve parking spots on campus. This system provides real-time updates on parking availability, interactive maps for navigation, and the ability to reserve spots in advance.

## Features

- **User Authentication**: Secure login system with password hashing
- **Role-Based Access Control**: Different access levels for admins and regular users
- **Real-Time Parking Updates**: Check parking availability instantly
- **Interactive Maps**: Easy navigation to available parking spots
- **Booking System**: Reserve parking spots in advance
- **Profile Management**: Update personal information and profile pictures
- **Secure Implementation**: CSRF protection, session management, and cache control

## Prerequisites

- Python 3.7 or later
- MySQL database
- Flask and required dependencies

## Installation

1. Clone the repository
```bash
git clone [repository-url]
```

2. Set up a virtual environment
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# OR
venv\Scripts\activate     # Windows
```

3. Install dependencies
```bash
pip install -r requirements.txt
```

4. Initialize the database
```bash
flask db init
flask db migrate -m "Initial migration."
flask db upgrade
```

5. Run the application
```bash
flask run
```

The application will be available at `http://127.0.0.1:5000/`

## Project Structure

```
ROLE-BASED ACCESS CONTROL/
├── __pycache__/
├── static/
│   ├── css/
│   ├── img/
│   └── js/
├── templates/
│   ├── about.html
│   ├── adminPanel.html
│   ├── base.html
│   ├── index.html
│   ├── login.html
│   ├── profile.html
│   ├── signup.html
│   ├── terms.html
│   └── userManagement.html
├── venv/
├── app.py
├── backend.py
├── requirements.txt
└── schema.sql
```

## Sample Accounts

### Admin
- ID: 221008049
- Password: Adm!nP@ssw0rd

### User
- ID: 98765432
- Password: Chr!st!n@30y2024#

## Tech Stack

- **Backend**: Python with Flask
- **Database**: MySQL
- **Frontend**: HTML, CSS, Bootstrap, JavaScript
- **Security**: Bcrypt for password hashing, CSRF protection

## Key Libraries

- Flask
- Flask-Login
- mysql-connector-python
- Hashlib
- Flask-WTF (for CSRF protection)

## Contributors

**Programmers:**
- Bazar Jayp S

**Documentation:**
- Ubante Jay Marion Bristol

## Future Improvements

- Two-Factor Authentication (2FA)
- Password reset via email
- Frontend modernization with React/Vue.js

## Support

If you encounter any issues, please check the troubleshooting section in the documentation or contact support at [support_email].
