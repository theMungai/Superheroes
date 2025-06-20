from app import create_app, seed_data
from app.models import db

app = create_app()

if __name__ == '__main__':
    with app.app_context():
        seed_data(db)
    app.run(debug=True)
