from flask import Flask, render_template, request
from preprocess import word_extractor, symptoms
from predict import predictor
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/your-disease', methods=['POST'])
def home_post():
    text = request.form.get('symptoms_input')
    words = word_extractor(text)
    final_symptoms = symptoms(words)
    print(final_symptoms)
    disease = predictor(final_symptoms)[0]
    return render_template('disease.html', text = text, final_symptoms = final_symptoms, disease = disease)


if __name__ == '__main__':
    app.run(debug=True)
    