from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "<h1>Congrats, it's a web app!</h1>"

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)