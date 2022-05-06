import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("firebase_key.json")
firebase_admin.initialize_app(cred, {'databaseURL': 'https://demo1-ec9a9.firebaseio.com'})

ref = db.reference('students')
print(ref)
collection_ref = ref.child('students')
print(collection_ref)

