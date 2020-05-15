import pyrebase
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
config={
    "apiKey": "AIzaSyDcdQUrQ9bScQxsmmoBN3AM1YQ-22zol7o",
    "authDomain": "heartdiseaseprediction-4baa3.firebaseapp.com",
    "databaseURL": "https://heartdiseaseprediction-4baa3.firebaseio.com",
    "projectId": "heartdiseaseprediction-4baa3",
    "storageBucket": "heartdiseaseprediction-4baa3.appspot.com",
    "messagingSenderId": "633661163756",
    "appId": "1:633661163756:web:7e204fc68ecc9fd5483dc9",
    "measurementId": "G-DCHRMT59FN",
    "service-account":"heartdiseaseprediction-4baa3-firebase-adminsdk-p4zc3-15c662fb6a.json"
}
# cred = credentials.Certificate("firstproject-4df96-firebase-adminsdk-luuob-b99543344e.json")
# firebase_admin.initialize_app(cred)

firebase=pyrebase.initialize_app(config)
db=firebase.database()
db.child("User").child("Name").push("Divya")

