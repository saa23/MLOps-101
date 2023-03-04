from flask import Flask, request, jsonify
import joblib
import pandas as pd
import numpy as np

# Your API definition
app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    json_ = request.json
    query = pd.get_dummies(pd.DataFrame(json_), dummy_na=True)
    query = query.reindex(columns=model_columns, fill_value=0)
    prediction = list(lr.predict(query))
    return jsonify({'prediction': str(prediction)})

if __name__ == '__main__':
    lr = joblib.load("model.pkl")                       # Load "model.pkl"
    model_columns = joblib.load("model_columns.pkl")    # Load "model_columns.pkl"
    app.run(debug=True)
    