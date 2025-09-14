from flask import Flask, render_template as render, redirect, url_for, request
from flask_sqlalchemy import SQLAlchemy as sql


app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///sql.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = sql(app)

class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    name = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(100), nullable=False)


with app.app_context():
    db.create_all()

@app.route("/")
def Home():
    users = Users.query.all()
    return render("index.html", users=users)



@app.route('/form')
def Form():
    return render("form.html")


@app.route("/submit", methods=["POST"])
def Submit():
    if request.method=="POST":
        username = request.form["username"]
        name = request.form["name"]
        password = request.form["password"]
        addData = Users(username=username, name=name, password=password)
        db.session.add(addData)
        db.session.commit()
        return redirect(url_for('Home'))
    


@app.route("/delete/<int:id>")
def delete(id):
    user = Users.query.get_or_404(id)
    db.session.delete(user)
    db.session.commit()
    return redirect(url_for('Home'))


@app.route("/search", methods=['POST'])
def Search():
    if request.method == "POST":
        search = request.form['search']
        users_by_name = Users.query.filter_by(name=search).all()
        users_by_username = Users.query.filter_by(username=search).all()
        return render('search.html', users_by_name=users_by_name, users_by_username=users_by_username)


if __name__ == "__main__":
    app.run(debug=True)
