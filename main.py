from flask import Flask
from flask import render_template, redirect
from DB_functions import get_all_cafes_from_db

app = Flask(__name__)

@app.route("/", methods=["GET"])
def main_button():
    return render_template("index.html")

@app.route("/map", methods=["POST"])
def show_map():
    cafes = get_all_cafes_from_db()
    return render_template('cafe_map.html', cafes=cafes)


if __name__ == "__main__":
    app.run(debug=True)
