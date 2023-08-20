from flask import Flask, session, redirect, render_template, request

app = Flask(__name__)
app.secret_key = "s32ljfcajfnak"

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/process", methods = ["POST"])
def process():
    session["data"] = {
        "name_user": request.form["name_user"],
        "user_language": request.form["user_language"],
        "user_location": request.form["user_location"],
        "user_comments": request.form["user_comments"]
	}
    return redirect("/result")

@app.route("/result")
def result():
    data = ["Name:", "Favorite Language:", "Dojo Location:", "Comments:"]
    return render_template("result.html", data = data)

if __name__ == "__main__":
    app.run(debug = True)