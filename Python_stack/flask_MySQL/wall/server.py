from flask import Flask, render_template, redirect, request, flash, session
from mysqlconnection import MySQLConnector
import re
import md5
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
app = Flask(__name__)

app.secret_key = "sldkfjslkjfds;f"
mysql = MySQLConnector(app,'wall') 

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods = ['POST'])
def login():
    email = request.form['email']
    password = md5.new(request.form['password']).hexdigest()
    query = "SELECT first_name, email,password FROM users WHERE email = :email_check AND password = :password_check"
    data = {
        'email_check': email,
        'password_check': password
    }
    email_check = mysql.query_db(query, data)

    if not EMAIL_REGEX.match(request.form['email']):
        flash("Invalid Email Address!", "login")
        return redirect('/')
    else:
        if email_check:
            profile_query = "SELECT id, first_name, last_name, email FROM users WHERE email = :email_check"
            data = {'email_check': email}
            profile= mysql.query_db(profile_query, data)
            session['name'] = profile[0]['first_name'] + " " + profile[0]['last_name']
            session['id'] = profile[0]['id']

            flash("You are now Logged In!")
            return redirect('/wall')
        else:
            flash("Email or Password is incorrect/invalid, please re-try or register below", "login" )
            return redirect('/')

@app.route('/register', methods = ['POST'])
def register():
    session['name'] = request.form['first_name']
    error = False
    if len(request.form['first_name'])<1 or len(request.form['last_name'])<1 or len(request.form['email'])<1 or len(request.form['password'])<1 or len(request.form['confirm'])<1:
        # session['result'] = "All fields must be filled out"
        flash("All fields must be filled out", "register")
        error = True

    if not request.form['first_name'].isalpha() or not request.form['last_name'].isalpha():
        flash("First and Last names can only contain letters", "register")
        error = True

    if not EMAIL_REGEX.match(request.form['email']):
        flash("Invalid Email Address!", "register")
        error=True

    if len(request.form['password'])< 8:
        flash("Passwords must be at least 8 characters long", "register")
        error = True

    if request.form['password'] != request.form['confirm']:
        flash("Passwords must match!", "register")
        error = True

    if error:
        return redirect('/')
    
    else:
        query = "INSERT INTO users (first_name, last_name, email, password, created_at, updated_at) VALUES (:f_name, :l_name, :email, :password, NOW(), NOW())"
        
        data = {
        'f_name': request.form['first_name'],
        'l_name': request.form['last_name'],
        'email': request.form['email'],
        'password': md5.new(request.form['password']).hexdigest()
        }

        mysql.query_db(query, data)
        flash("Successfully Registered! Please log in above!", "register")
        return redirect('/')

@app.route('/wall')
def wall():
        messageget_query = "SELECT*FROM users JOIN messages ON users.id = messages.users_id ORDER BY messages.created_at DESC"
        display = mysql.query_db(messageget_query)
        

        commentget_query = "SELECT first_name, last_name, comment, messages_id, comments.created_at, comments.updated_at FROM comments JOIN users ON comments.users_id = users.id JOIN messages ON messages.id = comments.messages_id ORDER BY comments.created_at"
        com = mysql.query_db(commentget_query)

        return render_template('wall.html', com = com, display = display)

@app.route('/insert', methods = ['POST'])
def insert():
    if request.form['action'] == 'message':
        message_query = "INSERT INTO messages (message, created_at, updated_at, users_id) VALUES (:message, NOW(), NOW(), :user_id)"
        data = {
            'user_id': session['id'],
            'message': request.form['message'] 
        }
        mysql.query_db(message_query, data)

    if request.form['action'] == 'comment':
        message_id = request.form['message_id']
        comment_query = "INSERT INTO comments (comment, created_at, updated_at, users_id, messages_id) VALUES (:comment, NOW(), NOW(), :user_id, :message_id )"
        print (message_id)
        data = {
            'comment': request.form['comment'],
            'user_id': session['id'],
            'message_id': message_id
        }
        print (data)
        mysql.query_db(comment_query, data)

    return redirect('/wall')

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')
app.run(debug=True)