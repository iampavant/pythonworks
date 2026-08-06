from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///students.db"
db = SQLAlchemy(app)

class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    branch = db.Column(db.String(50))

with app.app_context():
    db.create_all()

# Read
@app.route("/students")
def students():
    return render_template("students.html", students=Student.query.all())

# Create
@app.route("/add", methods=["GET", "POST"])
def add_student():
    if request.method == "POST":
        student = Student(
            name=request.form["name"],
            branch=request.form["branch"]
        )
        db.session.add(student)
        db.session.commit()
        return redirect("/students")
    return render_template("add.html")

# Update
@app.route("/edit/<int:id>", methods=["GET", "POST"])
def edit_student(id):
    student = Student.query.get(id)
    if request.method == "POST":
        student.name = request.form["name"]
        student.branch = request.form["branch"]
        db.session.commit()
        return redirect("/students")
    return render_template("edit.html", student=student)

# Delete
@app.route("/delete/<int:id>")
def delete_student(id):
    student = Student.query.get(id)
    db.session.delete(student)
    db.session.commit()
    return redirect("/students")

if __name__ == "__main__":
    app.run(debug=True)