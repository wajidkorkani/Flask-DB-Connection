from flask import Flask, render_template as render, redirect, url_for, request
from flask_sqlalchemy import SQLAlchemy as sql

# Initialize the Flask application
app = Flask(__name__)

# Database configuration
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///sql.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# Initialize the database
db = sql(app)


# User model: Represents a user in the database
class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    name = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(100), nullable=False)


# Create the database tables
with app.app_context():
    db.create_all()

# Homepage: Lists all users in the database
@app.route("/")
def Home():
    users = Users.query.all()
    return render("index.html", users=users)



# Signup form: Displays the form to add a new user
@app.route('/form')
def Form():
    return render("form.html")

 
# Handles form submission to add a new user to the database
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
    


# Deletes a user by ID
@app.route("/delete/<int:id>")
def delete(id):
    user = Users.query.get_or_404(id)
    db.session.delete(user)
    db.session.commit()
    return redirect(url_for('Home'))


# Searches users by name or username and displays results
@app.route("/search", methods=['POST'])
def Search():
    if request.method == "POST":
        search = request.form['search']
        users_by_name = Users.query.filter_by(name=search).all()
        users_by_username = Users.query.filter_by(username=search).all()
        return render('search.html', users_by_name=users_by_name, users_by_username=users_by_username)


# Run the Flask application
if __name__ == "__main__":
    app.run(debug=True)
