from flask import Flask, request, render_template, redirect, url_for





app = Flask(__name__)
app.secret_key = "RapemanBruh"



@app.route("/", methods=["POST", "GET"])
def home():
    return render_template("index.html")





if __name__ == "__main__":
    app.run(debug=True)