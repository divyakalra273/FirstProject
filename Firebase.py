import pyrebase
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
email=input("Enter Email")
password=input("enter pass")
auth.create_user_with_email_and_password(email, password)

print("done")