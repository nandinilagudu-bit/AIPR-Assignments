from flask import Flask, render_template, request, jsonify
import os

app = Flask(__name__, 
            template_folder=os.path.dirname(os.path.abspath(__file__)),
            static_folder=os.path.dirname(os.path.abspath(__file__)))

@app.route('/')
def index():
    """Serve the main HTML page"""
    return render_template('TaskH.html')

@app.route('/login', methods=['POST'])
def login():
    """Handle login form submission"""
    try:
        # Get JSON data from request
        data = request.get_json()
        username = data.get('username', '').strip()
        password = data.get('password', '').strip()
        
        # Validate username and password
        if not username:
            return jsonify({
                'success': False,
                'message': 'Username is required.'
            }), 400
        
        if not password:
            return jsonify({
                'success': False,
                'message': 'Password is required.'
            }), 400
        
        # Successfully logged in - print username to console
        print(f"✓ Successful Login - Username: {username}")
        
        return jsonify({
            'success': True,
            'message': f'Welcome, {username}! Login successful.',
            'username': username
        }), 200
    
    except Exception as e:
        print(f"Error during login: {str(e)}")
        return jsonify({
            'success': False,
            'message': 'An error occurred during login.'
        }), 500

if __name__ == '__main__':
    print("Starting Student Info Portal Flask App...")
    print("Access the application at http://localhost:5000")
    app.run(debug=True, host='localhost', port=5000)
