from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def intro():
    tag = "No Ninjas Here!"
    return render_template("index.html", header = tag)

@app.route('/ninja')
def ninja():
    return render_template("ninja.html")

@app.route('/ninja/<color>')
def color(color):
    if color == "blue":
        return render_template("leo.html")
    if color == "orange":
        return render_template("mich.html")
    if color == "red":
        return render_template("raph.html")
    if color == "purple":
        return render_template("don.html")
    return render_template("notapril.html")

app.run(debug=True) 

