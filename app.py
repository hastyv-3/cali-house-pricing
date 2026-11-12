# Standard libraries
import pickle

# 3rd-party libraries
from flask import Flask, flash, request, app, jsonify, url_for, render_template, session
import numpy as np
import pandas as pd

app = Flask(__name__)
app.config["SECRET_KEY"] = "0gjwg08yk"

# Load model and scaler
regmodel = pickle.load(open("regmodel.pkl", "rb"))
scaler = pickle.load(open("scaling.pkl", "rb"))


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/predict_api", methods=["POST"])
def predict_api():
    data = request.json["data"]

    print(data)
    print(np.array(list(data.values())).reshape(1, -1))

    new_data = scaler.transform(np.array(list(data.values())).reshape(1, -1))
    output = regmodel.predict(new_data)

    print(output[0])

    return jsonify(output[0])


@app.route("/predict", methods=["POST"])
def predict():
    data = [float(x) for x in request.form.values()]

    final_input = scaler.transform(np.array(data).reshape(1, -1))
    print(final_input)

    output = regmodel.predict(final_input)[0]
    flash("The house price prediction is {}".format(output))
    return render_template("home.html")


if __name__ == "__main__":
    app.run(debug=True)
