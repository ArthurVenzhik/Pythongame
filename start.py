import PySimpleGUI as sg

from gamelogic import GameLogic

if __name__ == "__main__":
    game = GameLogic()

    layout = [
        [sg.Text(f'Вгадайте число від 1 до 10:')],
        [sg.InputText(key='-GUESS-')],
        [sg.Button('Відправити', key='-SUBMIT-'), sg.Button('Нова гра'), sg.Button('Вийти')],
        [sg.Text('', size=(15, 2), key='-RESULT-')]
    ]

    window = sg.Window('Гра "Вгадай число"', layout)

    while True:
        event, values = window.read()

        if event in (sg.WIN_CLOSED, 'Вийти'):
            break

        if event == 'Нова гра':
            game.start_new_game()
            window['-RESULT-'].update('')
            window['-SUBMIT-'].update(disabled=False)
            continue

        if event == '-SUBMIT-':
            result = game.process_guess(values['-GUESS-'])
            window['-RESULT-'].update(result)

            if result.startswith('Вітаємо!'):
                window['-SUBMIT-'].update(disabled=True)

            window['-GUESS-'].update('')

    window.close()
