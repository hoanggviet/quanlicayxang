from flask import Flask
from models import *

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:2003@localhost:5432/QLCayXang"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)

def main():
    # db.drop_all()
    db.create_all()

if __name__ == "__main__":
    with app.app_context():
        main()
