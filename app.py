from flask import Flask, render_template, url_for

app = Flask(__name__)


@app.route("/")
@app.route("/home")
def index():
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/enter")
def enter():
    return render_template("enter.html")

@app.route("/registration")
def registration():
    return render_template("registration.html")

@app.route("/user/<string:name>/<int:id>")
def user(name, id):
    return "User page " + name + " - " + str(id)


if __name__ == "__main__":
    app.run(debug=True, use_reloader=True)