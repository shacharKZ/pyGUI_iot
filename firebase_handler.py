# import firebase_admin
# from firebase_admin import credentials
# from firebase_admin import db
#
# cred = credentials.Certificate("firebase_key.json")
# firebase_admin.initialize_app(cred, {'databaseURL': 'https://demo1-ec9a9.firebaseio.com'})
#
# ref = db.reference('/students')
# try:
#     print(ref.get())
# except():
#     print("!!!! did not work1")
# collection_ref = ref.child('students')
# try:
#     print(collection_ref.get())
# except():
#     print("!!!! did not work2")


#
# import os
# import firebase_admin
# from firebase_admin import db
#
#
# API_REQUEST_DATETIME_FORMAT = '%d-%m-%YT%H-%M-%S'
# STORAGE_BUCKET = 'demo1-ec9a9.appspot.com'
# # os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = f'{os.sep}home{os.sep}demo1-ec9a9-firebase-adminsdk.json'
# # os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'C:\\Users\\1912m\\mobilapse-firebase-key.json'
#
# # ROOT_CAPTURES_FOLDER_PATH = f'{os.sep}home{os.sep}pi{os.sep}cap_images{os.sep}'
#
# FIREBASE_RT_DB_URL = 'https://demo1-ec9a9-default-rtdb.europe-west1.firebasedatabase.app/'
#
# print('initializing FIREBASE')
# default_app = firebase_admin.initialize_app(credential=None, options={'storageBucket': STORAGE_BUCKET,
#                                                                       'databaseURL': FIREBASE_RT_DB_URL})
# print('FIREBASE ready!')
#
#
# ref = db.reference('/students')
# print(ref.get())
# # CAMERA_PATH = f'{os.sep}dev{os.sep}v4l{os.sep}by-id{os.sep}usb-USB2.0_UVC_VGA_USB2.0_UVC_VGA-video-index'
#
# DB_UPDATES = True


import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

# Fetch the service account key JSON file contents
cred = credentials.Certificate('firebase_key.json')
# Initialize the app with a service account, granting admin privileges
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://demo1-ec9a9-default-rtdb.europe-west1.firebasedatabase.app/'
})

ref = db.reference('/')
ref.set({
        'boxes':
            {
                'box001': {
                    'color': 'red',
                    'width': 1,
                    'height': 3,
                    'length': 2
                },
                'box002': {
                    'color': 'green',
                    'width': 1,
                    'height': 2,
                    'length': 3
                },
                'box003': {
                    'color': 'yellow',
                    'width': 3,
                    'height': 2,
                    'length': 1
                }
            }
        })

ref.push({'hello': {'hi': 3, 'holla': 4}})


ref2 = db.reference('boxes')

print(ref2.get('/'))

