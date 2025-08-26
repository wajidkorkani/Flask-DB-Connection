# Flask-DB-Connection

This project is a simple Flask web application demonstrating how to connect to a database, define models, collect user data via an HTML form, add data to the database, and delete records.

## Features
- SQLite database integration using SQLAlchemy
- User model with username, name, and password fields
- Add new users via a web form
- List all users on the homepage
- Delete users from the database

## Project Structure

- `Src/app.py`: Main Flask application
- `Src/Templates/index.html`: Homepage listing users
- `Src/Templates/form.html`: Form to add new users
- `Src/static/delete.png`: Delete icon (used in templates)

## Setup Instructions
1. **Clone the repository**
2. **Install dependencies**:
	- Python 3.x
	- Flask
	- Flask-SQLAlchemy
	- Install with:
	  ```powershell
	  pip install flask flask_sqlalchemy
	  ```
3. **Run the application**:
	```powershell
	python Src/app.py
	```
4. **Access the app**:
	- Open your browser and go to `http://127.0.0.1:5000/`

## Usage
- **Homepage**: View all users and delete any user.
- **Add User**: Go to `/form` to add a new user.

## License
This project is licensed under the MIT License.
