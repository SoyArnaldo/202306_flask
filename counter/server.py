from flask import Flask, render_template, redirect, session;

app = Flask(__name__)
app.secret_key = "keep it secret, keep it safe"

@app.route("/")
def home():
	if "session" in session:
		print('la llave existe!')
		session["session"] += 1
	else:
		print("la llave 'key_name' NO existe")
		session["session"] = 1
	
	return render_template("index.html")

@app.route("/count",  methods = ["POST"])
def login():
	return redirect("/")


@app.route("/destroy_session", methods = ["POST"])
def logout():
	session.pop("session")
	return redirect("/")

if "__main__" == __name__:
    app.run(debug = True)