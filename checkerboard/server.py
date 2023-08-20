from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def login():
    return render_template("index.html")

@app.route("/<int:id>/")
def modify(id):
    return render_template("modify.html", id = int(8/id))

@app.route("/<int:num1>/<int:num2>/")
def modify1(num1, num2):
    return render_template("modify1.html", num1 = int(num1/2), 
                            num2 = int(num2/2), width = str(80 * num2))

@app.route("/<int:num1>/<int:num2>/<string:color1>/<string:color2>/")
def modify2(num1, num2, color1, color2):
    context = {
        "num1": int(num1/2), 
        "num2": int(num2/2), 
        "color1": color1,
        "color2": color2,
        "width": str(80 * num2)
    }
    return render_template("modify2.html", context = context)

if "__main__" == __name__:
    app.run(debug = True)