from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_NOTIFICATIONS'] = False
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    email = db.Column(db.String(30), nullable = False)
    password = db.Column(db.String(20), nullable = False)
    userName = db.Column(db.String(20), nullable = False)
    age = db.Column(db.Integer, nullable = False)

    def __repr__(self):
        return '<User %r>' % self.id
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

@app.route("/registration", methods=['POST', 'GET'])
def registration():
    if request.method == "POST":
        email = request.form['email']
        password = request.form['password']
        userName = request.form['name']
        age = request.form['age']
        user = User(email=email, password=password, userName=userName, age=age)
        try:
            db.session.add(user)
            db.session.commit()
            return redirect('/v_LK')
        except:
            return "Произошла ошибка"
    else:
        return render_template("temp.html")

@app.route("/v_LK")
def v_LK():
    return render_template("v_LK.html")


@app.route("/user/<string:name>/<int:id>")
def user(name, id):
    return "User page " + name + " - " + str(id)



if __name__ == "__main__":
    app.run(debug=True, use_reloader=True)