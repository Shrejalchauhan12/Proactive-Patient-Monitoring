import pickle
import numpy as np
import csv
import os
import io
from flask import Flask, request, render_template,jsonify
import pandas as pd


app = Flask(__name__)

# Load models
with open("diabetesresult.pkl", "rb") as f:
    diabetes_model = pickle.load(f)

with open("migraineresult.pkl", "rb") as f:
    migraine_model = pickle.load(f)

with open("covidresult.pkl", "rb") as f:
    covid_model = pickle.load(f)

# Path to CSV
CSV_FILE = 'user_data.csv'

def create_csv_if_not_exists():
    if not os.path.isfile(CSV_FILE):
        with open(CSV_FILE, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Name', 'Age', 'Month'])

create_csv_if_not_exists()


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("aboutUs.html")

@app.route('/vitality_monitor')
def vitality_monitor():
    return render_template('Vitality Monitor.html')

@app.route("/icons")
def icons():
    return render_template("icons.html")

@app.route('/report')
def report():
    return render_template('report.html')

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        if request.is_json:
            data = request.get_json()
            name = data.get('name')
            age = data.get('age')
            month = data.get('month')
            with open(CSV_FILE, 'a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow([name, age, month])
            return jsonify({'message': 'User data saved successfully', 'name': name})
        else:
            if request.method == 'POST':
                Pregnancies = float(request.form['Pregnancies'])
                Glucose = float(request.form['Glucose'])
                BloodPressure = float(request.form['BloodPressure']) 
                SkinThickness = float(request.form['SkinThickness']) 
                Insulin = float(request.form['Insulin']) 
                BMI = float(request.form['BMI']) 
                DiabetesPedigreeFunction = float(request.form['DiabetesPedigreeFunction'])     
                Age = float(request.form['Age']) 
    
        # Make prediction
        input_data = np.array([[Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age]])
        prediction = diabetes_model.predict(input_data)

        # Interpret prediction
        if prediction[0] == 1:
            result = "Diabetic"
        else:
            result = "Non-Diabetic"

        return render_template('diabetespredict.html', prediction_text=f'The patient is likely {result}')
    return render_template('diabetespredict.html')

@app.route('/migrainepredict', methods=['GET', 'POST'])
def migrainepredict():
    if request.method == 'POST':
        try:
            input_features = ['Age', 'Duration', 'Frequency', 'Location', 'Character', 'Intensity',
                              'Nausea', 'Vomit', 'Phonophobia', 'Photophobia', 'Visual', 'Sensory',
                              'Dysphasia', 'Dysarthria', 'Vertigo', 'Tinnitus', 'Hypoacusis', 'Diplopia',
                              'Defect', 'Ataxia', 'Conscience', 'Paresthesia', 'DPF']
            values = [float(request.form.get(field, 0)) for field in input_features]
            input_data = np.array([values])
            migraine_prediction = migraine_model.predict(input_data)
            result = migraine_prediction[0]
            return render_template('migrainepredict.html', prediction_text=f"The patient is likely having: {result}")
        except Exception as e:
            return render_template('migrainepredict.html', prediction_text=f"Error: {str(e)}")
    return render_template('migrainepredict.html')

@app.route('/covidpredict', methods=['GET', 'POST'])
def covidpredict():
    if request.method == 'POST':
        try:
            input_features = ["Breathing Problem", "Fever", "Dry Cough", "Sore throat", "Running Nose", "Asthma",
                              "Chronic Lung Disease", "Headache", "Heart Disease", "Diabetes", "Hyper Tension",
                              "Fatigue", "Gastrointestinal", "Abroad travel", "Contact with COVID Patient",
                              "Attended Large Gathering", "Visited Public Exposed Places",
                              "Family working in Public Exposed Places", "Wearing Masks", "Sanitization from Market"]
            values = [int(request.form.get(field, 0)) for field in input_features]
            input_data = np.array([values])
            prediction = covid_model.predict(input_data)
            result = "High Risk of COVID-19" if prediction[0] == 1 else "Low Risk of COVID-19"
            return render_template('covidpredict.html', prediction_text=f'Prediction: {result}')
        except Exception as e:
            return render_template('covidpredict.html', prediction_text=f"Error: {str(e)}")
    return render_template('covidpredict.html')

if __name__ == "__main__":
    app.run(debug=True)

