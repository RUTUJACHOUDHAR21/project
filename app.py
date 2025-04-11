from flask import Flask, request, render_template_string, redirect, url_for

app = Flask(__name__)

# HTML Template for Login Page
login_page = '''
<!DOCTYPE html>
<html>
<head>
    <title>Login</title>
</head>
<body>
    <h2>Login Form</h2>
    <form method="POST" action="/login">
        <label>Username:</label><br>
        <input type="text" name="username" required><br><br>
        <label>Password:</label><br>
        <input type="password" name="password" required><br><br>
        <input type="submit" value="Login">
    </form>
</body>
</html>
'''

# Home Route
@app.route('/')
def home():
    return "Hello, CI/CD with GitHub Actions!"

# Login Route (GET + POST)
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        # For demonstration, use hardcoded login check
        if username == "admin" and password == "1234":
            return f"Welcome, {username}!"
        else:
            return "Invalid credentials. Please try again."

    return render_template_string(login_page)

if __name__ == '__main__':
    app.run(debug=True)
