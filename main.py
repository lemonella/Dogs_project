from flask import Flask
from flask import render_template, redirect


app = Flask(__name__)

@app.route("/", methods=["GET"])
def main_button():
	return render_template("index.html")

app.route("/map", methods=["POST"])
def show_map():
	return render_template("map.html")


if __name__ == "__main__":
    app.run()
