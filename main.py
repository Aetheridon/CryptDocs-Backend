from flask import Flask, render_template

app = Flask(__name__)

# All current html files are just a temporary front-end interface, after completing the backend then the React front-end development will start.

@app.route("/")
def login():
    return render_template("login.html")

@app.route("/signup")
def signup():
    return render_template("signup.html")

@app.route("/home")
def home():
    return render_template("home.html")

if __name__ == "__main__":
    app.run()