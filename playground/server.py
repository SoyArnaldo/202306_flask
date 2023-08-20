from flask import Flask, render_template;

app = Flask(__name__);

@app.route("/play/")
def login():
    return render_template("index.html")

@app.route("/play/<int:number>/")
def box(number):
    return render_template("box.html", numero = number)

@app.route("/play/<int:numero>/<string:color>")
def color(numero,color):
    return render_template("color.html", numero = numero, color = color)

if __name__ == "__main__":
    app.run(debug = True)