from flask import Flask, render_template, request, url_for
from preprocess import word_extractor, symptoms
from predict import predictor,cardio_predict,kidney_predict,pre_processing,bert_disease_predict
import pyrebase
import pandas as pd


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
@app.route('/symp_check')
def sym():
    return render_template('symp_check.html')

@app.route('/cardio_check')
def cardio():
    return render_template('cardio_check.html')

@app.route('/kidney_check')
def kidney():
    return render_template('kidney_check.html')

@app.route('/bert_disease_check')
def bert():
    return render_template('bert_symp_check.html')

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

@app.route('/your-cardio',methods = ['POST'])
def cardio_post():
    if request.method == 'POST':
        features = []
        phyAct = request.form.get('phyAct')
        features.append(phyAct)
        age = request.form.get('age')
        features.append(age)
        alc = request.form.get('alc')
        features.append(alc)
        sysBp = request.form.get('sysBp')
        features.append(sysBp)
        diaBp = request.form.get('diaBp')
        features.append(diaBp)
        chol = request.form.get('chol')
        features.append(chol)
        gender = request.form.get('gender')
        features.append(gender)
        gluc = request.form.get('gluc')
        features.append(gluc)
        height = request.form.get('height')
        features.append(height)
        smoke = request.form.get('smoke')
        features.append(smoke)
        weight = request.form.get('weight')
        features.append(weight)
        cardio = cardio_predict(features)
        print(cardio)
        if (cardio==[0]):
            cardio = '0'
        else:
            cardio = '1'
        return render_template('cardio.html', cardio = cardio)

@app.route('/your-kidney',methods = ['POST'])
def kidney_post():
    if request.method == 'POST':
        features = []
        age = request.form.get('age')
        features.append(age)
        al = request.form.get('al')
        features.append(al)
        ane = request.form.get('ane')
        features.append(ane)
        appet = request.form.get('appet')
        features.append(appet)
        bact = request.form.get('bact')
        features.append(bact)
        bg = request.form.get('bg')
        features.append(bg)
        bp = request.form.get('bp')
        features.append(bp)
        bu = request.form.get('bu')
        features.append(bu)
        cad = request.form.get('cad')
        features.append(cad)
        dm = request.form.get('dm')
        features.append(dm)
        hemp = request.form.get('hemp')
        features.append(hemp)
        htn = request.form.get('htn')
        features.append(htn)
        pc = request.form.get('pc')
        features.append(pc)
        pcc = request.form.get('pcc')
        features.append(pcc)
        pcv = request.form.get('pcv')
        features.append(pcv)
        pe = request.form.get('pe')
        features.append(pe)
        pot = request.form.get('pot')
        features.append(pot)
        rbc = request.form.get('rbc')
        features.append(rbc)
        rc = request.form.get('rc')
        features.append(rc)
        sc = request.form.get('sc')
        features.append(sc)
        sg = request.form.get('sg')
        features.append(sg)
        sod = request.form.get('sod')
        features.append(sod)
        su = request.form.get('su')
        features.append(su)
        wc = request.form.get('wc')
        features.append(wc)
        print(len(features))
        kid = kidney_predict(features)
        if (kid==[0.]):
            kid = '0'
        else:
            kid = '1'
        return render_template('kideny.html', kid = kid)


@app.route('/your-bert-diease', methods=['POST'])
def bert_post():
    text = request.form.get('bert_symptoms_input')
    df = pd.read_csv('dataset/dis_symp_prcoseessd.csv')
    text = pre_processing(text)
    results = bert_disease_predict(text)
    number_top_matches = 10
    diseases = []
    item = []
    i = 0
    score = []
    info = []
    for idx, distance in results[0:number_top_matches]:
        diseases.append(df['diseases'][idx])
        score.append(1-distance)
        i = i+1
        item.append(i)
        info.append(df['Overview'][idx])

    return render_template('bert.html',prediction = diseases,item = item,similarity = score,summary = score,overview = info)
if __name__ == '__main__':
    app.run(debug=True)
    