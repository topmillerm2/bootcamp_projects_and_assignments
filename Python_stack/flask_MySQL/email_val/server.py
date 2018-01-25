from flask import Flask, request, redirect, render_template, flash
from mysqlconnection import MySQLConnector
app = Flask(__name__)

app.secret_key = "sldkfjslkjfds;f"
mysql = MySQLConnector(app,'emailver') 

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods = ['POST'])
def verification():
    email = request.form['email']
    query = "SELECT email FROM users WHERE email = :email_check"
    data = {'email_check': email}

    email_check = mysql.query_db(query, data)

    if email_check:
        flash("Email is in the database")
        return redirect('/success')
    else:
        query = "INSERT INTO users(email, created_at, updated_at) VALUES (:email, NOW(), NOW())"
        data = {'email': request.form['email']}

        mysql.query_db(query, data)
        flash("Email inserted")
        return redirect('/')
    
@app.route('/success')
def success():
    emails = mysql.query_db("SELECT * FROM users")
    return render_template('success.html', all_emails = emails)

@app.route('/goback')
def goback():
    return redirect('/')
app.run(debug=True)
