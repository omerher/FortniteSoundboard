from flask import Flask, render_template, url_for, redirect, request
import os

path = "static/sounds/"
players = os.listdir(path)
sounds_players = {}
for player in players:
    sounds_players[player] = os.listdir(path + player)

app = Flask(__name__)

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

if __name__ == "__main__":
    app.run(debug=True)
