from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def about():
    return render_template('main_page.html')

@app.route('/projects')
def projects():
    my_projects = ['Danger Zones', 'Fat Unicorn: The Poopening', 'My Cohort', 'Certify Me', 'Woof Woof Go!']
    return render_template('projects.html', projects = my_projects)

@app.route('/about')
def paragraph():
    return render_template('about.html')

app.run(debug=True)

