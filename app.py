from flask import Flask, request, render_template, jsonify
from uuid import uuid4

from boggle import BoggleGame

app = Flask(__name__)
app.config["SECRET_KEY"] = "this-is-secret"

# The boggle games created, keyed by game id
games = {}


@app.get("/")
def homepage():
    """Show board."""

    return render_template("index.html")


@app.post("/api/new-game")
def new_game():
    """Start a new game and return JSON: {game_id, board}."""

    # get a unique string id for the board we're creating
    game_id = str(uuid4())
    game = BoggleGame()
    games[game_id] = game
    #access board + verify we have accessed what we need to access
    board = game.board
    print(f"{board}")

    new_board = {"gameId": f"{game_id}", "board": board}

    return jsonify(new_board)

@app.post('/api/score-word')
def score_word():
    global game
    #extract the JSON from the request.form
    gameId = request.json['gameId']
    word = request.json['word']

    # check if word is illegal
    if not game.is_word_in_word_list(word):
        response =
        return jsonify( {"result": "not a word"})



    # check if word is not on the board

    # if valid, continue

    print("request.form =", gameId)



    return 'hi'