
# Flask-DB-Connection

This project is a simple Flask web application that demonstrates how to connect to a database, define models, collect user data via an HTML form, add data to the database, search for users, and delete records. It uses SQLAlchemy for ORM and SQLite as the database backend.

## Features

- SQLite database integration using SQLAlchemy
- User model with username, name, and password fields
- Add new users via a web form
- List all users on the homepage
- Delete users from the database
- Search users by name or username

## Routes

- `/` — Homepage: Lists all users in a table with delete option
- `/form` — Signup form: Add a new user
- `/submit` — Handles form submission (POST)
- `/delete/<id>` — Delete a user by ID
- `/search` — Search users by name or username (POST)

## Templates

- `index.html`: Homepage with user table, search bar, and delete buttons
- `form.html`: Signup form for new users
- `search.html`: Displays search results for users by name or username

## Static Files

- `delete.png`: Delete icon for user table
- `search.css`: CSS for search and navigation styling

## Project Structure

- `Src/app.py`: Main Flask application
- `Src/Templates/`: HTML templates
- `Src/static/`: Static assets (images, CSS)

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

- **Homepage**: View all users, search for users, and delete any user.
- **Add User**: Go to `/form` to add a new user.
- **Search**: Use the search bar on the homepage to find users by name or username.

## License

This project is licensed under the MIT License.
