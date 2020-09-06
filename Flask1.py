from flask import *
import pyrebase
from sklearn.externals import joblib
import os
import numpy as np
import pickle

import pandas as pd

import seaborn as sns
from matplotlib import pyplot as plt
from sklearn.model_selection import train_test_split


from nltk.chat.util import Chat, reflections

from Session71 import chat

app = Flask(__name__)

config = {
    "apiKey": "AIzaSyD8KVaL8tdE1N0Bn12i2glgJxEddB6x808",
    "authDomain": "firstproject-4df96.firebaseapp.com",
    "databaseURL": "https://firstproject-4df96.firebaseio.com",
    "projectId": "firstproject-4df96",
    "storageBucket": "firstproject-4df96.appspot.com",
    "messagingSenderId": "672093701655",
    "appId": "1:672093701655:web:7f58c784c845e58ed8fe52",
    "measurementId": "G-7YYMQY56YP"
  }
firebase = pyrebase.initialize_app(config)
db = firebase.database()
auth = firebase.auth()


conversation = [
        [
            "Hi",
            ["Hey, What can i do for you ?", ]
        ],

        [
            "What is Your Name ?",
            ["My Name is John. Good to Talk to You !! What is your Name ?", ]
        ],

        [
            r"my name is (.*)",
            ["Hello %1, Its good to chat with You !! What programming languages you know?", ]
        ],

        [
            r"i know (.*)",
            ["OK!! So you can code in %1", "this is great that you know %1"]
        ],

    ]

@app.route("/")
def home():

    return render_template('HomePage.html')

@app.route("/mainview",methods=['GET','POST'])
def mainView():

    return render_template('MainView.html')






@app.route("/login",methods=['GET','POST'])
def login():
    if request.method == "POST":

        error = None
        email = request.form['email']
        password = request.form['password']

        # try:
        auth.sign_in_with_email_and_password(email, password)
            # flash('Invalid credentials')
        # except:
        #     flash('You are successfully logged in')
        return redirect(url_for("mainView"))



    return render_template('LoginNew.html')



@app.route("/signIn",methods=['GET','POST'])
def signIn():
    if request.method == 'POST':
        name=request.form['firstName']
        lastName=request.form['lastName']
        email = request.form['email']
        password = request.form['password']
        repass = request.form['password1']
        birthDate=request.form['birthdate']
        phoneNumber=request.form['phoneNumber']
        height=request.form['height']
        weight=request.form['weight']
        gender = request.form['gender']


        auth.create_user_with_email_and_password(email, password)
        if password == repass:

            db.child("firstName").push({"firstName": name})
            db.child("lastName").push({"lastName": lastName})
            db.child("email").push({"email": email})
            db.child("password").push({"password": password})
            db.child("birthDate").push({"birthdate": birthDate})
            db.child("phoneNumber").push({"phoneNumber": phoneNumber})
            db.child("height").push({"height": height})
            db.child("weight").push({"weight": weight})
            db.child("gender").push({"gender": gender})

            return redirect(url_for("mainView"))
        else:
           print("Password not matched")


    return render_template('RegisterNew.html')

@app.route("/chatbot",methods=["GET","POST"])
def chatBot():
    if request.method == 'POST':

        user_input = request.form['msg']

        bot_response =chat(user_input)
        bot_response = str(bot_response)
        print("Friend: " + bot_response)
    return render_template('Chatbot.html', user_input=user_input,
                               bot_response=bot_response
                               )
        # mess=request.form("msg")
        # chat(mess)

    # return render_template("ChatBot.html")
