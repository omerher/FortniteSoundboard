from flask import Flask, render_template, url_for
import os

path = "static/sounds/"
players = os.listdir(path)
sounds_players = {}
for player in players:
    sounds_players[player] = os.listdir(path + player)

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html", players=sounds_players)

@app.route('/players/<player>/')
def players(player):
    return render_template("players.html", sounds_players=sounds_players, player=player)

if __name__ == "__main__":
    app.run(debug=True)
