from flask import Flask, render_template, request, session

app = Flask(__name__)
app.secret_key = "secret123"

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        name = request.form["name"]
        session["username"] = name
        return f"Hello, {name}. Session created successfully!"
    return render_template("form.html")

if __name__ == "__main__":
    app.run(debug=True)
