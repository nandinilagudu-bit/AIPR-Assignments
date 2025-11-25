// Login Form Validation Script

function validateLoginForm(event) {
    // Prevent form submission
    event.preventDefault();
    
    // Get form elements
    const username = document.getElementById('username').value.trim();
    const password = document.getElementById('password').value.trim();
    
    // Clear previous error messages
    clearErrorMessages();
    
    // Validate username and password
    let isValid = true;
    
    if (username === '') {
        displayError('usernameError', 'Username is required. Please enter your username.');
        isValid = false;
    }
    
    if (password === '') {
        displayError('passwordError', 'Password is required. Please enter your password.');
        isValid = false;
    }
    
    // If validation passes, send to server
    if (isValid) {
        console.log('Working on submit JS validation.');
        submitLoginToServer(username, password);
    }
    
    return false;
}

function submitLoginToServer(username, password) {
    // Send login data to Flask backend
    fetch('/login', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            username: username,
            password: password
        })
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            displaySuccessMessage(`Welcome, ${data.username}! Login successful.`);
            // Reset the form
            document.getElementById('loginForm').reset();
        } else {
            displayError('usernameError', data.message);
        }
    })
    .catch(error => {
        console.error('Error:', error);
        displayError('usernameError', 'An error occurred. Please try again.');
    });
}

function displayError(elementId, message) {
    const errorElement = document.getElementById(elementId);
    if (errorElement) {
        errorElement.textContent = message;
        errorElement.style.display = 'block';
        errorElement.style.color = '#e74c3c';
        errorElement.style.fontSize = '0.9em';
        errorElement.style.marginTop = '5px';
    }
}

function clearErrorMessages() {
    const errorElements = document.querySelectorAll('.error-message');
    errorElements.forEach(element => {
        element.textContent = '';
        element.style.display = 'none';
    });
    
    // Clear success message
    const successElement = document.getElementById('successMessage');
    if (successElement) {
        successElement.textContent = '';
        successElement.style.display = 'none';
    }
}

function displaySuccessMessage(message) {
    const successElement = document.getElementById('successMessage');
    if (successElement) {
        successElement.textContent = message;
        successElement.style.display = 'block';
        successElement.style.color = '#27ae60';
        successElement.style.fontSize = '0.95em';
        successElement.style.marginTop = '10px';
    }
}

// Optional: Clear error message when user starts typing
document.addEventListener('DOMContentLoaded', function() {
    const usernameInput = document.getElementById('username');
    const passwordInput = document.getElementById('password');
    
    if (usernameInput) {
        usernameInput.addEventListener('focus', function() {
            clearErrorMessages();
        });
    }
    
    if (passwordInput) {
        passwordInput.addEventListener('focus', function() {
            clearErrorMessages();
        });
    }
});
