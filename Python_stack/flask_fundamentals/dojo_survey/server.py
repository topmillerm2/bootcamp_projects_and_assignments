from flask import Flask, render_template, request, redirect, session, flash
app = Flask(__name__)
# our index route will handle rendering our form

app.secret_key = 'KeepItSecretKeepItSafe'

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/process', methods=['POST'])
def process():
    error = False
    if len(request.form['name'])<1 or len(request.form['comment'])<1:
        flash("Name and Comment Sections must be filled out")
        error = True
    if len(request.form['comment'])>120:
        flash("Comment section too long.")
        error = True
    if error:
        return redirect('/')
    print ("Submitted Info")
    name = request.form['name']
    location = request.form['location']
    favorite_language = request.form['fav_lang']
    comment = request.form['comment']
    my_dict = {
        "name": request.form['name'],
        "location": request.form['location'],
        "favorite_language": request.form['fav_lang'],
        "comment": request.form['comment']
    }
    
    return render_template("result.html", values = my_dict)
app.run(debug=True) 