from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from helpers.application import app

app.config['SQLALCHEMY_DATABASE_URI'] = (
    'postgresql://postgres:emmanuel1@postgres:5432/cbodb'
)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)
