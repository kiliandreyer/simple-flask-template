from flask import Flask, render_template

app = Flask(__name__)

@app.route("/", methods=["POST", "GET"])
def home():
    message = "This is a Flask Template"
    return render_template('index.html', message=message)

if __name__ == "__main__":
    app.run(debug=True)