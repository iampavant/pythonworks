from flask import Flask
from student import student_bp
from admin import admin_bp

app = Flask(__name__)

app.register_blueprint(student_bp, url_prefix="/student")
app.register_blueprint(admin_bp, url_prefix="/admin")

@app.route("/")
def home():
    return "Welcome to Gitam"

if __name__ == "__main__":
    app.run(debug=True)
