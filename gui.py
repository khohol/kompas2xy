import PySimpleGUI as sg
import main

sg.theme('Dark')

layout = [  [sg.Text('Дані з компасу:'), sg.Input(key='-INPUT-')],
            [sg.Text('Знаків після коми:'), sg.Input(key='-FLOAT-', default_text='2')],
            [sg.Button('Конвертувати', key='-CONVERT-'), sg.Button('Exit')],
            [sg.Text('Х', size=(15,0)), sg.Text('Y', size=(15,0)), sg.Text('Z', size=(15,0))],
            [sg.Output(size=(15,20), key='-XCOORD-'), sg.Output(size=(15,20), key='-YCOORD-'),sg.Output(size=(15,20), key='-ZCOORD-')]]

window = sg.Window('kompas2xy', layout)

while True:  # Event Loop
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    if event == '-CONVERT-':
        xCoord, yCoord, zCoord = main.inputData(inputValue=values['-INPUT-'], outputFloat=int(values['-FLOAT-']))
        window['-XCOORD-'].update(xCoord)
        window['-YCOORD-'].update(yCoord)
        window['-ZCOORD-'].update(zCoord)

window.close()