from flask import Flask, render_template, request
from preprocess import word_extractor, symptoms
from predict import predictor
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
        return render_template('disease.html', text = text, final_symptoms = final_symptoms, diseases = diseases)

@app.route('/your-disease-re', methods=['POST'])
def home_repost():
    if request.method == 'POST':
        final_symptoms = request.form.getlist('disease_checkbox')
        diseases = predictor(final_symptoms)
        return render_template('disease.html', text = input_text, final_symptoms = final_symptoms, diseases = diseases)

if __name__ == '__main__':
    app.run(debug=True)
    