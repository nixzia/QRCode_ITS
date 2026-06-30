from flask import Flask, redirect, render_template
import json

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/qr/<room>")
def redirect_room(room):

    with open("classroom_links.json", "r") as file:
        links = json.load(file)

    if room in links:
        return redirect(links[room])

    return f"Classroom '{room}' not found.", 404


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )