from flask import Flask, render_template, request

app = Flask(__name__)

# All current html files are just a temporary front-end interface, after completing the backend then the React front-end development will start.

@app.route("/", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        print(username)
    return render_template("login.html")

@app.route("/signup", methods=["POST", "GET"])
def signup():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        print(f"Username: {username}\nPassword: {password}")
    return render_template("signup.html")

@app.route("/home")
def home():
    return render_template("home.html")

if __name__ == "__main__":
    app.run()