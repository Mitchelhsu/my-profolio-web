from flask import Flask, request, render_template


class CustomFlask(Flask):
    jinja_options = Flask.jinja_options.copy()
    jinja_options.update(dict(
        block_start_string='(%',
        block_end_string='%)',
        variable_start_string='((',
        variable_end_string='))',
        comment_start_string='(#',
        comment_end_string='#)',
    ))

app = CustomFlask(__name__)

@app.route("/")
def fromPage():
    return render_template('index.html')

@app.route("/DinnerPicker/")
def dinner():
    return render_template('DinnerPicker.html')

@app.route("/ClubCourse/")
def club():
    return render_template('ClubCourse.html')

@app.route("/PsychTest/")
def psych():
    return render_template('PsychTest.html')

@app.route("/RPG/")
def rpg():
    return render_template('RPG.html')

@app.route("/YTPlayer/")
def youtube():
    return render_template('YTPlayer.html')

@app.route("/Movies")
def movies():
    return render_template('Movies.html')

@app.route("/Galaxy")
def galaxy():
    return render_template('Galaxy.html')

@app.route("/Salary")
def salary():
    return render_template('Salary.html')

if __name__ == '__main__':
    app.run(debug=True)