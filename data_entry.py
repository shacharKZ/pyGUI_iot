import PySimpleGUI as sg
import pandas as pd
import os
import firebase_handler
import time
# Add some color to the window
sg.theme('DarkTeal9')

FIRE_BASE_FILE = '/csv_file1'  # path inside firebase for the online xlsx (excel) file
FIRE_BASE_FILE_TMP_LOCAL = './csv_file1_tmp.xlsx'  # path for local copy for data from firebase
EXCEL_FILE = './Data_Entry.xlsx'  # local file
df = pd.read_excel(EXCEL_FILE)  # local file
firebase_handler.set_up_fire_base()  # might not work if firebase is not configure

default_size = (20, 1)
layout_home = [
    [sg.Button('Open local file and edit it manually')],
    [sg.Text('Please fill out the following fields:')],
    [sg.Text('Name', size=default_size), sg.InputText(key='Name')],
    [sg.Text('City', size=default_size), sg.InputText(key='City')],
    [sg.Text('Favorite Colour', size=default_size), sg.Combo(['Green', 'Blue', 'Red'], key='Favorite Colour')],
    [sg.Text('I speak', size=default_size),
                            sg.Checkbox('German', key='German'),
                            sg.Checkbox('Spanish', key='Spanish'),
                            sg.Checkbox('English', key='English')],
    [sg.Text('No. of Children', size=default_size), sg.Spin([i for i in range(0,16)], initial_value=0, key='Children')],
    [sg.Submit(), sg.Button('Clear'), sg.Exit()]
]

layout_firebase = [
    [sg.Text('This will work only if pre-configured', visible=True)],
    [sg.Button('Open file from fire base!')],
    [sg.Button('Update file to fire base', visible=False)],
    [sg.Exit()]
]

layout = [
    [sg.TabGroup([[sg.Tab('Home(local)', layout_home, visible=True),
                   sg.Tab('FireBase', layout_firebase, visible=True)
                   ]])],
    ]

window = sg.Window('Simple data entry form', layout, size=(500, 280), font=('Arial', 15))


def clear_input():
    for key in values:
        window[key]('')
    return None


while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    if event == 'Clear':
        clear_input()
    if event == 'Open local file and edit it manually':
        os.system(f'open {EXCEL_FILE}')
    if event == 'Submit':
        new_record = pd.DataFrame(values, index=[0])
        df = pd.concat([df, new_record], ignore_index=True)
        df.to_excel(EXCEL_FILE, index=False)
        sg.popup('Data saved!')
        clear_input()
    if event == 'Open file from fire base!':
        df = firebase_handler.get_csv_from_json_from_fire_base(FIRE_BASE_FILE)
        if df is None:
            sg.popup('Something did not work! check firebase_handler.py and firebase_key.json')
            continue
        df.to_excel(FIRE_BASE_FILE_TMP_LOCAL, index=False)
        time.sleep(0.07)
        os.system(f'open {FIRE_BASE_FILE_TMP_LOCAL}')
        window['Update file to fire base'].update(visible=True)
    if event == 'Update file to fire base':
        df = pd.read_excel(FIRE_BASE_FILE_TMP_LOCAL)
        # print(df)
        firebase_handler.update_csv_as_json_to_fire_base(df, FIRE_BASE_FILE)
        sg.popup('Data was update to firebase!')


window.close()
