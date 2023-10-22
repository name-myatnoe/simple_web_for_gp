from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Simple user database (key: email, value: password)
users = {}

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login_post():
    email = request.form['email']
    password = request.form['password']

    if email in users and users[email] == password:
        session['email'] = email
        return render_template('dashboard.html')
    return "Invalid email or password."

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/register', methods=['POST'])
def register_post():
    email = request.form['email']
    password = request.form['password']

    if email in users:
        return "email already taken."

    users[email] = password
    return render_template('dashboard.html')

@app.route('/dashboard')
def daskboard():
    return render_template('dashboard.html')

@app.route('/logout')
def logout():
    session.pop('email', None)
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
