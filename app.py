from flask import Flask, render_template, request, jsonify
import joblib
import numpy as np

app = Flask(__name__)
model = joblib.load('iris_pipeline.pkl')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    try:
        features = np.array([[float(data['sepal_length']),
                              float(data['sepal_width']),
                              float(data['petal_length']),
                              float(data['petal_width'])]])
        pred = model.predict(features)[0]
        return jsonify({'prediction': pred})
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)
