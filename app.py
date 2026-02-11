from flask import Flask, render_template, request
import numpy as np
import pickle

app = Flask(__name__)

# ---------- LOAD MODEL ----------
with open("mini_project.pkl", "rb") as f:
    m, c = pickle.load(f)

# Convert safely
m = np.array(m)
c = float(c)

# Flatten m if needed
if m.ndim > 1:
    m = m.flatten()

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    try:
        # Read inputs
        data = np.array([
            float(request.form["bedrooms"]),
            float(request.form["bathrooms"]),
            float(request.form["sqft_living"]),
            float(request.form["sqft_lot"]),
            float(request.form["floors"]),
            float(request.form["waterfront"]),
            float(request.form["view"]),
            float(request.form["condition"]),
            float(request.form["sqft_above"]),
            float(request.form["sqft_basement"]),
            float(request.form["yr_built"]),
            float(request.form["yr_renovated"]),
            float(request.form["city"]),
            float(request.form["country"]),
            float(request.form["year"]),
            float(request.form["month"]),
            float(request.form["day"])
        ])

        # ---------- SHAPE CHECK ----------
        if m.size != data.size:
            return render_template(
                "index.html",
                error=f"Model expects {m.size} features, but received {data.size}. "
                      f"Please re-save the model correctly."
            )

        # Prediction
        price = np.dot(data, m) + c
        price = round(float(price), 2)

        return render_template("index.html", prediction=price)

    except Exception as e:
        return render_template("index.html", error=str(e))

if __name__ == "__main__":
    app.run(debug=True)
pytho