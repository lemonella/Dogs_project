from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"
    return render_template('hello.html', name=name)

if __name__ == "__main__":
    app.run(debug=True)