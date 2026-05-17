from flask import Flask, render_template, request
from generator import generate_password

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    password = None
    error = None

    if request.method == "POST":
        try:
            length = int(request.form.get("length", 12))
            upper = "upper" in request.form
            lower = "lower" in request.form
            digits = "digits" in request.form
            symbols = "symbols" in request.form
            safe_symbols = "safe_symbols" in request.form

            password = generate_password(
                length,
                upper=upper,
                lower=lower,
                digits=digits,
                symbols=symbols,
                safe_symbols=safe_symbols,
            )
        except ValueError as e:
            error = str(e)

    return render_template("index.html", password=password, error=error)

if __name__ == "__main__":
    app.run(debug=True)