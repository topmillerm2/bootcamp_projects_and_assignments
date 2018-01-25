from flask import Flask, render_template, session, redirect, request
app = Flask(__name__)
import random

app.secret_key = 'sdfkjsdflkjsdlfksjdflksjdf32'

@app.route('/')
def index():
    if session.get('result') == None:
        session['result'] = ''
    if session.get('cpu_num') == None:
        randnum = random.randrange(0,101)
        session['cpu_num'] = randnum
        print (randnum)
    if session.get('player_guess')==None:
        session['player_guess'] = 0
    return render_template("index.html")

@app.route('/input', methods=['POST'])
def guess():
    session['player_guess']= int(request.form['number'])
    if session['player_guess']==session['cpu_num']:
        session['result'] = 'You guessed it correct!'
    elif session['player_guess']>session['cpu_num']:
        session['result'] = 'Too high. Try Again!'
    else:
        session['result'] = 'Too low. Try Again!'
    return redirect('/')

@app.route('/reset')
def reset():
    session.clear()
    return redirect('/')

app.run(debug=True)