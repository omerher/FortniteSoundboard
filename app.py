from flask import Flask, render_template, url_for, redirect, request, flash
from werkzeug.utils import secure_filename
import os
from os.path import join, dirname, realpath

UPLOADS_PATH = join(dirname(realpath(__file__)), 'static/uploads')

path = "static/sounds/"
players = os.listdir(path)
sounds_players = {}
for player in players:
    sounds_players[player] = os.listdir(path + player)

ALLOWED_EXTENSTIONS = {'mp3', 'wav'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOADS_PATH
app.secret_key = b'_6mew"HES3wd/4xec]/'

@app.route('/')
def index():
    return render_template("index.html", players=sounds_players, query="")

@app.route('/players/<player>/')
def players(player):
    return render_template("players.html", sounds_players=sounds_players, player=player)

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/search', methods=['POST'])
def search():
    query = request.form["search"]
    return render_template("index.html", players=sounds_players, query=query)

@app.route('/submit')
def submit():
    return render_template("submit.html", players=sounds_players)

@app.route('/submit-file', methods=["GET", "POST"])
def submitfile():
    if request.method == "POST":
        if 'file' not in request.files:
            flash("No file part")
            return redirect('/')
        
        file = request.files["file"]
        player_name = request.form["player-name"]
        filename = secure_filename(file.filename)
        
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        
        if player_name != "other":
            filename = player_name + "_" + filename  # formats the file name
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        else:
            player_name = request.form["other"]
            filename = player_name + "_" + filename  # formats the file name
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        
        flash("Success!")
        return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)
