from flask import Flask, render_template, session, redirect, request
app = Flask(__name__)

app.secret_key = 'sdfkjsdflkjsdlfksjdflksjdf32'

@app.route('/')
def count():
    if 'values' in session:
        session['values']+= 1
    else:
        session['values'] = 1

    if 'ninja' in session:
        session['ninja']+= 2
    else:
        session['ninja'] = 1
    return render_template("index.html", count= session['values'], sec_count = session['ninja'])

@app.route('/logout')
def reset():
    session['values'] = 0
    session['ninja'] = 0
    return redirect('/')

app.run(debug=True)
    