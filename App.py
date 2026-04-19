from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/sum5", methods=["GET", "POST"])
def sum5():
    if request.method == "POST":
        a = int(request.form["a"])
        b = int(request.form["b"])
        c = int(request.form["c"])
        d = int(request.form["d"])
        e = int(request.form["e"])

        result = a + b + c + d + e

        return render_template("result31.html", result=result)

    return render_template("index31.html")

if __name__ == "__main__":
    app.run(debug=True)
