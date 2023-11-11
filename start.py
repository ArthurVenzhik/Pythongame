import PySimpleGUI as sg
from gamelogic import GameLogic

class GameGUI:
    def __init__(self):
        self.game = GameLogic()

        layout = [
            [sg.Text('Вгадайте число від 1 до 10:')],
            [sg.InputText(key='-GUESS-', enable_events=True, focus=True, size=(10, 1)), sg.Button('Відправити', key='-SUBMIT-'), sg.Button('Нова гра'), sg.Button('Вийти')],
            [sg.Text('', size=(25, 2), key='-RESULT-', justification='center')],
            [sg.Text('Спроб за гру:', size=(15, 1)), sg.Text('0', key='-ATTEMPTS-', size=(3, 1))],
            [sg.Text('Максимальна кількість спроб:', size=(25, 1)), sg.Text('3', key='-MAX_ATTEMPTS-', size=(3, 1))]
        ]

        self.window = sg.Window('Гра "Вгадай число"', layout, finalize=True)
        self.window['-GUESS-'].bind('<Return>', '_SUBMIT_')

    def run(self):
        while True:
            event, values = self.window.read()

            if event in (sg.WIN_CLOSED, 'Вийти'):
                break

            if event == 'Нова гра':
                self.game.start_new_game()
                self.update_attempts_display()
                self.window['-RESULT-'].update('')
                self.window['-SUBMIT-'].update(disabled=False)
                continue

            if event in ('-SUBMIT_', '-SUBMIT-') and not self.window['-SUBMIT-'].Disabled:
                result = self.game.process_guess(values['-GUESS-'])
                self.window['-RESULT-'].update(result)
                self.update_attempts_display()

                if result.startswith('Вітаємо!'):
                    self.window['-SUBMIT-'].update(disabled=True)

                self.window['-GUESS-'].update('')

        self.window.close()

    def update_attempts_display(self):
        self.window['-ATTEMPTS-'].update(str(self.game.attempts))
        self.window['-MAX_ATTEMPTS-'].update(str(self.game.max_attempts))

if __name__ == "__main__":
    game_gui = GameGUI()
    game_gui.run()
