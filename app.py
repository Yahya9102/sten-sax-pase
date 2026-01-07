from flask import Flask, render_template, request

from db import init_db,insert_round,get_stats
from game import get_computer_choice, get_result

app = Flask(__name__)


init_db()


@app.get("/")
def index():
    stats = get_stats()
    return render_template("index.html",stats=stats)



@app.post("/play")
def play():
    player_choice = request.form.get("choice")
   

    if player_choice not in ["sten", "sax", "påse"]:
        return "Ogiltigt val", 400
    
    computer_choice = get_computer_choice()
    result = get_result(player_choice, computer_choice)
    
    insert_round(player_choice, computer_choice, result)


    stats = get_stats()
    return render_template(
        "result.html",
        player_choice=player_choice,
        computer_choice = computer_choice,
        result=result,
        stats=stats,
    )



if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)