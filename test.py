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

input = 'I have a heavy cold and cough'
db = firebase.database()
db.child('Accepted Diseases').child(input).update({"Final Symptoms": 'cold'})
db.child('Accepted Diseases').child(input).update({"Disease": 'allergy'})
#db.child('input').child('name').update({"Input": input})