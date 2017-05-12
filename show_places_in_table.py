from flask import Flask
from flask import render_template

from places import Place


@app.route("/places")
def table():
    cafes = Place.query.all()
    return render_template('table.html', cafes=cafes)

if __name__ == "__main__":
    app.run()
