from flask import Flask, render_template, request, redirect
app = Flask(__name__)
# our index route will handle rendering our form
@app.route('/')
def index():
    my_header = "Welcome to this webpage!"
    return render_template("index.html", header = my_header)

@app.route('/ninjas')
def ninja_fo():
    info_img="http://www.freepngimg.com/download/ninja/1-2-ninja-download-png.png"
    info_txt = 'A ninja (忍者) or shinobi (忍び, "to sneak") was a covert agent or mercenary in feudal Japan. The functions of the ninja included espionage, sabotage, infiltration, assassination and guerrilla warfare.'
    return render_template("ninjas.html", txt = info_txt, img = info_img)
@app.route('/dojos/new')
def form():
    return render_template("dojos.html")
app.run(debug=True) 