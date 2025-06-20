# 🦸 Superheroes

## 📋 Description

This project is a Flask RESTful API for managing superheroes and their superpowers, as well as their associated strength levels via `HeroPower`.

## 🚀 Setup Instructions

1. Clone the repository
2. Set up a virtual environment
3. Install dependencies
4. Run migrations and seed data
5. Start the Flask server

## 📂 API Endpoints

### GET /heroes
Returns a list of all heroes.

### GET /heroes/:id
Returns a specific hero with associated powers.

### GET /powers
Returns all powers.

### GET /powers/:id
Returns a specific power.

### PATCH /powers/:id
Update a power's description.

### POST /hero_powers
Associate a hero with a power and strength level.

## 🛠 Technologies
- Flask
- SQLAlchemy
- Flask-Migrate
- SQLite

# Set-up Instructions
# 1. Clone your private repo
git clone <your-repo-url>
cd flask-superheroes-api

# 2. Create a virtual environment
python3 -m venv venv
source venv/bin/activate

# 3. Install dependencies
pip install Flask Flask-SQLAlchemy Flask-Migrate Flask-Cors

# 4. Initialize database
flask db init
flask db migrate -m "Initial migration"
flask db upgrade

# 5. Seed database
python run.py seed

# 6. Start the server
python run.py
