# Standard libraries
import pickle

# 3rd-party libraries
from flask import (
    abort,
    Flask,
    flash,
    request,
    jsonify,
    url_for,
    render_template,
    redirect,
)
import numpy as np

# User-created libraries
from helper import sanitize_input

PREDICTORS = ("MedInc", "HouseAge", "AveRooms", "AveBedrms", "Population", "AveOccup",
              "Latitude", "Longitude")

app = Flask(__name__)
app.config["SECRET_KEY"] = "0gjwg08yk"

# Load model and scaler
with open("regmodel.pkl", "rb") as file:
    regmodel = pickle.load(file)

with open("scaling.pkl", "rb") as file:
    scaler = pickle.load(file)


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/predict_api", methods=["POST"])
def predict_api():
    data = request.json["data"]
    sorted_data = sanitize_input(data, PREDICTORS)


    final_input = scaler.transform(np.array(list(sorted_data.values())).reshape(1, -1))
    output = regmodel.predict(final_input)

    return jsonify(output[0])


@app.route("/predict", methods=["POST"])
def predict():
    data = request.form
    sorted_data = sanitize_input(data, PREDICTORS)

    final_input = scaler.transform(np.array(sorted_data.values()).reshape(1, -1))
    output = regmodel.predict(final_input)[0]
    
    flash(f"The house price prediction is ${(output * 100000):.2f}")
    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(debug=True)
