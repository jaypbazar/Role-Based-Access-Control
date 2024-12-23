# Energy Monitoring System

## Project Overview
The Energy Monitoring System is a Python-Flask project using a MySQL database. It tracks electrical equipment, operators, and energy consumption, enabling companies to manage equipment ownership, monitor energy usage, and generate alerts. The project promotes efficient resource optimization and sustainability practices within organizations.

Originally developed as a small Database Management System, the application has been refactored to improve scalability, user experience, and functionality. Enhancements include a dynamic user interface, secure login, optimized database interactions, and robust session management.

---

## Features

### Existing Features
- Equipment, operator, and company management.
- Energy usage monitoring.
- Alerts for significant energy consumption.

### New Features and Improvements
- **Navigation Bar**: Easily navigate back to the home page from any other page.
- **Secure Login**: Access the home page only when logged in.
- **Improved Search Functionality**: Search for equipment using keywords.
- **Dynamic Page Layout**: View category data and add new records without leaving the current page.
- **Flash Messages**: Provide consistent error and success notifications.
- **Optimized Backend**: Centralized database operations using the `MySQLDatabase` class.

---

## Installation and Setup Guide

### Prerequisites
Ensure the following are installed:
- [Python](https://www.python.org/downloads/)
- [MySQL](https://www.mysql.com/downloads/)

### Steps
1. **Clone the Repository**
   ```
   git clone https://github.com/jaypbazar/Energy-Monitoring-System-refactor.git
   ```

2. **Set Up a Virtual Environment**
   ```
   python -m venv venv
   venv\Scripts\activate  # On Windows
   source venv/bin/activate  # On macOS/Linux
   ```

3. **Install Dependencies**
   ```
   pip install -r requirements.txt
   ```

4. **Initialize the Database**
   ```
   flask db init
   flask db migrate -m "Initial migration."
   flask db upgrade
   ```

5. **Run the Application**
   ```
   flask run
   ```

---

## User Manual

### Instructions
1. Log in with your account. If you don't have one, click "Sign Up" to register.
2. After logging in, navigate through categories (Equipment, Operators, Energy Usage, Companies) using the dynamic layout.
3. Use the floating action button to add new records.
4. View logs or usage records under the Equipment category and update them as needed.

---

## Technical Overview

### Refactoring Highlights
- Consolidated database queries with the `MySQLDatabase` class, simplifying maintenance and enhancing performance.
- Introduced session management functions to secure user sessions.
- Reduced endpoints and improved data rendering using JavaScript.

### Backend Enhancements
- Added functions for data operations (`/fetch`, `/add`, `/edit`, `/delete`).
- Simplified error handling with flash messages.

### Frontend Enhancements
- Improved user interface using Bootstrap and CSS.
- Dynamically rendered data using JavaScript for smoother transitions.

---

## Testing Documentation

### Strategy
- **Unit Testing**: Focused on components like `MySQLDatabase` class methods.
- **Integration Testing**: Verified Flask backend, MySQL, and JavaScript interactions.
- **End-to-End Testing**: Ensured workflows like login, adding equipment, and viewing logs function correctly.
- **Security Testing**: Validated SQL injection prevention and session handling.

### Key Test Cases
| Test Case                        | Expected Outcome                        | Result  |
|----------------------------------|------------------------------------------|---------|
| Login with valid credentials     | Redirected to the home page             | Passed  |
| Login with invalid credentials   | Display flash message "Invalid login"  | Passed  |
| Add a new equipment record       | Record appears in Equipment category    | Passed  |
| SQL injection attempt on login   | Input sanitized; no data exposed        | Passed  |
| Navigate categories dynamically  | Smooth layout transitions, no reload    | Passed  |

---

## Future Improvements
- **Enhanced Reporting**: Introduce graphical reports for energy usage trends.
- **Role-Based Access Control**: Implement different access levels for admins, operators, and viewers.
- **Mobile App Integration**: Develop a companion mobile app.
- **AI-Based Insights**: Suggest energy optimizations using AI.
- **Advanced Security Measures**: Implement OAuth and two-factor authentication.