"""@app.route("/get")

def get_bot_response():
    userInput = request.args.get('msg')

    greetings = ['hola', 'hello', 'hi', 'Hi', 'hey!', 'hey']

    question = ['How are you?', 'How are you doing?']
    responses = ['Okay', "I'm fine"]
    while True:

        if userInput in greetings:
            random_greeting = random.choice(greetings)
            value = random_greeting
            return value
        elif userInput in question:
            random_response = random.choice(responses)
            value = random_response
            return value
        else:
            value = "I did not understand what you said"
            return value
"""
@app.route("/prediction",methods=["GET","POST"])
def prediction():
    if request.method == 'POST':
        if request.method == 'POST':
            age = int(request.form['age'])
            sex = int(request.form['sex'])
            trestbps = float(request.form['trestbps'])
            chol = float(request.form['chol'])
            restecg = float(request.form['restecg'])
            thalach = float(request.form['thalach'])
            exang = int(request.form['exang'])
            cp = int(request.form['cp'])
            fbs = float(request.form['fbs'])
            x = np.array([age, sex, cp, trestbps, chol, fbs, restecg,
                          thalach, exang]).reshape(1, -1)

            scaler_path = os.path.join(os.path.dirname(__file__), 'models/scaler.pkl')
            scaler = None
            with open(scaler_path, 'rb') as f:
                scaler = pickle.load(f)

            x = scaler.transform(x)

            model_path = os.path.join(os.path.dirname(__file__), 'models/rfc.sav')
            clf = joblib.load(model_path)

            y = clf.predict(x)
            print(y)

            # No heart disease
            if y == 0:
                return render_template('nodisease.html')

            # y=1,2,4,4 are stages of heart disease
            else:
                return render_template('heartdisease.html', stage=int(y))
    return render_template("HeartPredictionView.html")

@app.route("/stats",methods=["GET","POST"])
def statstics():
    if request.method=="POST":
        df = pd.read_csv('heart.csv')
        df.head()
        bins = ['sex', 'fbs', 'exang']
        cats = ['cp', 'restecg', 'slope', 'thal']
        ords = ['ca']
        nums = ['age', 'oldpeak', 'trestbps', 'chol', 'thalach']
        target = ['target']
        df.cp = df.cp.replace({0: 'Asympt.', 1: 'Atypical', 2: 'Non', 3: 'Typical'})
        df.restecg = df.restecg.replace({0: 'LV hyper', 1: 'Normal', 2: 'ST-T wave'})
        df.slope = df.slope.replace({0: 'down', 1: 'up', 2: 'flat'})
        df.thal = df.thal.replace({0: 'NA', 1: 'Fixed', 2: 'Normal', 3: 'Revers.'})
        X_train, X_test, y_train, y_test = train_test_split(df,
                                                            df.target,
                                                            test_size=0.2,
                                                            random_state=42,
                                                            stratify=df.target)

        fig = plt.figure(figsize=(8, 6))
        fig.subplots_adjust(hspace=0.4, wspace=0.4, bottom=0.01, top=0.95)

        for i, var in enumerate(cats):
            i = i + 1
            ax = fig.add_subplot(2, 2, i)
            ax.set_xticklabels(ax.get_xticklabels(), rotation=45)
            sns.countplot(data=X_train, x=var, hue='target', ax=ax)
        plt.savefig('static\graphimage.jpeg',bbox_inches='tight')
        plt.show()

        df.restecg = df.restecg.replace({'Normal': 0, 'LV hyper': 1, 'ST-T wave': 1})
        df.thal = df.thal.replace({'NA': 0, 'Normal': 0, 'Fixed': 1, 'Revers.': 1})
        X_train, X_test, y_train, y_test = train_test_split(df,
                                                            df.target,
                                                            test_size=0.2,
                                                            random_state=42,
                                                            stratify=df.target)
        bins = ['sex', 'fbs', 'exang', 'thal', 'restecg']
        cats = ['cp', 'slope']

        fig = plt.figure(figsize=(8, 6))
        fig.subplots_adjust(hspace=0.4, wspace=0.4, bottom=0.01, top=0.95)

        for i, var in enumerate(bins):
            i = i + 1
            ax = fig.add_subplot(2, 3, i)
            sns.countplot(data=X_train, x=var, hue='target', ax=ax)
        plt.savefig('static\graphimage2.png',bbox_inches='tight')
        plt.show()

    return render_template("Stats.html")


def generateGraph():
    table = pd.read_csv("recons_dataset\combined_dataset.csv")
    male=table['tsex']==1
    female=table['tsex']==0
    plt.plot(male.index, female.values)
    plt.xlabel("Male")
    plt.ylabel("Female")
    plt.title("Risk factor according to gender")

    plt.show()
    plt.savefig('static\graphimage.png',bbox_inches='tight')




if __name__=='__main__':

    app.run(debug=True)
