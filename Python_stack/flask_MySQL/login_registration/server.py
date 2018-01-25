from flask import Flask, render_template, redirect, request, flash, session
from mysqlconnection import MySQLConnector
import re
import md5
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
app = Flask(__name__)

app.secret_key = "sldkfjslkjfds;f"
mysql = MySQLConnector(app,'login') 

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods = ['POST'])
def verification():
    email = request.form['email']
    password = md5.new(request.form['password']).hexdigest()
    query = "SELECT email,password FROM users WHERE email = :email_check AND password = :password_check"
    data = {
        'email_check': email,
        'password_check': password
    }
    
    email_check = mysql.query_db(query, data)

    if not EMAIL_REGEX.match(request.form['email']):
        flash("Invalid Email Address!")
        return redirect('/')
    else:
        if email_check:
            flash("You are now Logged In!")
            return redirect('/success')
        else:
            flash("Email not found, please register")
            return redirect('/register')

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/registerprocess', methods = ['POST'])
def verify():
    error = False

    if len(request.form['first_name'])<1 or len(request.form['last_name'])<1 or len(request.form['email'])<1 or len(request.form['password'])<1 or len(request.form['confirm'])<1:
        # session['result'] = "All fields must be filled out"
        flash("All fields must be filled out")
        error = True

    if not request.form['first_name'].isalpha() or not request.form['last_name'].isalpha():
        flash("First and Last names cannot contain numbers")
        error = True

    if not EMAIL_REGEX.match(request.form['email']):
        flash("Invalid Email Address!")
        error=True

    if len(request.form['password'])< 8:
        flash("Passwords must be at least 8 characters long")
        error = True

    if request.form['password'] != request.form['confirm']:
        flash("Passwords must match!")
        error = True

    if error:
        return redirect('/register')
    
    else:
        query = "INSERT INTO users (first_name, last_name, email, password, created_at, updated_at) VALUES (:f_name, :l_name, :email, :password, NOW(), NOW())"
        
        data = {
        'f_name': request.form['first_name'],
        'l_name': request.form['last_name'],
        'email': request.form['email'],
        'password': md5.new(request.form['password']).hexdigest()
        }

        mysql.query_db(query, data)
        flash("Successfully Registered! You are now Logged In!")
        return redirect('/success')

@app.route('/success')
def success():
    return render_template('success.html')

@app.route('/logout')
def logout():
    return redirect('/')
app.run(debug=True)