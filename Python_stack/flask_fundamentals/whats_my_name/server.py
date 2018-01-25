from flask import Flask, render_template, request, redirect
app = Flask(__name__)
# our index route will handle rendering our form
@app.route('/')
def index():
    my_header = "Welcome to this webpage!"
    return render_template("index.html", header = my_header)

@app.route('/process', methods=['POST'])
def get_form():
    print ("Got Form")
    name = request.form['name']
    email = request.form['email']
    return redirect('/')
app.run(debug=True)