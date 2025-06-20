from flask import Flask
from app.models import db
from app.routes import api
from app.seed import seed_data
from flask_migrate import Migrate

migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///heroes.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    app.register_blueprint(api)
    migrate.init_app(app, db)

    return app

if __name__ == '__main__':
    app = create_app()
    with app.app_context():
        db.create_all()
        seed_data(db)  # Optional if seed.py is written
    app.run(debug=True)
