import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import pandas as pd
import json

def set_up_fire_base():
    # Fetch the service account key JSON file contents
    cred = credentials.Certificate('firebase_key.json')
    # Initialize the app with a service account, granting admin privileges
    firebase_admin.initialize_app(cred, {
        'databaseURL': 'https://demo1-ec9a9-default-rtdb.europe-west1.firebasedatabase.app/'
    })

def reset_db_with_dummy_data():
    ref = db.reference('/')
    ref.set({
        'students':
            {
                'student_key_1': {
                    'name': 'Alice',
                    'semester': 2,
                    'age': 22,
                },
                'student_key_2': {
                    'name': 'Bob',
                    'semester': 1,
                    'age': 23,
                },
                'student_key_3': {
                    'name': 'Mike',
                    'semester': 3,
                    'age': 21,
                },
            }
    })


def get_data_from_fire_base_path(path="",):
    ref = db.reference(path)
    return ref.get()


def add_data_to_fire_base_with_path(data, path="/"):
    ref = db.reference(path)
    # ref.push({'hello': {'hi': 3, 'holla': 4}})
    ref.push(data)


def upload_csv_as_json_to_fire_base(df: pd.DataFrame, path="/"):
    ref = db.reference(path)
    json_tmp = df.to_json()
    ref.push(json_tmp)

def update_csv_as_json_to_fire_base(df: pd.DataFrame, path="/"):
    ref = db.reference(path)
    json_tmp = df.to_json()
    ref.set(json_tmp)

'''This is a bad way to do so! find a better way!'''  # TODO !
def get_csv_from_json_from_fire_base(path="/"):
    ref = db.reference(path)
    dict_json_tmp = ref.get()
    # single_key = [x for x in dict_json_tmp][0]
    # json_tmp = json.loads(dict_json_tmp[single_key].__str__())
    json_tmp = json.loads(dict_json_tmp.__str__())
    df = pd.DataFrame(json_tmp)
    return df


set_up_fire_base()
# reset_db_with_dummy_data()
# add_data_to_fire_base_with_path({'hello': {'hi': 3, 'holla': 4}})
# print(get_data_from_fire_base_path("students"))

# df = pd.read_excel('./Data_Entry.xlsx')
# print(df)
# update_csv_as_json_to_fire_base(df, path='/csv_file1')
tmp = get_csv_from_json_from_fire_base(path='/csv_file1')
print(tmp)
# # tmp['Name'][1] = "AAAAAAAAA"
# tmp.loc[:, ('Name', 1)] = 'AAAAAA'
# print(tmp)
# update_csv_as_json_to_fire_base(tmp, path='/csv_file1')

