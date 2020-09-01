
from flask import Flask, request, jsonify, render_template
app = Flask(__name__)
@app.route('/')
def home():
    return render_template('index.html')

@app.route("/prediction")
def predict():
    return render_template('prediction.html')


if __name__ == "__main__":
    app.run()