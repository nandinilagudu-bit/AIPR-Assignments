# Student Info Portal - Flask Application

## Overview
This is a Flask web application that serves the Student Info Portal with a login form that validates user credentials on the client-side and server-side.

## Features
- ✅ HTML login form with client-side validation
- ✅ Server-side validation with Flask backend
- ✅ Prints username to console on successful login
- ✅ Error handling for empty fields
- ✅ Responsive design that works on all devices
- ✅ JSON-based communication between frontend and backend

## Files Included
- **TaskH.html** - Main HTML page with navigation and login form
- **Task2style.css** - Responsive CSS styling
- **task3.js** - Client-side form validation and Flask API calls
- **task4.py** - Flask backend application

## Setup Instructions

### 1. Install Flask
Open PowerShell and run:
```powershell
pip install flask
```

### 2. Run the Flask Application
Navigate to the project directory and run:
```powershell
python task4.py
```

You should see output like:
```
Starting Student Info Portal Flask App...
Access the application at http://localhost:5000
```

### 3. Access the Application
Open your web browser and navigate to:
```
http://localhost:5000
```

## How to Use

1. **Enter Credentials**: Fill in the username and password fields in the login form
2. **Submit Form**: Click the "Login" button
3. **Validation**: 
   - Client-side: Checks if fields are empty
   - Server-side: Additional validation via Flask backend
4. **Success**: On successful login:
   - Username will be printed to the Flask console
   - Success message appears on the page
   - Form is reset for next attempt

## Example Console Output
When a user logs in with username "student123":
```
✓ Successful Login - Username: student123
```

## API Endpoint

### POST /login
**Request:**
```json
{
    "username": "student123",
    "password": "mypassword"
}
```

**Success Response (200):**
```json
{
    "success": true,
    "message": "Welcome, student123! Login successful.",
    "username": "student123"
}
```

**Error Response (400):**
```json
{
    "success": false,
    "message": "Username is required."
}
```

## Technology Stack
- **Frontend**: HTML5, CSS3, JavaScript (ES6)
- **Backend**: Python Flask
- **Communication**: JSON via Fetch API

## Notes
- The Flask app runs in debug mode for development
- All HTML, CSS, and JS files are served from the same directory
- No database is used; this is a basic authentication demo
- Error messages are displayed to the user on validation failure
