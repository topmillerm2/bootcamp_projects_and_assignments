from flask import Flask, render_template, request, flash, redirect, session

app = Flask(__name__)

app.secret_key = 'KeepItSecretKeepItSafe'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods = ['POST'])
def process():
    error= False
    session['fname']= request.form['fname']
    session['lname']= request.form['lname']
    session['email']= request.form['email']
    if len(request.form['fname'])<1 or len(request.form['lname'])<1 or len(request.form['email'])<1 or len(request.form['password'])<1 or len(request.form['confirm_password'])<1:
        flash("All fields must be filled out")
        error = True
    if not request.form['fname'].isalpha() or not request.form['lname'].isalpha():
        flash("First and Last names cannot contain numbers")
        error = True
    if len(request.form['password'])< 8:
        flash("Passwords must be at least 8 characters long")
        error = True
    if request.form['password']!= request.form['confirm_password']:
        flash("Passwords must match!")
        error = True
    if error == True:
        return redirect('/')
    if error == False:
        flash("Registration Successful", "success")
        return redirect('/')

@app.route('/refresh')
def reset():
    session.clear()
    return redirect('/')

    
app.run(debug=True)