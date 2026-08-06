from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///students.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    branch = db.Column(db.String(50))

with app.app_context():
    db.create_all()

@app.route("/")
def home():
    return "Database connected and table created."

if __name__ == "__main__":
    app.run(debug=True)
