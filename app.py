from flask import Flask, render_template, request
from preprocess import word_extractor, symptoms
from predict import predictor
import pyrebase

config = {
    "apiKey": "AIzaSyAtb_ClJ1maEUb20NZ3lNmPZJDMoX5M2mw",
    "authDomain": "ubuntu-doc-assist.firebaseapp.com",
    "databaseURL": "https://ubuntu-doc-assist.firebaseio.com",
    "projectId": "ubuntu-doc-assist",
    "storageBucket": "ubuntu-doc-assist.appspot.com",
    "messagingSenderId": "325752264622",
    "appId": "1:325752264622:web:255050e2424ad547035a3f",
    "measurementId": "G-65JHR5Q2B5"  
}

firebase = pyrebase.initialize_app(config)
db = firebase.database()

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

input_text = ''

@app.route('/your-disease', methods=['POST'])
def home_post():
    if request.method == 'POST':
        text = request.form.get('symptoms_input')
        words = word_extractor(text)
        final_symptoms = symptoms(words)
        diseases = predictor(final_symptoms)
        global input_text
        input_text = text
        
        if request.form.get('accept'):
            db.child('Accepted Diseases').child(input_text).update({"Symptoms": final_symptoms})
            db.child('Accepted Diseases').child(input_text).update({"Disease": diseases})
        
    return render_template('disease.html', text = text, final_symptoms = final_symptoms, diseases = diseases)

@app.route('/your-disease-re', methods=['POST'])
def home_repost():
    if request.method == 'POST':
        final_symptoms = request.form.getlist('disease_checkbox')
        diseases = predictor(final_symptoms)
        
        if request.form.get('accept'):
            db.child('Accepted Diseases').child(input_text).update({"Symptoms": final_symptoms})
            db.child('Accepted Diseases').child(input_text).update({"Disease": diseases})
            
    return render_template('disease.html', text = input_text, final_symptoms = final_symptoms, diseases = diseases)

if __name__ == '__main__':
    app.run(debug=True)
    