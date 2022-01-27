import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__)
model = pickle.load(open('model2.pkl', 'rb'))


@app.route('/')
def home():
    return render_template('index2.html')


@app.route('/predict', methods=['POST'])
def predict():
    # For rendering results on HTML GUI
    float_features = [float(x) for x in request.form.values()]
    final_features = [np.array(float_features)]
    prediction = model.predict(final_features)

    output = prediction[0]
    if output == 1:
        output = "Severe!"
    else:
        output = "None!"

    return render_template('index2.html', prediction_text='Chances of flood occurring are: {}'.format(output))


if __name__ == "__main__":
    app.run(debug=True)
