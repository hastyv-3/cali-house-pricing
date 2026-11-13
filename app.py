# Standard libraries
import pickle

# 3rd-party libraries
from flask import (
    Flask,
    flash,
    request,
    jsonify,
    url_for,
    render_template,
    redirect,
)
import numpy as np

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

    new_data = scaler.transform(np.array(list(data.values())).reshape(1, -1))
    output = regmodel.predict(new_data)

    return jsonify(output[0])


@app.route("/predict", methods=["POST"])
def predict():
    data = [float(x) for x in request.form.values()]

    final_input = scaler.transform(np.array(data).reshape(1, -1))

    output = regmodel.predict(final_input)[0]
    flash("The house price prediction is {}".format(output))
    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(debug=True)
