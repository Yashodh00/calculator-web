from flask import Flask, render_template, request, jsonify
from lib import calculate_expression

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/calculate", methods=["POST"])
def calculate():
    data = request.get_json()

    expression = data.get("expression", "")

    result = calculate_expression(expression)

    return jsonify({
        "result": result
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)