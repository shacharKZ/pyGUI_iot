import PySimpleGUI as sg
import pandas as pd

# Add some color to the window
sg.theme('DarkTeal9')

EXCEL_FILE = 'Data_Entry.xlsx'
df = pd.read_excel(EXCEL_FILE)

default_size = (20,1)
layout_home = [
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
    # [sg.Text('This will work only if you connected firebase right!')],
    [sg.Text('Not yet implemented')],
]

layout = [
    [sg.TabGroup([[sg.Tab('Home', layout_home, visible=True),
                   sg.Tab('FireBase', layout_firebase, visible=True)
                   ]])],
    ]
    # [sg.Button('Run'), sg.Button("Cancel")]]

window = sg.Window('Simple data entry form', layout, size=(500, 260), font=('Arial', 15))

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
    if event == 'Submit':
        new_record = pd.DataFrame(values, index=[0])
        df = pd.concat([df, new_record], ignore_index=True)
        df.to_excel(EXCEL_FILE, index=False)
        sg.popup('Data saved!')
        clear_input()


window.close()
